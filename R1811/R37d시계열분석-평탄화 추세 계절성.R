# 시계열 분석 -평활법
# 과거 자료의 형태를 분석해 미래를 예측
# 이동평균, 지수평활 

# 이동평균 Moving average
# '내일의 수치는 최근 며칠간 수치의 평균이다'
# 시계열의 추세를 파악하기 위해 시계열을 
# 평활하게 만드는 유용한 기법
# 계절 변동을 측정하는데에도 활용 

# 시계열에 이동평균을 적용하기 위해서는
# 시계열자료에 선형추세가 있어야 하고 
# 주기적변동(n년마다반복)도 있어야 함
# 추세 / 순환 / 불규칙 => 순환 / 계절 / 불규칙 특성 제거

#forecast 패키지의 ma 함수 이용
# 가장 최근에 얻어진 n개의 관찰값의 단순평균 계산 


# 매출액 데이터 (1991~2016, 단위 백만)
sales <- c(1,2,3,4,5,4,3,2,3,4,5,6,5,4,3,4,5,6,7,6,5,4,5,6,7,8)
plot(sales,type = 'l')

# 이동평균 계산 (구간 : 7)
# 1,2,3,4,5,4,3 => 22 => 3.1
# 2,3,4,5,4,3,2 => 23 => 3.2
# ...
# 6,5,4,5,6,7,8 => 41 => 5.8

# 매출엑 데이터를 시계열자료로 생성
tsales <- ts(sales, start = 1991)
tsales

# 매출액 시계열자료에 이동평균 적용
library(forecast)
mtsales <- ma(tsales , 5)

plot(tsales,type='l')
points(mtsales,col='red',type ='l')

# 생산량 (1998~2016, 단위 : 만)
prod <- c (5,6,7,10,5,3,7,10,12,11,9,13,15,18,15,11,14,17,22)
tprod <- ts(prod , start = 1998)
mtprod <- ma(tprod , 3)

plot(tprod,type='l')
points(mtprod,col='red',type='l')

# 매출액(2008~2016, 단위 : 백만)
sales2 <- c(8,11,9,14,9,10,10,8,12)
tsales2 <- ts(sales2,start=2008)
mtsales2 <- ma(tsales2,3)

plot(tsales2,type = 'l')
points(mtsales2,col='red',type ='l')

# 나일강 연간 흐름 자료에 MA 적용 (1871~1970)
plot(Nile)

# MA 3,5,7
nile3 <-ma(Nile,3)
nile5 <-ma(Nile,5)
nile7 <-ma(Nile,7)
nile9 <-ma(Nile,9)

points(nile3 , type = 'l' , col = 'red')
points(nile5 , type = 'l' , col = 'green')
points(nile7 , type = 'l' , col = 'blue')
points(nile9 , type = 'l' , col = 'orange')


# 지수평활법 
# 예측할 자료와 가까운 시점의 실제 자료에
# 가중치를 부여하고, 과거로 갈수록 지수적으로
# 가중치를 줄여나가면서 예측하는 기법 

# 단순지수 : 추세나 계절성없이 평균이 완만하게 변화하는 시계열에 적용 ( 알파)
# 이중지수 : 데이터에 추세가 존재할 때(Hlot: 알파/베타)
# 삼중지수 : 데이터에 계절성이 존재할 때(Winters : 알파/베타/감마)

# TTR 패키지의 HoltWinters() 사용
# 지수평활법에 의해 예측값을 알아보려면
# predict 함수를 사용 
install.packages('TTR')
library(TTR)

# 단순지수 평활법
# 사용자 월평균 스마트폰 사용시간 자료(2012)
phone <- c(296,367,365,367,401,370,281,313,373,352,377,356,320,409,321,397,320,317,306,313,324)
tphone <- ts(phone,start=2012,frequency = 12)
plot(tphone) # 추세, 계절성(반복) 없음 

etphone<-HoltWinters(tphone ,alpha =0.5 ,beta = F ,gamma = F)
# 알파, 베타, 감마 : 평활계수
# 단순지수 평활은 알파 계수만 사용 
# 계수값이 1에 가까우면 오차가 커지는 예측값 산출 
plot(etphone)
etphone
predict(etphone,n.ahead = 7, prediction.interval = T) #예측하기


# 이중지수 평활법
etphone<-HoltWinters(tphone ,alpha =0.5 ,beta = 0.1 ,gamma = F)
# 이중지수평활은 알파 베타 계수만 사용 
# 오차를 최소로 하는 모수 알파 베타를 
# 찾는다는 것은 다소 어려움
# R에서 자동으로 모수를 찾아주는 기능 제공
plot(etphone)
etphone
predict(etphone,n.ahead = 7, prediction.interval = T) #예측하기
plot(HoltWinters(etphone)) # 자동 모수 찾기 기능 적용 (안됨..)


# 삼중지수 평활법
# 월별 수출입 데이터 (2012)
exp <- c (362,385,432,341,382,409,498,387,473,513,582,474,544,582,681,557,628,707,773,592,627,725,854,661)
texp <- ts(exp,start = 2012 ,frequency = 12)
etexp <-HoltWinters(texp,alpha = 0.5,beta = 0.1,gamma = 0.05)
plot(etexp)
etexp
predict(etexp,n.ahead = 7, prediction.interval = T) #예측하기

plot(HoltWinters(texp))

# 단순지수 : 추세나 계절성없이 평균이 완만하게 변화하는 시계열에 적용 ( 알파)
# 이중지수 : 데이터에 추세가 존재할 때(Hlot: 알파/베타)
# 삼중지수 : 데이터에 계절성이 존재할 때(Winters : 알파/베타/감마)

# 1995 ~ 2016, 이승엽 홈런수 자료
homerun <-c(13,9,32,38,54,36,39,47,56,14,30,41,30,8,16,5,15,21,13,32,26,27)
thr <- ts(homerun, start=1995)
plot(thr)  # 단순지수평활 -> 자동기능x

thr5 <- HoltWinters(thr, alpha = 0.5,
                    beta=F,gamma=F)

thr3 <- HoltWinters(thr, alpha = 0.3,
                    beta=F,gamma=F)

thr7 <- HoltWinters(thr, alpha = 0.7,
                    beta=F,gamma=F)

plot(thr5, type='l', col='red')
plot(thr3, type='l', col='blue')   # 이게 제일 smooth함
plot(thr7, type='l', col='green')

predict(thr3,n.ahead = 7, prediction.interval = T) #예측하기


# 1987~1993 , 호주 팬시점에서 판매된 기념품 수 
library(data.table)
setwd('c:/Java/data')
fancy <- fread('fancy.csv', header=F)
tfancy <- ts(fancy, start=1987, frequency = 12)
plot(tfancy)  # 계절성이 보임,추세보임(3중) - 자동사용 가능



# 1989 ~2007, 호주 남부 주거용 전기 판매량 
power <- fread('power.csv',header=F)
tpower <- ts(power, start = 1989, frequency = 12)
plot(tpower) # 추세만 있음 - 자동x
etpower <- HoltWinters(tpower, alpha = 0.3, beta=0.2,gamma=F)
predict(etpower,n.ahead = 7, prediction.interval = T) #예측하기



# 주식데이터를 이용한 지수평활법 활용
nasdaq.com
investing.com