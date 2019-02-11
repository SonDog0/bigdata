# 중회귀분석

ex) 난방비 가이드라인 작성을 위해 20개 주택에대해 중회귀 분석
setwd('c:/Java/data')
house <-read.csv('houses.txt',header = T, sep='\t', stringsAsFactors = F)

str(house)

house
m <- with(house, lm(난방비~평균외부기온+단열재+난방사용연수))

summary(m)  # 난방사용연수는 유의확률이 0.148임 => 사용하면 안됨

coef(m)

y= 427.19 - 4.5827평균외부기온 - 14.831단열재 + 6.101난방사용연수

lm(house$난방비)

427.19 - 4.5827*30 - 14.831*5 + 6.101*10

ex) 놀이동산 만족도 데이터셋을 이용
놀이기구, 게임만족도, 청결만족도, 전체만족도에 대한 관계 분석
park <- read.csv('parks.csv', stringsAsFactors = F,header=T)
str(park)
model <- with(park, lm(overall~rides+games+clean))
summary(model)
coef(model)

y = -131.68 + 0.578*놀이기구+0.26*게임+1.284*청결도


# 다중회귀식 평가
다중회귀식의 통계적 분석은 회귀모형과 잔차를 이용

m <- with(house, lm(난방비~평균외부기온+단열재+난방사용연수))
m2 <- with(house, lm(난방비~평균외부기온+단열재))
m3 <- with(house, lm(난방비~평균외부기온+난방사용연수))
m4 <- with(house, lm(난방비~단열재+난방사용연수))

summary(m)  # 0.7675
summary(m2) # 0.7495
summary(m3) # 0.648
summary(m4) # 0.2995

coef(m2)

y= 490.285 - 5.1499평균외부기온 - 14.718단열재

lm(house$난방비)

35 3 6 기준으로 했을때 259 예측 but 실값 250 
따라서 오차는 9 : 다른 관측치에 대해 오차 계산

=> 추정치의 다중표준오차는
잔차평균제곱MSE의 제곱근 = 평균제곱오차

# 결정계수
독립변수등이 난방비 변동의 설명정도를 판단 가능케 하는 수치

# 수정결정계수
독립변수가 증가하면 결정계수가 무조건적으로 상승
=> 의미없는 변수들에 의해서도 결정계수가 상승하므로
이를 상쇄시키기 위해 사용

# 다중선형회귀 추론
F-statistic
다중회귀분석에서는 종속변수와 독립변수n개의
연관을 보여주는 미지의 모회귀식이 있다고 가정
이것을 관계의 모형이라고 부름

만일 독립변수가 없어도 종속변수를 추정할 수 있을까?
  
즉, 다중회귀계수가 모두 0 인지 검정하자 -F분포 이용
귀무가설 : 각 계수가 abc가 0이다
대립 : 각계수 abc가 모두0은 아니다

F분포의 측징
자유도에 의해 분포의 모양이 바뀜
연속분포, 양의 방향으로 치우친 분포, 점금적 구조


# 개별 회귀계수에 대한 평가
summary(m)

분자 : k-1
분모 : n-k-1


# 의학정보 데이터를 참고해서
심박수BMP에 영향을 주는 요인 
bmp 몸무게
bmp 몸무게 강제호기량 잔기량
setwd('c:/Java/data')
m <- read.csv('medical.csv', header=T, stringsAsFactors = F)
str(m)

model <- with(m, lm(BMP~weight))
model
summary(model)

model2 <- with(m, lm(BMP~weight+FEV+RV))
model2
summary(model2)

# 상호작용항 x1 * x2
회귀분석에서 상호작용은 별도의 독립변수를 통해 만들어 낼 수 있음
str(house)

model <- with(house, lm(난방비~평균외부기온+단열재+평균외부기온*단열재))
coef(model)
summary(model)

평균외부기온*단열재 회귀계수는 상호작용항으로써 기능을 하지 못함

