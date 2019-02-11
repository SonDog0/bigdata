# 데이터 조작
# 실제 데이터 분석 업무에서 
# 모델링이나 시각화에 적합한 형태의
# 데이터를 얻기 위해서는
# 데이터 변환/조작/필터링 등의 전처리 작업이 필요

# apply, plyr, dplyr, sqldf, reshape2 등의 패키지 이용 해 수월히 작업 가능

# plyr : 데이터를 쪼개고, 일부를 취하여 
# 특정 함수를 적용, 집계결과를 제공하는 기능
# 

install.packages('plyr')
library(plyr)

?plyr

# 두개의 데이터 프레임을 하나로 합침
# (rbind, cbind 말고 다른 방식으로)

a <- c(1,2,3,4,5)  # 번호 @1
b <- c(160,171,173,162,165)   # 키 @1

c <- c(5,4,1,3,2)  # 번호 @2
d <- c(55,73,60,57,80) # 몸무게

x <- data.frame(id=a,height=b)
y <- data.frame(id=c,weight=d)

z <- join(x,y, by='id')
z


# 만일, 서로 일치하지 않는 id가 존재한다면?
# left join으로 작동

a <- c(1,2,3,4,6)  # 번호 @1
b <- c(160,171,173,162,180)   # 키 @1

c <- c(5,4,1,3,2)  # 번호 @2
d <- c(55,73,60,57,80) # 몸무게

x <- data.frame(id=a,height=b)
y <- data.frame(id=c,weight=d)

z <- join(x,y,by='id') # 결측치는 NA로 대체
z

# 그럼 서로 일치하는 ID만으로 결합한다면?
z <- join(x,y,type='inner',by='id') 
z

# 그럼 서로 일치하는 id만 결합하고,
# 일치하지 않는 id도 포함시킨다면?
# full join
z <- join(x,y,by='id',type='full')
z


# 만일, 서로 일치하지 않는 id가 존재한다면?
# right join으로 작동
z <- join(x,y,by='id',type='right')
z

# 만일, 서로 일치하는 key가 2개 존재한다면
join(x,y,by=c('id','name'))

# 그룹별 기술통계량 구하기
# 집단변수를 기준으로 그룹단위로 기술통계함수를 적용 - 행렬, 데이터프레임
# apply, tapply, ddply

# apply
# 단순 기술통계 / 사용자 작성 함수를 적용

head(iris[-5])
apply(iris[-5], 1, mean)  # 1은 행, 2는 열
apply(iris[-5], 2, mean)  # 1은 행, 2는 열
apply(iris[-5], 2, mean, na.rm=T) # na를 제거


# tapply : 그룹별 통계 계산 함수
# 하나의 통계함수만 적용

unique(iris$Species) # 붓꽃 품종 확인

tapply(iris$Sepal.Length, iris$Species, mean)

# 붓꽃 품종별 꽃받침 길이 합계 구하기
tapply(iris$Sepal.Length, iris$Species, sum)

# mtcars 에서 실린더 별 평균 연비 구하기
mtcars
tapply(mtcars$mpg, mtcars$cyl, mean)



# ddply : 그룹별 통계 계산 함수
# 여러개의 통계함수만 적용
# ddply(데이터셋, .(그룹변수), 요약집계,변수명=통계함수(변수))
ddply(iris,.(Species), summarise,avg=mean(Sepal.Length))

# 실린더별 평균 연비 구하기
ddply(mtcars,.(cyl), summarise,avg=mean(mpg))




# 함수 만들기 - 최빈값 함수 만들기
getMode = function(v){
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}



# 붓꽃 품종별 꽅받침 길이에 대해
# 평균/최대/최소/중위/최빈 구하기

ddply(iris,.(Species), summarise,avg=mean(Sepal.Length)
      ,max=max(Sepal.Length),min=min(Sepal.Length)
      ,median=max(Sepal.Length),mode=getMode(Sepal.Length))

# 집계요약 함수 : summarise
# 주어진 함수의 결과를 새로운 DF에 생성 후 반환
summarise(iris, means=mean(Sepal.Length))


# 메이저 리거 야구 선수 연간 타격율 데이터
# 1871 ~ 2007
?baseball
head(baseball)
tail(baseball)
str(baseball)

baseball$year[baseball$id=='ansonca01']


# 선수별 첫 출전 년도 계산 : summarise
ddply(baseball, .(id), summarise,
      출전년도=min(year))

# 집계요약 함수 : transform
# 주어진 함수의 결과를 기존 DF에 생성 후 반환
# 선수별 첫 출전 년도 계산
g<-ddply(baseball, .(id), transform,
      출전년도=min(year))
g





# dplyr : 
# plyr의 느린 속도를 개선
# 주로 데이터 프레임을 처리하는 함수군으로 구성
# 데이터 조회/집계/분석에 최적화
# 다루는 방법은 RDBS 와 유사 - 배우기 쉬움
# select, filter, mutate, group by, summarise, arrange

install.packages("ggplot2")

install.packages('dplyr')
library(dplyr)

# dplyr 설치 후 데이터셋을 호출하면
# 자동으로 10행까지 출력해 줌
data(diamonds, package='ggplot2')
head(diamonds)
diamonds

