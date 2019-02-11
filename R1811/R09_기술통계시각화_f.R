# 여러 개의 그래프를 한 화면에 배치하기

# mfrow=c(행,열) : 행 우선 배치
# mfcol=c(행,열) : 열 우선 배치

# 현재 그래프 설정 저장
.opar <- par(no.readonly = T)

mtcars

par(mfrow=c(2,2))   # 화면분활 2x2
plot(mtcars$mpg)
plot(mtcars$cyl)
plot(mtcars$gear)
plot(mtcars$hp)

par(.opar)             # 그래픽 초기화
par(mfcol=c(2,2))
plot(mtcars$mpg)
plot(mtcars$cyl)
plot(mtcars$gear)
plot(mtcars$hp)

par(.opar)             # 그래픽 초기화
par(mfrow=c(3,1))
plot(mtcars$mpg)
plot(mtcars$cyl)
plot(mtcars$gear)

# 좀더 복잡한 레이아웃
# 지정하고 싶다? - layout
# layout(matrix(영역번호), 행수, 열수)
# layout.show(): 분활된 영역 미리보기

par(.opar)             # 그래픽 초기화

layout(matrix(c(1,1,2,3),2,2, byrow=T))   #2x2
layout.show()
layout.show(2)
layout.show(3)

plot(mtcars$mpg)
plot(mtcars$cyl)
plot(mtcars$gear)





setwd('c:/Java/data')
# 육군 신체측정 정보 데이터 셋 
# 연속형 데이터, 순서척도 데이터
army<-read.csv('kr_army_phy_str.csv',sep=',',header = T,stringsAsFactors = F)
head(army)
tail(army)
str(army)
summary(army)

# 데이터가 모두 문자형이므로 적절한 형변환이 필요
library(stringr)
table(is.na(army)) # 결측치 검사

# army$신장.센티미터 <- as.numeric(army$신장.센티미터)
# 변환한 결과를 다시 army에 저장함
# 하지만 변수명이 길어 불편을 초래
# 파생변수로 재생성

cm <- str_replace_all(army$신장.센티미터,'cm','')
현역신장 <- as.numeric(cm)
summary(현역신장)


kg <- str_replace_all(army$몸무게.킬로그램,' kg','')
현역몸무게 <- as.numeric(kg)
summary(현역몸무게)

str(army$측정.일자)


# 문자추출
substr('asbdfads1234',1,4) # (1~4째 글자 뽑아오기)


# 2016년 대상자 추출
years <- substr(as.character(army$측정.일자),1,4)

h2016 <- army$신장.센티미터[years == '2016']
head(h2016)
tail(h2016)
summary(h2016)

h2016 <- str_replace_all(h2016,'cm','')
h2016 <- as.numeric(h2016)
summary(h2016)

# 153.6 198.4
brk <- seq(150,200,5)
h<-hist(h2016, breaks = brk, col=rainbow(10), ylim = c(0,25000))
h
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))

# 2016년 현역들의 신장 info를 4분기에 놔눠서 출력
setwd('c:/Java/data')
army<-read.csv('kr_army_phy_str.csv',sep=',',header = T,stringsAsFactors = F)

library(stringr)
years <- substr(as.character(army$측정.일자),1,6)
h2016_1 <- army$신장.센티미터[years == '201601' | years == '201602' | years == '201603' ]
h2016_1 <- str_replace_all(h2016_1,'cm','')
h2016_1 <- as.numeric(h2016_1)
summary(h2016_1)


h2016_2 <- army$신장.센티미터[years == '201604' | years == '201605' | years == '201606' ]
h2016_2 <- str_replace_all(h2016_2,'cm','')
h2016_2 <- as.numeric(h2016_2)
summary(h2016_2)


h2016_3 <- army$신장.센티미터[years == '201607' | years == '201608' | years == '201609' ]
h2016_3 <- str_replace_all(h2016_3,'cm','')
h2016_3 <- as.numeric(h2016_3)
summary(h2016_3)

h2016_4 <- army$신장.센티미터[years == '201610' | years == '201611' | years == '201612' ]
h2016_4 <- str_replace_all(h2016_4,'cm','')
h2016_4 <- as.numeric(h2016_4)
summary(h2016_4)





.opar <- par(no.readonly = T)
par(mfrow=c(2,2))

h2016_1
h1 <- hist(h2016_1, breaks = seq(150,200,5), col=rainbow(10), xlim=c(150,200),ylim = c(0,10000))
text(h1$mids, h1$counts, labels = h1$counts, adj=c(0.5,-0.5))

h2<-hist(h2016_2, breaks = seq(150,200,5), col=rainbow(10), ylim = c(0,10000), xlim=c(150,200))
h2
text(h2$mids, h2$counts, labels = h2$counts, adj=c(0.5,-0.5))

h3<-hist(h2016_3, breaks = seq(150,200,5), col=rainbow(10), ylim = c(0,10000), xlim=c(150,200))
h3
text(h3$mids, h3$counts, labels = h3$counts, adj=c(0.5,-0.5))

h4<-hist(h2016_4, breaks = seq(150,200,5), col=rainbow(10), ylim = c(0,10000), xlim=c(150,200))
h4
text(h4$mids, h4$counts, labels = h4$counts, adj=c(0.5,-0.5))


# 화면 분활하는 또다른 방법!
# split.screen() 
# close.screen() 이걸 써서 종료




# 정수로 변환 as.integer
years <- substr(as.character(army$측정.일자),1,6) 
h2016_1 <- str_replace_all(years,'cm','')
h2016_1 <- as.integer(h2016_1)
h2016_1 <- h2016_1[h2016_1 >=  201601 & h2016_1 <= 201603 ]
summary(h2016_1)



# 국방부 병영 표준 식단 정보 데이터 셋
# 범주형 명목
food<-read.csv('kr_army_food.csv',sep=',',header = T,stringsAsFactors = F)
head(food)
str(food)
summary(food)
