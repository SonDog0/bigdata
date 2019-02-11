# reshape2 : 데이터 구조를 wide/long 형식 변형
# 데이터 분석시 DF/matrix를 wide 형식인 상태에서
# 실행하는 경우가 있고, 상황에 따라 long형식인 상태에서
# 실행되는 경우도 존재
# 엑셀의 피벗테이블과 유사한 형태로 분석 실시


library(reshape2)
airquality # 공기질측정데이터
head(airquality)
table(is.na(airquality))

# 월별 각 평균 측정값 조사
#  wide 형식-> long 형식

# 기준없이 melt실행
# melt시 value 열은 반드시 숫자로만 구성되도록 함
head(melt(airquality))
tail(melt(airquality))


# 월과 일을 기준으로 melt 실행
newOne <- melt(airquality, id=c('Month', 'Day'))
newOne

# melt 한 결과의 열이름 변경
melt(airquality, id= c('Month', 'Day'), variable.name = 'climate_var', value.name = 'climate_var')

# ChickWeight 데이터셋
# id는 time, chick, diet로melt하세요

head(ChickWeight)
newOne<-melt(ChickWeight, id = c('Time','Chick','Diet'))

# melt 한 결과를 원래대로 되돌리거나
# 집계계산을 위한 구조로 변형하려면
# cast, dcast(DF형태), acast(벡터나 행렬)를 사용

#head(dcast(newOne, Month+Day~...))
#head(dcast(newOne, Month+Day~variable))

# ChickWeight 데이터셋
# melt한 데이터를 원래대로 만드세요
dcast(newOne, Time+Chick+Diet~...)


# dcast를 단순히 데이터 구조를 재구성 하는 것만으로
# 사용할 것이 아니고 집계함수를 적용시킬 수 도 있음

# dcast(newOne, Month~...)
# 일 컬럼과 나머지 측정값컬럼이 합쳐져 보임
# 월 별 각 평균 측정 값을 출력
dcast(newOne, Month~variable, mean)
dcast(newOne, Month~variable, mean, na.rm=T) # 결측값제외

# 월 별 각 평균 측정 값을 출력
# 일 컬럼은 제외함

# ChickWeight 데이터셋
ChickWeight
# Time 별 평균 weight
dcast(newOne, Time~variable, mean)
# Diet 별 평균 weight
dcast(newOne, Diet~variable, mean)

# mtcars 데이터셋
head(mtcars) # wide 형식
# 행번호 자리에 차종이 표시됨
# 차종 컬럼을 따로 생성해야 함

rownames(mtcars) # 행번호(이름) 모두 표시
mtcars$car <- rownames(mtcars)

# 차종, cyl, gear, am
# 차종, 실린더수, 기어수, 수동여부로 melt 실행
newOne <- melt(mtcars, id = c('car','cyl', 'gear','am'))
head(newOne)

# 실린더수 별 평균 연비
dcast(newOne, cyl~variable, mean)[,1:2]

# 실린더수 별 기어별 평균 연비
dcast(newOne, car+cyl+gear~variable, mean)[,1:3]
# 실린더수 별 기어별 수동 여부 별 평균연비
dcast(newOne, cyl+gear+am~variable, mean)[,1:4]





# applewood 데이터셋
setwd('c:/Java/data')
aw <- read.csv('applewood.txt',sep = ' ', header = T, stringsAsFactors = T)
summary(aw)

# profit 컬럼이 문자형이므로
# 전처리를 통해 숫자형으로 변환
library(stringr)
aw$Profit <- str_remove_all(aw$Profit, '\\$')
aw$Profit <- str_remove_all(aw$Profit, ',')
aw$Profit <- as.numeric(aw$Profit)

summary(aw)

meltOne <- melt(aw, id=c('Location','Vehicle.Type'))
head(meltOne)
tail(meltOne)

# 지역별 평균이익
dcast(meltOne, Location~variable, mean)
dcast(meltOne, Location~variable, mean)[,c(1,3)]


# 차종별 평균이익
dcast(meltOne, Vehicle.Type~variable, mean)
dcast(meltOne, Vehicle.Type~variable, mean)[,c(1,3)]





# HR의 EMPLOYEES 데이터셋
emp <- read.csv('c:/Java/data/hr/EMPLOYEES.csv', header = T, sep = ',', stringsAsFactors = F )

#melt를 용이하게 컬럼 선별 
newemp <- emp[,c(6,7,8,11)]

# 입사년도 컬럼 생성
# 기존 입사년월일 제거
newemp$YEAR <- substr(newemp$HIRE_DATE,1,4)
newemp <- newemp[,-1]

str(newemp)



meltOne <- melt(newemp, id=c('JOB_ID','DEPARTMENT_ID','YEAR'))

head(meltOne)


# 직급별 평균연봉
dcast(meltOne, JOB_ID~variable, mean)
dcast(meltOne, JOB_ID~variable, min)
dcast(meltOne, JOB_ID~variable, max)
dcast(meltOne, JOB_ID~variable, num)
dcast(meltOne, JOB_ID~variable, length)  # 사원수


# 부서별 평균연봉
dcast(meltOne, DEPARTMENT_ID~variable, mean)
dcast(meltOne, DEPARTMENT_ID~variable, length)  # 사원수

# 연도별 평균연봉
dcast(meltOne, YEAR~variable, mean)
dcast(meltOne, YEAR~variable, length)   # 사원수


 



