# 기술적 통계
# 통계에서 사용하는 데이터 유형
# 이산형
# 연속형

# 통계학 종류
# 기술통계 - 자료를 중심으로 통계수치, 표, 
#            그래프등을 이용해서 집단의 특성 파악(위치, 경향, 분포)
# 추론통계 - 표본을 이용해 모집단 특성 파악  
#모수통계(모집단 분포 가정)
#빈도분석 : 변수의 분포와 중심치 파악
#상관분석 : 연속형 변수간의 관계 파악, 상관계수로 표현
#표본평균분석 : 두집간 간의 평균 비교
#3집단이상 편균분석 : 세집단 간의 평균 비교
#회귀분석 : 변수간의 인과관계 분석 및 예측 



#비모수 통계(모집단 분포 불분명)
# 적합도 점정 : 카이스퀘어 ks점증, 이항분포
# 변수간 상관분석 : 스피어만 순위 상관분석



# 기술통계
# 위치척도를 이용한 기술통계
# 평균
weight <- c(72,67,60,78,82)
mean(weight)

# 1. 단순랜덤 : 모집단 개체에 번호부여, 원하는 갯수 만큼 추첨하여 뽑기
# 2. 계통추출 : k번째
# 3. 층화추출 : 층간이질절, 층내동질적  
# 4. 군집추출 : 층간동질적, 층내이질적 

# 표본추출 : sample
# 복원추출 : 중복가능
sample(1:100,5, replace = T)
# 비복원 추출 : 
sample(1:100,5)


# 층화추출 : strata
# 계통추출 : sampleBy

# 산술평균 : 모집단이 정규분포일때 중심화 경향 통계값
# 가중편균 :weighted.mean
# 관측값에 가중치를 적용해 평균 구함
sales <- c(95,72,87,65)
weights <- c(0.5,0.25,0.125,0.125)

mean(sales)
weighted.mean(sales,weights)


# 도수를 이용한 가중평균
kor.A <- c(4.0,3.0)
kor.B <- c(3.0,4.0)
counts <- c(3,2)  # 도수

weight <- counts/sum(counts)
weight
weighted.mean(kor.A, weight)
weighted.mean(kor.B, weight)

# 도수를 이용한 가중평균
score <- c(90,80,75,60)
counts <- c(3,12,15,5)

weight <- counts/sum(counts)

weighted.mean(score, weight)



# 1~100사이 7개 표본 추출, 평균
mean(sample(1:100,7,replace = T))
mean(sample(1:100,7))




# 건설회사는 시간제 근로자에게 시간당
# 16.50, 19.00 ,25.00의 임금을 지급한다
# 총 26명의 근로자중 14명은 16.50
# 10명은 19.00, 2명은 25.00
# 평균근로자의 시간당 평균 임금은 얼마인가?

wage <- c(16.50,19.00,25.00)
counts <- c(14,10,2)

weight <- counts/sum(counts)


sum(wage* counts/sum(counts))
weighted.mean(wage, counts)




# 중앙값 : median
data <- c(7,7,2,3,7,6,9,10,8,9,1000)
mean(data)
median(data)


# 최빈값 : 
data <- c(1,2,2,3,4,3,5,5,7,2,2,0)
table(data)
freq <- table(data)   # 빈도표
freq    
max(freq)

idx <- which.max(freq) # max값 index
idx   # 2,3 (실제값, 위치값)
names(freq)[idx]




# 산포

#  ex) 호수의 수심 평균 3미터
# 범위 : 데이터 최대/최소 차이
range(data)

# 분산 : 표본분산을 구해짐
weight <- c(72,67,60,78,82)
mean(weight)
median(weight)
var(weight)

# 어떤 두 지점의 5일동안 오후 4~5 사이의
# 카푸치노 판매량
a <- c(20,40,50,60,80)
b <- c(20,45,50,55,80)
var(a)
var(b)





# 타이타닉 데이터셋
# 탑승객의 나이에 대한 기술통계량 조사
setwd('c:/Java/data')
tit<-read.csv('titanic.csv', header = T, stringsAsFactors = F)
str(tit)
Age<-tit$Age[!is.na(tit$Age)]  # ... 이렇게 할필요가 없었눼
Age

# 생존 탑승객의 평균 나이는?
mean(tit$Age, na.rm = T)
mean(Age)

mean(tit$Age[tit$Survived == 1], na.rm = T)


# 생존 탑승객의 가중 평균 나이는?
head(tit$Age)
weights <- tit$Survived/sum(tit$Survived)
weighted.mean(tit$Age, weights, na.rm=T)


weighted.mean(tit$Age, tit$Survived, na.rm = T)



# 승선등급 중 가장 많은 수를 차지하는 것은?
nrow(tit[tit$Pclass == 1,])
nrow(tit[tit$Pclass == 2,])
nrow(tit[tit$Pclass == 3,])


freq <- table(tit$Pclass)
freq
idx<-which.max(freq)
names(freq)[idx]

# 비생존 탑승객의 최소/최대 나이
library('sqldf')
sqldf('select max(Age), min(Age) from tit where Survived == 0' )

dead <- tit$Age[tit$Survived == 0]
dead <- dead[!is.na(dead)]
min(dead, na.rm=T)
max(dead, na.rm=T)


# 운임의 범위
fare <- tit$Fare[!is.na(tit$Fare)]
fare
range(tit$Fare)


# 표준편차
# 1년동안 발부된 모든 벌칙금 통지서 조사
# 19 17 22 18 28 34 45 39 38 44 34 10

a <- c(19, 17, 22, 18, 28, 34, 45, 39, 38, 44, 34, 10)
var(a)
sd(a)


# 회계 수습 사원들의 월급
# 3536,3173,3448,3121,3622
# 사무수숩사원 mean = 3550, sd = 250
b <- c(3536,3173,3448,3121,3622)
mean(b)
sd(b)


# 체비셰프 정리
# p(|X-m| < k*s) >= 1-1/(k^2)
# p(|X-m| > k*s) <= 1/(k^2)





# 정규분포일시 90% => 1.645
#              95% => 1.96
#              99% => 2.58


# 평균 x 표편s 일때 
1 - 1/(3.5^2)


# 데이터 위치
# 분위수
# 4분위수
x <- c(136,182,166,132,130,186,140,155)
quantile(x, 0.25)
quantile(x, 0.5)
quantile(x, 0.75)
quantile(x, 0.8)
quantile(x, 1)
quantile(x)
summary(x)


# 사무실 수수료 내역
# 2038,1758,1721,1637,2097,2047
# 2205,1787,2287,1940,2311,2054
# 2406,1471,1460

c <- c(2038,1758,1721,1637,2097,2047,2205,1787,2287,1940,2311,2054,2406,1471,1460)
quantile(c)
median(c)
boxplot(c)
mean(c)


# 타이타닉 데이터셋
# 탑승객의 나이에 대한 기술통계량 조사

# 나이의 사분위수
quantile(tit$Age, na.rm=T)
# 운임의 사분위수
quantile(tit$Fare, na.rm=T)

# 주당 이익자료
d<-c(0.09,0.13,0.41,0.51,1.12,1.20,1.49,3.18,3.50,6.36,7.83,8.92,10.13,12.99,16.40)
mean(d)
quantile(d)
sd(d)
boxplot(d)
library(fBasics)
skewness(d)   # 왜도
kurtosis(d)   # 첨도
?kurtosis

