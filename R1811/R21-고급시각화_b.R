set.seed(2018111614)
tinydia <- diamonds[sample(nrow(diamonds), 1000),]

gg <- ggplot(tinydia)
gg+geom_point(aes(carat,price, color=cut))

gg <- ggplot(mtcars)
gg + geom_point(aes(wt,mpg, color=as.factor(cyl)))


# 산점도

gg <- ggplot(tinydia)
gg+geom_line(aes(carat,price, color=cut))


# linetype : solid, dotted, dashed, longdash, twodash, dotdash
gg <- ggplot(tinydia)
gg+geom_line(aes(carat,price, color=cut), linetype='dotted')

gg <- ggplot(mtcars, aes(wt, mpg))
gg <- gg + geom_line(linetype='twodash')
gg+geom_point()


# 특정변수를 이용해서
# 그룹형태로 그리기
gg <- ggplot(mtcars, aes(wt, mpg, 
                         group=as.factor(cyl),
                         color=as.factor(cyl)))
gg <- gg + geom_line(aes(linetype=as.factor(cyl)))
gg+geom_point(aes(color=as.factor(cyl)))


# 막대그래프
막대그래프 작성시 stat='identity'를 지정
그래야DF의 데이터들을 자동으로 통계데이터로 생성

df <- data.frame(A=c('a','b','c'),
                 B=c(4.2,10,29.5))
gg <- ggplot(data=df, aes(A,B))
gg + geom_bar(stat='identity')



gg <- ggplot(data=df, aes(A,B))
gg <- gg + geom_bar(stat='identity')
gg +coord_flip() # x/y 축을 전치시킴


gg <- ggplot(data=df, aes(A,B))
gg <- gg + geom_bar(stat='identity', width = 0.5)
gg


gg <- ggplot(data=df, aes(A,B))
gg <- gg + geom_bar(stat='identity', color='blue', fill='white')
gg

gg <- ggplot(data=df, aes(A,B))
gg <- gg + geom_bar(stat='identity', fill='orange')
gg + geom_text(aes(label=B),hjust=0.5,vjust=-0.3, size=5)


gg <- ggplot(data=df, aes(A,B))
gg <- gg + geom_bar(stat='identity', fill='orange')
gg + geom_text(aes(label=B),hjust=0.5,vjust=1.5, size=5)

# 막대그래프 사용자 지정 색상

gg <- ggplot(data=df, aes(A,B, color=A))
gg <- gg + geom_bar(stat='identity', fill='white')
gg + scale_color_manual(values=c('#999999','#E69F00','#56B4E9'))


gg <- ggplot(data=df, aes(A,B, fill=A))
gg <- gg + geom_bar(stat='identity')
gg + scale_fill_manual(values=c('#999999','#E69F00','#56B4E9'))


# RColorBrewer 패키지를 사용
install.packages('RColorBrewer')
library(RColorBrewer)
?RColorBrewer

gg <- ggplot(data=df, aes(A,B, fill=A))
gg <- gg + geom_bar(stat='identity')
gg + scale_fill_brewer(palette='Paired')


# 흑백으로 표시

gg <- ggplot(data=df, aes(A,B, fill=A))
gg <- gg + geom_bar(stat='identity')
gg <- gg + scale_fill_grey()
gg
gg+scale_x_discrete(limits=c('c','b','a'))




# 누적막대 그래프
df <- data.frame(A=rep(c('x','y'), each=3),
                 B=rep(c('a','b','c'),2),
                 C=rep(c(6.8,15,33,4.2,10,29.5)))

df

gg <- ggplot(data=df, aes(B,C,fill=A))
gg + geom_bar(stat = 'identity')


gg <- ggplot(data=df, aes(B,C,fill=A))
gg + geom_bar(stat = 'identity',
              position = position_dodge())

# 누적막대 그래프 레이블 추가
gg <- ggplot(data=df, aes(B,C,fill=A))
gg <- gg + geom_bar(stat = 'identity',
              position = position_dodge())
gg + geom_text(aes(label=C),vjust=1,size=4,
               position = position_dodge(0.8))



# 오차 막대 그래프는 숙제 (오차막대 그래프....?)
표준편차를 미리 계산해 두어야 함
df$sd <- sd(df$C)
df$sd

geom_errorbar()


gg <- ggplot(data=df, aes(B,C,fill=A))
gg <- gg + geom_bar(stat = 'identity',
                    position = position_dodge())
gg + geom_errorbar(
  aes(ymin=C-sd+10, ymax=C+sd-10),
  position = position_dodge(0.8),
  width=0.3
)


# 산점도에 수직선 그리기
# hline, vline, abline

gg <- ggplot(data=mtcars, aes(wt, mpg))
gg <- gg + geom_point()
gg + geom_hline(yintercept = 25,
                color='red', linetype='dotted')


gg <- ggplot(data=mtcars, aes(wt, mpg))
gg <- gg + geom_point()
gg + geom_vline(xintercept = 3.5,
                color='blue', linetype='dashed')


m <- lm(mpg~wt, data=mtcars)
coef(m)[1]
coef(m)[2]


gg <- ggplot(data=mtcars, aes(wt, mpg))
gg <- gg + geom_point()
gg + geom_abline(intercept = coef(m)[1],
                 slope = coef(m)[2],
                color='orange', linetype='dashed')



# 지도공간 시각화
지도공간 기법으로 시각화는 ggmap 패키지는
구글맵, 네이버맵등의 올라인 소스로부터
가져온 정적 지도위에 특별한 데이터나 모형을
시각화하는 함수를 제공

특히, get_googlemap() 함ㅅ를 이용하면
구글에서 지정한 지역의 지도를 내려받아
그래프 형태로 삽입할 수 있게 해줌
네이버맵은 get_navermap() 함수를 사용

install.packages('ggmap')
library(ggmap)

# 지도 위치정보 가져오기

gc <- geocode('seoul')
as.numeric(gc) # deprecate 됨 = google API key 필요

cloud.google.com/maps-platform 회원가입후 구글API 사용권한을 가진 키 발급

AIzaSyBDUyG2U8NR8IFB11fejPUYTGhZ85EZ7u8


# R에서 구글맵 API를 등록해서 맵 관련 질의를 가능하게 해주는 라이브러리
install.packages('devtools')
library(devtools)
devtools::install_github('dkahle/ggmap', ref='tidyup')

# 웹브라우져에서 API 작동여부 확인
http://maps.googleapis.com/maps/api/gecode/json?address=seoul&key=API키

# API 추가
Geocoding API
Maps Elevation API
Maps embed API
Maps Static API
Street View Static API


# 구글맵 API로 지도정보 받아오기
library(ggmap)
register_google(key='AIzaSyBDUyG2U8NR8IFB11fejPUYTGhZ85EZ7u8')

gc <- geocode('seoul')
seoul <- as.numeric(gc)
get_googlemap(center = seoul, zoom = 11)

map <- get_googlemap(center = seoul, zoom = 11)
ggmap(map, extent = 'device')

# 실행할때마다 처음부터 끝까지 다시 해야함 .... 왜해야하냐 이걸

setwd('c:/Java/data')
gu <- read.csv('seoul_lon_lat.txt', sep=' ', stringsAsFactors = F, header = F)


# maptype : terrain, roadmap, satelite, hybrid
gm <- ggmap(map, extent = 'device')
gm + geom_point(data=gu, aes(x=V3, y=V4))

# 서울 자치구별 교통사고 발생건수를 지도그래프를 이용해서 표시

