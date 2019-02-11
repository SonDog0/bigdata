# 기존 시계열분석의 단점
# 변수변환(log), 차분, 이동평균, 지수평활화등은
# trail and error 방식으로 모형을 찾아야 함
적절한 선택법을 좁은 범위내에서 찾아야 하고
잘 작동하는 좋은 모형인지에 대한 검증이 어려움

=> ARIMA 모형을 이용하면 된다!

ARIMA 모델
Auto Regressive Intergrated Moving Averege

자기회귀와 이동평균모형을 결합한 모델
현 시점의 관측값을 과거 관측값과
오차의 선형결합으로 표현
1970년, Box-Jenkins 모형이 제시되어
지금까지 널리 사용

# 자기회귀 모형
정상시계열의 자기회귀적 표현
즉, 현재의 시계열 값은 과거 시계열값들에 영향을 받음

자기상관 : 연속되는 잔차들이 서로 상관관계를 가짐

예) 가구판매점이 할인판매를 위해 상당금액의 광고비 집행
가구 판매량과 광고비와의 상관관계 예상
=> 과연, 판매량 증가가 이번달에만 발생할까?
=> 아님, 다음n달까지 지속될까?
==> 상관계수가 1/-1 에 가까우면 강한 상관관계를 의미

시계열 자료, 즉, 일정기간에 대한 연속적으로 
조사한 관측치를 회귀분석 기법(1차식)을 이용해서 
분석시 특별한 어려움이 있음
=> 각 잔차는 독립적이어야 하고 
   패턴이 없어야 하며, 상관계과는 최소화해야함
=> 양이나 음의 잔차가 연속적으로 발생하면 안됨

그렇다면, 과거의 패턴이 지속될때
시계열 관측치 데이터Y는
과거 관측치 y1,y2,y3,... 에 의해 예측가능

그럼, 어느정도까지 멀리 있는 과거 관측치까지 
이용해야 하나? - 멀수록 영향력은 줄어듬


   
   
AR(1) 모형의 예
my_par <- par(no.readonly = T)
ar1 <- arima.sim(model = list(ar=0.8), n=1000)
par(mfrow=c(1,2))   # 1행2열
acf(ar1, main='ACF')
pacf(ar1, main='PACF')
par(my_par)


# ACF : 상관계수의 영향력은 지수적으로 감소
# PACF : 부분상관계수의 영향력은 초반에만 반짝(+)

AR(1) 모형의 예
my_par <- par(no.readonly = T)
ar1 <- arima.sim(model = list(ar=-0.8), n=1000)
par(mfrow=c(1,2))   # 1행2열
acf(ar1, main='ACF')
pacf(ar1, main='PACF')
par(my_par)

# ACF : 상관계수의 영향력은 sin 함수적으로 감소
# PACF : 부분상관계수의 영향력은 초반에만 반짝(-)




MR(1) 모형의 예
my_par <- par(no.readonly = T)
ma1 <- arima.sim(model = list(ma=0.8), n=1000)
par(mfrow=c(1,2))   # 1행2열
acf(ma1, main='ACF')
pacf(ma1, main='PACF')
par(my_par)

# ACF : 상관계수의 영향력은 초반에만 반짝 (+)
# PACF : 부분상관계수의 영향력은 sin함수적으로 감소

AR(1) 모형의 예
my_par <- par(no.readonly = T)
ma1 <- arima.sim(model = list(ma=-0.8), n=1000)
par(mfrow=c(1,2))   # 1행2열
acf(ma1, main='ACF')
pacf(ma1, main='PACF')
par(my_par)

# ACF : 상관계수의 영향력은 초반에만 반짝 (+-)
# PACF : 부분상관계수의 영향력은 지수함수적으로 감소



# 이걸 이용해서 초반에만 영향을 받을 수 있게 조절
# 전제조건 : 정상성을 만족시켜 놓고 해야 재대로된 결과를 얻을 수 있음



# AirPassengers 데이터를 ARIMA 모형으로 예측
library(TTR)
library(forecast)

# 소스 데이터를 시계열로 변환
ap <- AirPassengers
plot(ap)

# 시계열 데이터를 분해 - 경향, 계절성, 불규칙 확인
plot(decompose(ap))


# 1. 시계열 데이터를 정상성이 띄도록 전처리
# 시계열 데이터의 계절성 제거 여부 확인

nsdiffs(ap) # 계절성 제거를 위한 차분수
ap1 <- diff(ap, lag=frequency(ap),
            differences = 1)

ndiffs(ap1) # 정상성을 위한 차분 수
ap1 <- diff(ap1, differences = 1)

# ap1 <- diff(log(ap))   # 변수변환, 차분
# ap2 <- diff(ma(ap,5))   # 변수변환, 차분
# ap2 <- diff(SMA(ap))   # 변수변환, 차분
# ma는 결측치땜시 안됨

# 생성된 시계열자료의 정상성 여부 판단
# tseries 패키지 adf.test 함수 사용
# p-value가 0.05 이하면 정상성을 띔
install.packages('tseries')
library(tseries)
adf.test(ap1, alternative='stationary')  # 정상성


# ACF, PACF 함수로 자기상관 지수 확인
my_par <- par(no.readonly = T)
par(mfrow=c(1,2))   # 1행2열
acf(ap1, main='ACF')
pacf(ap1, main='PACF')
par(my_par)

# acf, pacf 함수로 자기상관 최적화지수 확인
# acf : MA 최적화 지수 식별
# pacf : AR 최적화 지수 식별

ARIMA 모형의 AR 차수와 MA차수는
각각 PACF, ACF 그래프를 참고함
=> AR : 0, MA : 1

한편, 최적화 계수를 선택하는 것이
어려운 경우 forecast의 auto.arima 함수를 이용하면
자동으로 산출해줌

# 선택된 최적화 지수로 arima 모형을 생성
# ARIMA(p,d,q) 함수 사용
# p: AR지수, q:MA지수, d: Diff 지수(차분을 몇번 했는가?)
model1 <- arima(ap, order = c(0,2,1))
model2 <- auto.arima(ap)  # 자동 검출


# 생성된 모형을 이용해서 예측값 조사
predicts <- forecast(model1, level = c(95),h=5) # 기간 5
plot(predicts)
predicts

predicts2 <- forecast(model2, h=5) # 기간 5
plot(predicts2)
predicts2



setwd('c:/Java/data')
library(data.table)
# 1대부터 현대 42대까지 
kings <- fread('kings.csv',header=F)
str(kings)

tkings <- ts(kings)
plot(tkings)


# 시계열 데이터 분해
plot(decompose(tkings)) # periods가 없어서 안됨

# 정상성처리
nsdiffs(tkings) # 계절성 x
ndiffs(tkings)  # 차분 적용가능 1회

tkings1 <- diff(tkings,1)
plot(tkings1)   # 분산이 너무 큼

# 정상성 검증
adf.test(tkings1, alternative = 'stationary')

# acf, pacf 함수로 ARIMA 최적화지수 확인
acf(tkings1, main='ACF')    # ma : 1 아닌가...? 2라고 하시네..?
pacf(tkings1, main='PACF')  # AR : 3

# 선택된 최적화 지수로 아리마 모델 생성
model1 <- arima(kings, order = c(3,1,2))
model2 <- auto.arima(kings)  # 자동 검출

model1   # 둘중 aic가 더 작은걸 쓰면됨
model2   #


# 생성된 모형을 이용해서 예측값 조사
predicts <- forecast(model1, level = c(95),h=3)
plot(predicts)
predicts

predicts2 <- forecast(model2, h=3)
plot(predicts2)
predicts2



# 백색 잡음

