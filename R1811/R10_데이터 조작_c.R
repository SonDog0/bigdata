# reshape : 데이터셋의 구조를 변형하는 함수
# 주로 DF, matrix의 모양을 다른 형태로 바꿈
# 
install.packages('reshape')
library(reshape)

# a <- c(1,2,3,4,5,6,7,8,9,10)
# b <- reshape(a, [2,5])
# b => 12345
#      678910

# wide data를 long data로 변환
# c <-  1,2,3,4,5 
#      6,7,8,9,10
# d <- reshape(a, [5,2])
# d => 1,2
#      3,4
#      5,6
#      7,8
#      9,10


install.packages('reshape2')
library(reshape2)

?french_fries
?smiths

# melt, cast 함수 : data 구조 변형함수
str(french_fries)   # 9개 변수

head(french_fries)   # wide 형식으로 출력
(french_fries)
head(melt(id=1:2, french_fries))



data(Fruits, package = 'googleVis')
Fruits   # 7개의 변수로 구성된 DF (wide)

mfruits <- melt(id='Year', Fruits)   # 3개의 변수로 구성된 DF (long)
mfruits[c(1:9),]  # 재구성된 DF에 접근하기

# smiths 데이터셋
# subject, time 변수를 기준으로 재구성
str(smiths)


newOne <- melt(id=c('subject','time'), smiths)
newOne <- melt(id=c(1:2), smiths)
newOne <- melt(id=1:2, smiths)
newOne




# airquality
# month, day
str(airquality)
new1 <- melt(id=c('Month','Day'), airquality)
new1


# melt 된 데이터를 원래대로 돌려놓기
ori <- dcast(newOne, subject+time~...)
ori

# 부분 복귀
orip <- dcast(newOne, subject~...)
orip


# 총정리
no <- c(1,1,2,2)
day <- c(1,2,1,2)
kor <- c(40,30,50,25)
mat <- c(70,55,80,45)
ex <- data.frame(no,day,kor,mat)
ex

meltOne <- melt(id=c(no,day), ex)
meltOne
dcast(meltOne, no+day~...)



# Cars93 : 차종별 시내/고속도로 연비 데이터
library(MASS)
str(Cars93)

library(dplyr)
# dplyr 사용
# Type, Origin, MPG.city, MPG.highway
# Type 은 'Compact','Van'
newCar93 <- Cars93 %>% select(Type, Origin, MPG.city, MPG.highway)%>% filter(Type %in% c('Compact', 'Van'))
head(newCar93)

# 자동차 종류별로 시내/ 고속도로 평균연비
meltOne <- melt(id='Type', newCar93)
head(meltOne) 
# 자동차 종류별, 시내/ 고속도로 평균연비
# + 측정장소(Origin) : 올바른 DF 작성 실패
# 즉, value 컬럼에 숫자/ 문자 혼재



dcast(meltOne, Type~..., mean)   # 실패
dcast(meltOne, Type~...)

# 따라서, Type, Origin을 기준으로 다시 melt
newOne <- melt(id=c('Type','Origin'), newCar93)
newOne


dcast(newOne , Type~..., mean )  # 차종별 평균 연비
dcast(newOne , Type~variable, mean )  # 차종별 평균 연비


dcast(newOne , Origin~..., mean )  # 측정지역별 평균 연비
dcast(newOne , Origin~variable, mean )  # 측정지역별 평균 연비


# 자동차 종류별, 측정 지역별 
dcast(newOne , Type+Origin~variable, mean )