# Orange 데이터셋을 이용
나무의 수명에 따라 나무의 둘레에 영향을 주는지
상호작용항 : 나무둘레와 나이

data(Orange)
summary(Orange)
head(Orange)

model1 <- with(Orange, lm(circumference~ Tree+age))
model2 <- with(Orange, lm(circumference~ Tree+age+Tree*age))
summary(model1)
summary(model2)

Orange$Tree <- factor(Orange$Tree, ordered = F)
=> 순서없는 범주형 변수로 변환


# mtcars 데이터셋을 이용해서
mpg~ wt hp
data(mtcars)
summary(mtcars)
m<-with(mtcars, lm(mpg~wt+hp+wt*hp))
summary(m)



# 다중공선성
VIF가 10 이상이면 제외
VIF : 1/1-결정계수


ex) 다중공선성 문제 풀기
시멘트가 굳어지며 발생하는 열의 양을 결정짖는 4가지
x1 <- c(7, 1, 11, 11, 7, 11, 3, 1, 2, 21, 1, 11, 10)
x2 <- c(26, 29, 56, 31, 52, 55, 71, 31, 54, 47, 40, 66, 68)
x3 <- c(6, 15, 8, 8, 6, 9, 17, 22, 18, 4, 23, 9, 8)
x4 <- c(60, 52, 20, 47, 33, 22, 6, 44, 22, 26, 34, 12, 12)

y <- c(78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7, 
       72.5, 93.1, 115.9, 83.8, 113.3, 109.4)

cm <- data.frame(y,x1,x2,x3,x4)
cm
plot(cm)

# 상호작용항 고려 x
m <- with(cm, lm(y~x1+x2+x3+x4))
m <- lm(y~., data = cm)  # 독립변수를 .으로 줄여씀
m

summary(m)




VIF 구하기
car 패키지의 vif 함수를 이용
각변수간의 다중공선성을 검사
install.packages('car')
library(car)

vif(m)
m1 <- lm(y~x1+x2, data = cm)
m2 <- lm(y~x1+x4, data = cm)
m3 <- lm(y~x3+x4, data = cm)

summary(m1) # 0.9744 0.9787
summary(m2) # 0.967
summary(m3) # 0.9223


# 독립변수 최적화
step(lm모델, 변수범위, 소거종류)



전진소거법 : 중요도 (R^2)가 높은 변수부터 추가
후진소거법 : p값이 높은 변수부터 제거
최적선택법/단계별선택법 : 

  
  
EX) 부동산 주택 난방비 예측
전진/후진제거법 사용


후진 소거법
step(lm(난방비~.,data=house), direction = 'backward')


전진 소거법 : 절편부터 시작
step(lm(난방비~1, data=house), 
     scope=list(lower=~1, upper=~평균외부기온+단열재+난방사용연수),
     direction = 'forward')


단계소거법
step(lm(난방비~1, data=house), 
     scope=list(lower=~1, upper=~평균외부기온+단열재+난방사용연수),
     direction = 'both')




AIC :  종속변수의 실제 분포와 모형에 의해 
        예측된 분포사이의 불일치 측정값
        낮을수록 좋은 모형을 의미함

RSS : 오차의 분산정도를 나타내는 값



library(MASS)
str(Boston)

상관행렬
plot(Boston)

회귀분석
m <- lm(medv~.,data = Boston)

options(scipen = 100)
summary(m)


m <- lm(medv~crim+zn+chas+nox+rm+dis+rad+tax+ptratio+black+lstat, data = Boston)
summary(m)

m <- lm(medv~crim+zn+nox+rm+dis+rad+tax+ptratio+black+lstat, data = Boston)
summary(m)


# 다중공선성 확인
library(car)
vif(m)


# 변수소거를 위한 또 다른 방법 1
install.packages('leaps')
library(leaps)

m <- regsubsets(medv~.,data=Boston)
summary(m)