# select - 모두 조회
# ex) carat, price 변수 출력
diamonds[,1]    # DF의 컬럼 인덱스
diamonds[,'carat']    # DF의 변수명
diamonds[,'price']
diamonds[,c(1,7)]

select(diamonds, carat)
select(diamonds, carat, price)
select(diamonds, 1)
select(diamonds, 1,7)

# pipe를 이용한 연산 : %>%
# 이전명령을 실행한 결과를
# 다음 명령의 입력으로 처리
diamonds %>%select(carat, price)

# 변수명을 검색해서 출력
# start_with, end_with, contains, matches
diamonds %>% select(starts_with('c'))
diamonds %>% select(ends_with('e'))
diamonds %>% select(contains('l'))

# 변수명이 r과 t를 포함하는 것만 출력
diamonds %>% select(matches('r.+t'))


# 특정 변수 제외
# ex) carat과 price를 제외
diamonds[,c(-1,-7)]
diamonds%>% select(-carat,-price)

# filter - 조건 검색
# cut 변수 중 'Idal'인 데이터 조회
diamonds %>% filter(cut == 'Ideal')



# price 가  1000이상인 데이터 조회
diamonds %>% filter(price >= 1000)

# carat이 2이상, price가 14000 이하인 데이터 조회
diamonds %>% filter(carat >=2 & price <= 14000)

# carat이 1초과, 5미만인 데이터 조회
diamonds %>% filter(carat >1 & carat<5)

# carat이 1미만이거나, 5초과인 데이터 조회
diamonds %>% filter(carat<1 | carat >5)



# group_by : 집계 함수
# ex) cut 별 평균 가격 조회
diamonds %>% group_by(cut) %>%
  summarise(mean=mean(price))

# 색상별 최대 최소 가격 조회
diamonds %>% group_by(color) %>%
  summarise(max=max(price),min=min(price))

# clarity별 총갯수 조회 - tally()
diamonds %>% group_by(clarity) %>% tally()


# arrange : 조회 후 데이터정렬하기
diamonds %>% select(carat, price) %>% arrange(price)  # 오름차순
diamonds %>% select(carat, price) %>% arrange(desc(price))  # 내림차순
diamonds %>% select(carat, price) %>% arrange(carat, price)  # 내림차순


# mutate - 결과를 기존 DF/새로운 DF에 부착
diamonds %>% mutate(price/carat)

# 새로운 DF에 price/carat 컬럼 추가
diamonds %>% select(carat,price) %>% mutate(price/carat)

# 새로운 DF에 price/carat 컬럼 추가
diamonds %>% select(carat,price) %>% mutate(ratio = price/carat)
diamonds %>% select(carat,price) %>% mutate(ratio = price/carat, double=ratio*2)


# aggregate - 집계 관련 함수
# dplyr의 group by 보다 비교적 단순하게 코드 작성
library('diamonds',package = 'ggplot2')
diamonds

# aggregate( 집계대상, 데이터, 적용함수)
# cut 별 평균  price
aggregate(price ~ cut, diamonds, mean)


# cut 별 평균  carat
aggregate(carat~cut, diamonds, mean)

# cut/color 별 평균  carat
aggregate(carat~ cut+color, diamonds, mean)

# Fruits 데이터셋
install.packages('googleVis')
data(Fruits, package='googleVis')
Fruits

# 년도별 총 판매액
aggregate(Sales~Year, Fruits, sum)

# 과일별 총 판매액
aggregate(Sales~Fruit, Fruits, sum)

# 과일별 최대 판매액
aggregate(Sales~Fruit, Fruits, max)

# 과일/년도 별 최대 판매액
aggregate(Sales~Fruit+Year, Fruits, max)

# 연도별 이익 합계
aggregate(Profit~Year+Fruit, Fruits, sum)


# sqldf : RDBMS에서 사용하는 SQL 문으로
# 데이터 조작을 가능하게 해주는 패키지
install.packages('sqldf')
library(sqldf)
data(Fruits, package='googleVis')
data(diamonds, package='ggplot2')

# 과일, 년도, 매출, 이익 조회
sqldf('select Fruit, Year, Sales,Profit from Fruits')

# Apple 에 대한 모든 정보 조회
sqldf('select * from Fruits where Fruit="Apples"')

# 매출액 순으로 오름차순 정렬 출력
sqldf('select * from Fruits order by Sales desc')



# 년도별 총 판매액
sqldf('select Year,sum(Sales) sales from Fruits group by Year')

# 과일별 총 판매액
sqldf('select Fruit, sum(Sales) from Fruits group by Fruit')

# 과일별 최대 판매액
sqldf('select Fruit, max(Sales) from Fruits group by Fruit')

# 과일/년도 별 최대 판매액
sqldf('select Fruit, Year, max(Sales) from Fruits group by Fruit,Year')

# 연도별 이익 합계
sqldf('select Year, sum(Profit) from Fruits group by Year')

# hr 데이터셋에서 employees, department 등을 join 해서 사원 이름과 부서명 조회
setwd('c:/Java/data')
emp <- read.csv('employees.csv',header=T, stringsAsFactors = F)
dep <- read.csv('DEPARTMENTS.csv',header=T, stringsAsFactors = F)

sqldf('select e.FIRST_NAME, d.DEPARTMENT_NAME 
      from emp e join dep d using(DEPARTMENT_ID)')
