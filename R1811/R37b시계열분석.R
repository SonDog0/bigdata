# 시계열 자료 생성하기
시계열 분석을 하려면
자료를 시계열 객체로 생성해야 함

ts(데이터, 계열시작, 계열종료, 주기)
주기 - 12:월, 4:분기, 1:년

# 백화점 월별 매출액 자료
sales <- c(18,33,41,7,34,35,24,25,24,21,25,20,22,31,40,29,25,21,22,54,31,25,26,35)

ts.sales <- ts(sales, start = 2003, frequency = 12)
ts.sales
start(ts.sales)
end(ts.sales)
frequency(ts.sales)

plot(ts.sales)



# 시작년도, 월 지정
ts.sales2 <- ts(sales, start = c(2003,5), frequency = 12)
ts.sales2



# 시작년도, 분기 지정
ts.sales3 <- ts(sales, start = c(2003), frequency = 4)
ts.sales3

ts.sales3 <- ts(sales, start = c(2003,5), frequency = 4)
ts.sales3


# 시작년도, 년 지정
ts.sales4 <- ts(sales, start = c(2003,5), frequency = 1)
ts.sales4


# 핸드폰 데이터 사용량 자료
hand <- c(296,367,365,367,401,370, 281,313,373,352,377,356, 320,409,321,397,320,317, 306,313,324)
hand1 <- ts(hand, start = 2012, frequency = 12)

plot(hand1)


# 특정지역 여행자 방문자 수
trip <- c(143,152,161,139,137,174, 142,141,162,180,164,171, 206,193,207,218,229,225, 204,227,223,242,239,266)
trip1 <- ts(trip)
plot(trip1, start = c(2015), frequency = 1 )


# 수출입 자료
export <- c(362,385,432,341,382,409, 498,387,473,513,582,474, 544,582,681,557,628,707, 773,592,627,725,854,661)
export1 <- ts(export, start=2010, frequency = 12)
plot(export1)



# 사무용품 판매점 종사자 수
offdept <- c(98.1, 124.4, 156.7, 201.4, 227.3, 280.9, 298.8, 323.1, 344.8, 364.4, 331, 322, 317, 321, 331, 340, 365, 371, 385)
ts.offdept <- ts(offdept, start = 1996, frequency = 1)
plot(ts.offdept)

# 휘발유 1갤런 평균판매가격 (1996~2015)
gas <- c(1.2, 1.2, 1.03, 1.14, 1.48, 1.42, 1.35, 1.56, 1.85, 2.27, 2.57, 2.80, 3.25, 2.35, 2.78, 3.52, 3.62, 3.49, 3.34, 2.4)
ts.gas <- ts(gas, start=1996, frequency = 1)
plot(ts.gas)

# 배터리 판매수량(1996~2016)(단위:1000)
batt <- c(24, 30, 31, 26.5, 27, 27.5, 34, 35, 31, 32, 35.5, 41, 42, 38, 39, 46, 52, 53.5, 47, 51, 48)
ts.batt <- ts(batt, start = 1996, frequency = 1)
plot(ts.batt)

# 야구용품 판매자료(2014~2016)
baseball <- c(9, 10.2, 3.5, 5, 12, 14.1, 4.4, 7.3, 16, 18.3, 4.6, 8.6)
ts.baseball <- ts(baseball, start=1996, frequency = 4)
plot(ts.baseball)



# 세계은행에서 발표한 세계개발지수
install.packages('WDI')
library(WDI)

?WDI
WDIsearch()   #데이터 변수 출력

# 국가별 전체/1인당 GDP (dollar)
gdp <- WDI(country = c('US','KR','CN','JP'),
           indicator = c('NY.GDP.PCAP.CD',
                         'NY.GDP.MKTP.CD'),
           start=1960, end=2017)
head(gdp) 
names(gdp) <- c('code','nation','year','perGDP','GDP')

# 1인당 GDP 그래프
plot(gdp$year, gdp$perGDP)

# 전체 GDP 그래프
plot(gdp$year, gdp$GDP)


us <- gdp$perGDP[gdp$code=='US']
head(us)
ts.us <- ts(us, start = min(gdp$year))
plot(ts.us)

us2 <- gdp$GDP[gdp$code=='US']
head(us2)
ts.us2 <- ts(us2, start = min(gdp$year))
plot(ts.us2)
