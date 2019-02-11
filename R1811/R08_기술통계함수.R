# 기술통계 함수
# 모수의 분포와 중심화 경향, 퍼짐정도를 측정해서
# 집단의 특성을 기술
# 관측한 데이터를 도표로 정리하거나,
# 통계량을 정리함으로써 관측한 현상의 특징을 기술
# 연구 수행을 위한 데이터 수집이 완료되면
# 가장 먼저 수행행하는 분석 단계
# 주로 자료 분포에 대한 평균, 중앙값, 표준편차 등을 분석

# 데이터 확인
setwd=('c:/Java/data')
stores <-read.csv('productSales.csv', header = T, stringsAsFactors = F)

# 1 구조확인 
str(stores)

# 2 데이터 앞 뒤 임의 확인
head(stores, 10)
tail(stores, 10)

install.packages('car')
library(car)
some(stores, 10)   # 임의 표시

# 3. 데이터 요약
summary(stores)    #기술 통계 요약
length(stores)
nrow(stores)

min(stores$p1sales)
max(stores$p1sales)
mean(stores$p1sales)

median(stores$p1sales)    # 중앙
var(stores$p1sales)       # 분산 : 관측값의 퍼짐 정도
sd(stores$p1sales)        # 편차 : 퍼짐정도를 알아보는 또 다른 척도

quantile(stores$p1sales)  # 사분위

# 4. 데이터 범위, 치우침
range(store$p1sales)  # 범위

install.packages('fBasics')
library(fBasics)
skewness(store$p1sales)  #왜도 - 0보다 크므로 오른꼬리 분포

kurtosis(store$p1sales)  #첨도 - 3보다 크면 정규분포 곡선에 비해 다소 뽀죡한 모양

# 5. 기타등등
sum(store$p1sales)

rank(store$p1sales)    # 순위 출력  # 해당값에 대한 위치값이 출력

stores$p1sales[rank(store$p1sales) <= 10] # 값이 작은 순서로 10개 출력 - 정렬 안됨 

stores$p1sales[rank(-store$p1sales) <= 10] # 값이 큰 순서로 10개 출력 - 정렬 안됨 

x <- sample(1:50, 20) #난수 방식으로 표본 추출 (1~50 사이 수 중에서 20개 추출)
x
rank(x) # 작은 순서대로
rank(-x) # 큰순서대로

x[rank(x) <=5 ]  # 작은값들 중 5개만 추출
x[rank(-x) <=5 ] # 큰 값들 중 5개만 추출 

sort(stores$p1sales) # 정렬
sort(stores$p1sales, decreasing = T) # 내림 차순 정렬
head(sort(stores$p1sales, decreasing = T))
tail(sort(stores$p1sales, decreasing = T))

# gdp_rank_25, incomes 데이터셋을 이용해서
# 기술통계 함수를 이용해 데이터 수치적 분석 실시

# 문자 데이터를 숫자로 변경
install.packages('stringr')
library(stringr)   #문자처리 패키지
gdp_rank_25$GDP <- str_replace_all(gdp_rank_25$GDP, ',','')
new_gdp_rank_25 <- gdp_rank_25
new_gdp_rank_25$GDP <- as.numeric(new_gdp_rank_25$GDP)
new_gdp_rank_25

summary(new_gdp_rank_25$GDP)
skewness(new_gdp_rank_25$GDP)
kurtosis(new_gdp_rank_25$GDP)


str(incomes)
incomes$`2010` <- str_replace_all(incomes$`2010`, ',','')
incomes$`2010` <- str_replace_all(incomes$`2010`, '\\$','')
incomes$`2011` <- str_replace_all(incomes$`2011`, ',','')
incomes$`2011` <- str_replace_all(incomes$`2011`, '\\$','')
incomes$`2012` <- str_replace_all(incomes$`2012`, ',','')
incomes$`2012` <- str_replace_all(incomes$`2012`, '\\$','')
incomes$`2013` <- str_replace_all(incomes$`2013`, ',','')
incomes$`2013` <- str_replace_all(incomes$`2013`, '\\$','')
incomes$`2014` <- str_replace_all(incomes$`2014`, ',','')
incomes$`2014` <- str_replace_all(incomes$`2014`, '\\$','')
incomes$`2015` <- str_replace_all(incomes$`2015`, ',','')
incomes$`2015` <- str_replace_all(incomes$`2015`, '\\$','')

new_incomes <- incomes

incomes$`2010` <- as.numeric(incomes$`2010`)
incomes$`2011` <- as.numeric(incomes$`2011`)
incomes$`2012` <- as.numeric(incomes$`2012`)
incomes$`2013` <- as.numeric(incomes$`2013`)
incomes$`2014` <- as.numeric(incomes$`2014`)
incomes$`2015` <- as.numeric(incomes$`2015`)

