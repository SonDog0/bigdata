# ggplot2

기본적으로 ggplot 함수를 이용해 만들고
연산자를 이용해 레어어를 추가하는 방식으로 나머지 부분을 그림

레이어 : 점,선, 히스토그램등의 기하학적 그래프를 그려주는 요소
일반적으로 geom_ 접두사로 시작함
geom_point
geom_line
geom_histogram


install.packages('ggplot2')
library(ggplot2)

head(diamonds)

# 그래프를 그리기 위한 프레임 표시
ggplot(diamonds)

# aesthetic으로 그래프 외간(x,y축,색)의 지정
gg <- ggplot(diamonds, aes(x=carat, y=price, color='red'))

# 점그래프 그림
gg + geom_point()



gg <- ggplot(diamonds)
gg + geom_point(aes(x=carat, y=price, color=cut))


# 선그래프

gg <- ggplot(diamonds)
gg + geom_line(aes(x=carat, y=price, color=cut))

# 히스토그램
gg <- ggplot(diamonds)
gg + geom_histogram(aes(x=carat, y=price))


# 점 +  선
gg <- ggplot(diamonds)
gg <- gg + geom_point(aes(x=carat, y=price))
gg + geom_line(aes(x=carat, y=price))


# 밀도 그래프
ggplot(diamonds) + geom_density(aes(x=carat), fill='grey') 
ggplot(diamonds) + geom_density(aes(x=carat), fill='red')



ggplot(diamonds) + geom_boxplot(aes(x=cut, y=price))

ex) mtcars 차량중량 대비 연비 점그래프
str(mtcars)
ggplot(data=mtcars) + geom_point(aes(x=wt, y=mpg, color=cyl))


ex) economics 
년도별 실업률
년도별 인구수
점 / 꺽은선 그래프

str(economics)


ggplot(economics) + geom_point(aes(x=date, y=unemploy))
ggplot(economics) + geom_point(aes(x=date, y=pop))

ggplot(economics) + geom_line(aes(x=date, y=unemploy))
ggplot(economics) + geom_line(aes(x=date, y=pop))


# ggplot의 경량화 버전 - qplot
R의 기본 그래프 패키지를 확장


nrow(diamonds)

set.seed(20181116)   # 난수생성을 위한 seed 설정
tinydia <- diamonds[sample(nrow(diamonds), 1000), ]

#기본사용법
qplot(x=carat, y=price, data=tinydia)

# 색상지정
qplot(x=carat, y=price, data=tinydia, colour=color)

# shape 그래프 표시점 모양지정
qplot(x=carat, y=price, data=tinydia, shape=cut)
qplot(x=carat, y=price, data=tinydia, shape=cut, colour=color)


# 그래프에 회귀선을 추가하고 
# 신뢰구간 표시하기
library(splines)

qplot(carat, price, data=tinydia, geom = c('point','smooth'), method='lm')


# 상자그래프
qplot(color, price/carat, data=tinydia, geom='boxplot')


# 히스토그램
qplot(carat, data=tinydia, geom='histogram', fill=color)

# 막대그래프
qplot(color, data=tinydia, geom='bar', fill=color)
tinydia

# 선그래프
qplot(date, pop, data=economics, geom='line', colour='red')


# 그래프 축, 제목, 레이블 세부 지정
qplot(carat, price, data=tinydia, xlab='캐럿',ylab='가격',main='캐럿당 가격')
?qplot

# 부분 데이터(facet)를 이용한 그래프 출력
qplot(carat, data=tinydia,
      geom = 'histogram',
      facets = color~.)

qplot(carat, data=tinydia,
      geom = 'histogram',
      facets = .~color)



# iris- 꽃잎길이 대비 꽃받침길이
str(iris)
qplot(Sepal.Length,Sepal.Width,data=iris)
qplot(Petal.Length,Petal.Width,data=iris, colour=Species, shape=Species)


# Cars93 - 고속도로 연비 막대 그래프
library(MASS)
str(Cars93)

qplot(MPG.highway, data=Cars93,
      geom = 'bar', fill=Cylinders)


# Cars93 - 고속도로 연비 drv 변수로 부분화시켜 막대그래프 그리기
# (열단위 출력)
qplot(MPG.highway, data=Cars93,
      geom = 'histogram',
      facets = .~Origin)

# Cars93 - 고속도로 연비 wt 변수로 부분화시켜 막대그래프 그리기
qplot(MPG.city, Weight, data=Cars93)



# mtcars
차체중량 연비 대비 산점도
생상은  carb, 모양은 cyl
크기는 qsec
str(mtcars)
mtcars
qplot(wt, mpg, data = mtcars, colour=as.factor(carb), shape=as.factor(cyl), size=qsec)


# mtcars
차체중량 연비 대비 산점도
단, 각 점에 자동차 이름을 레이블로 표시

qplot(wt, mpg, data=mtcars,
      label=rownames(mtcars),
      geom=c('point','text'),
      hjust=-0.1,vjust=0.5)

점,선 표시

qplot(wt, mpg, data=mtcars,
      geom=c('point','line'),
      colour=as.factor(cyl),
      linetype=as.factor(cyl))

qplot(clarity,data = tinydia, fill=cut)
