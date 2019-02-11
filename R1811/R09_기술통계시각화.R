# 그래프 기초
# 숫자와 텍스트만으로 작성된 통계 결과는 지루/따분
# 그래프와 그림형태로 제시 (시각적 묘사)
# => 열정적 반응(데이터의 관계 구분 용이)

# 양적변수 - 이산(정수), 연속(실수)

# 그래프 - plot, hist, boxplot

# 산점도 plot
# 연속형 데이터를 이용해서 작성해보는 기본적인 그래프
# 실제값은 x 축에 예측값은 y축에 배치 
# 데이터들의 분포를 시각적으로 나타냄

#정규분포를 따르는 난수 15개를 생성한 후 산점도 그림
plot(rnorm(15))

# 히스토그램(막대그래프)
# 관측치의 빈도분포를 시각적으로 나타냄
# 그룹, 계급은 x축, 빈도수는 y축에 배치
hist(rnorm(15))

# 박스 그래프, 상자수염 그래프
# 각종 기술통계수치 
# 최대값, 최소값, 사분위값, 중앙값등을 이용
boxplot(rnorm(15))

# 사례 : 두 약물에 따른 환자 반응
dose <- c(20,30,40,45,60)
drugA <- c(16,20,27,40,60)
drugB <- c(15,18,25,31,40)

# A약에 대한 반응 - 산점도
plot(drugA)   # x축 값은 1부터
plot(dose,drugA)    # x축 값은 dose

# B약에 대한 반응 - 산점도
plot(drugB)
plot(dose,drugB)    

# 산점도 시각화 옵션
plot(drugA, type='p')  #점 point
plot(drugA, type='l')  #선 line
plot(drugA, type='b')  #선 점 both
plot(drugA, type='h')  #수직선 
plot(drugA, type='s')  #계단

# 그래프 다양한 설정 알아보기

#현재 그래프 매개변수 설정 저장
.opar <- par(no.readonly = FALSE)

par(pch=17, lty=2, lwd=3, cex=2,bg='light cyan')

#pch : 점 종류(0 ~ 25)
#lty : 선 종류(1 ~ 6)
#cex : 기호크기(1,0.5,1.5)
#lwd : 선굵기(1)
#bg : 배경색
plot(drugB, type = 'b')

par(.opar)   # 그래프 매개변수 초기화

#모든 설정을 지정해서 그래프 작성
plot(drugA, type='b', col='red',main='메인',sub='밑에 뜸',
     fg='orange',xlab='x축',ylab='y축',
     pch=16,lty=3,cex=0.5,
     xlim=c(-5,10), ylim=c(0,100))

# 두개의 그래프 그리기
plot(drugA, type='b',col='red',ylab='drugs')
lines(drugB, type='b',col='blue')
grid()   # 모눈 표시

# cars 데이터셋을 이용한 그래프 그리기
# 자동차 제동거리관련 데이터
str(cars)

plot(cars$speed)
plot(cars$dist)

#변수 두개를 사용 - 회귀직선 그리기
plot(cars$speed, cars$dist)
grid()
abline(lm(cars$dist~cars$speed),col='red')

# 리더쉽 - 매니져별 나이에 대한 산점도
manager <-c(1:5)
date <-c('10/24/14','10/28/14','10/01/14','10/12/14','05/01/14')
country <- c('US','US','UK','UK','UK')
gender <-c('M','F','F','M','F')
age <-c(32,45,25,39,99)

leadership <- data.frame(manager,date,country,gender,age)

str(leadership)


plot(leadership$manager,leadership$age)
grid()

# 매니져별 나이에 대한 산점도 - 성별표시
#gender가 범주형 변수이므로
# level에 따라 점모양을 다르게 출력
plot(leadership$manager,leadership$age, pch=as.integer(leadership$gender)) 


# 매니져별 나이에 대한 산점도 - 국적표시
plot(leadership$manager,leadership$age, pch=as.integer(leadership$country)) 

# iris 데이터셋
# 붓꽃 꽃잎 길이/너비와 붓꽃받침 길이/너비에 따라
# 붓꽃을 분류해 놓은 데이터
?iris
str(iris)

#붓꽃 꽃잎 길이/너비(petal)
plot(iris$Petal.Length,iris$Petal.Width)
#붓꽃받침 길이/너비(sepal)
plot(iris$Sepal.Length,iris$Sepal.Width)
#붓꽃 꽃잎 길이/너비(petal)&붓꽃 종류
plot(iris$Petal.Length,iris$Petal.Width, pch=as.integer(iris$Species), col=iris$Species)
#붓꽃받침 길이/너비(sepal)&붓꽃 종류
plot(iris$Sepal.Length,iris$Sepal.Width, pch=as.integer(iris$Species), col=iris$Species)

head(iris)
str(iris)
as.integer(iris$Species)

# 범례 추가하기 - legend
with(leadership, plot(manager,age,pch=as.integer(gender),col=as.integer(gender)))
legend('topleft',c('Male','Female'), pch=c(1,2), col=c(1,2))

# 
plot(iris$Petal.Length,iris$Petal.Width, pch=as.integer(iris$Species), col=iris$Species)
legend('topleft',c('setosa','versicolor','virginica'), 
       pch=as.integer(iris$Species[c(1,51,101)]), col=as.integer(iris$Species[c(1,51,101)]))

plot(iris$Petal.Length,iris$Petal.Width, pch=as.integer(iris$Species), col=iris$Species)
legend('topleft',c('setosa','versicolor','virginica'), 
       pch=1:3, col=1:3)

plot(iris$Sepal.Length,iris$Sepal.Width, pch=as.integer(iris$Species), col=iris$Species)
legend('topright',c('setosa','versicolor','virginica'), 
       pch=1:3, col=1:3)

# 산점도 각 점에 수치 표시
plot(drugA, type='p',col='red')
grid()
# text(drugA, cex=0.7, lab=drugA, adj=c(0,0))
# text(drugA, cex=0.7, lab=drugA, adj=c(-1,1))
# text(drugA, cex=0.7, lab=drugA, adj=c(1,1))
text(drugA, cex=0.7, lab=drugA, adj=c(0.5,0 )) # (양수 왼쪽,양수 아래)
text(drugA, cex=0.7, lab=drugA, adj=c(3,3 )) # (양수 왼쪽,양수 아래)




# 그래프 눈금 다루기
plot(drugA, type='p',col='red')  # x축은 눈금이 잘 나오는데 y축은 눈금 간격이 넓음

plot(drugA, type='p',col='red', axes=F, ann=F)  # 죄다지움

axis(1, at=seq(1:5))
axis(1, at=1:5, lab=c('A','B','C','D','E'))

axis(2, at=seq(0:70))
# axis(2, ylim=c(0,70))
box()

# 제목 다루기
plot(drugA, type='p',col='red', ann=F)  # 죄다지움
title(main='환자 투약 효과',col.main='red', font.main=4)
title(xlab='환자',col.lab='blue', font.lab=3)
title(ylab='환자',col.lab='green', font.lab=3)


# 이산형 데이터와 연속형 데이터
head(cars)
head(Nile)

plot(cars, type='p')
abline(lm(cars$dist~cars$speed), col='red')
str(cars)


plot(cars, type='l')

plot(Nile, type='l')
plot(Nile, type='p')

plot(AirPassengers, type='p')
plot(AirPassengers, type='l')