m <- regsubsets(medv~.,data=Boston, method = 'forward')  # 전진
m <- regsubsets(medv~.,data=Boston, method = 'backward') # 후진
m <- regsubsets(medv~.,data=Boston, method = 'seqrep')  # 단계소거
m <- regsubsets(medv~.,data=Boston, method = 'exhaustive') # 첫번째를 우선시
summary(m)

summary(m)$bic  # 회귀모델 측정값
summary(m)$adjr2

plot(m,scale = 'bic')
plot(m,scale = 'adjr2')



setwd('c:/Java/data')
b<-read.csv('banks.txt', sep='\t', header = T, stringsAsFactors = F)
b

library('corrplot')

m <- lm(Income~.,data = b)
summary(m)

corb <- cor(b)
corrplot(corb, method = 'number')

# 독립변수 소거
m <- lm(Income~.-Mortgage,data = b)
summary(m)

vif(m)


# 잔차의 정규분포 확인
plot(m)
1) 잔차그래프 : 정규성
-> 독립변수가 정규본포를 띄면 
잔차도 정규분포를 띄는가?
* 숫자가 붙어있는 얘들은 이상치

library(lattice)

hist(rstandard(m)) # 잔차 히스토그램으로 정규성 확인

2) 잔차 확률분포도 : 독립성
누적 정규확률분포표
점선 : 표준누적 정규분포

3) 잔차예측비교도 : 선형성


4) 잔차 분산비교도 : 등분산성
독립변수의 분산이 일정하면
잔차도 비슷한 양상을 띄는가?

# cook's distance
회귀방정식 계수 결정에
불균형한 영향을 미치는
독립변수 존재 여부



따라서, 산출된 회귀방정식은
가계소득변수의 변동성을 70정도 설명
기본 4가지 가정에 문제 없음

ex) 미술품 수집가 그림낙찰가격과

art <- read.csv('artsbuyer.txt',sep='\t',header = T, stringsAsFactors = F)
art <- art[,-1]
summary(art)
art

m <- lm(Price~., data = art)
summary(m)
plot(m)
m

art_cor <- cor(art[,-1])
corrplot(art_cor, method = 'number')

vif(m)

# 잔차의 정규분포, 공분산성, 성형성 확인
.opar <- par(no.readonly = F)
par(mfrow=c(2,2))
plot(m)



par(.opar)

library(lattice)
hist(rstandard(m))




car<-read.csv('carparts.txt',sep='\t',header = T, stringsAsFactors = F)
library(stringr)
car$outlet <- str_remove_all(car$outlet,',')
car$outlet <- as.integer(car$outlet)

plot(car)
cor_car <- cor(car)
corrplot(cor_car, method='number')

m<-lm(sales~.,data=car)
summary(m)

m<-lm(sales~.-manager,data=car)
summary(m)

m<-lm(sales~.-manager-outlet,data=car)
summary(m)

m<-lm(sales~.-manager-outlet-year,data=car)
summary(m)

.opar <- par(no.readonly = F)
par(mfrow=c(2,2))
plot(m)

par(.opar)

library(lattice)
hist(rstandard(m))





ex)공매를 통해 차압된 주택을 전문적으로 판매하는 회사에서 
주택대출잔고, 월납입액, 납입회차 대비 최종 경매가에 대한 회귀분석 실시
au <- read.csv('auctions.txt',sep='\t', stringsAsFactors = F)
summary(au)
plot(au)

cor_au <- cor(au)
corrplot(cor_au, method = 'number')
m<-lm(Auction~.,data = au)
vif(m)
summary(m)

m<-lm(Auction~.-Payments,data = au)
summary(m)

m<-lm(Auction~Loan,data = au)
summary(m)



.opar <- par(no.readonly = F)
par(mfrow=c(2,2))
plot(m)

par(.opar)
hist(rstandard(m))

ex) 주택보수재료취급 회사
매출액, 광고비, 거래첫, 경쟁브랜드수, 잠재력
