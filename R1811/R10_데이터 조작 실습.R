# data.seoul.go.kr
# 16품목 생필품 시장가격 조사 데이터
# 데이터셋의 헤더가 한글 -> sqldf에서는 깨져보임
# 따라서, 헤더는 포함시키지 않음
setwd('c:/Java/data')
market_price <- read.csv('seoul_food_price.csv',
                         sep=',',header=F, stringsAsFactors = F,
                         fileEncoding = 'UTF-8', skip=1)
summary(market_price)

# dplyr 조회 테스트
# head(market_price %>% select(품목.이름, 가격.원.))


# sqldf 조회 테스트
# head(sqldf('select [품목.이름], [가격.원.] from market_price'))
head(sqldf('select V5, V7 from market_price'))

# market_price 컬럼명을 적절히 변경(한글/영어)
colnames(market_price) <- c('num','market_num','market_name',
                            'goods_num','goods_name','standard','price',
                            'year_month','etc','check_date',
                            'market_type_code','market_type_name',
                            'state_code','state_name')
summary(market_price)

# 전통시장과 대형마트간 농수산물 가격차이 분석
# 이에 적절한 그래프
# 기간 : 2018-09, 2018-08

str(market_price)

library(dplyr)
mp <- market_price %>% select(goods_name,price,market_type_name, year_month)

str(mp)

# 시마 유형 확인
unique(mp$market_type_name)

# 년도, 시장 유형으로 분류
# market1 <- mp %>% filter(year_month == '2018-09'|year_month == '2018-8')
tmp <- mp %>% filter(year_month %in% c('2018-09', '2018-08'))

marcket1 <-  tmp %>% filter(market_type_name == '전통시장')
marcket2 <-  tmp %>% filter(market_type_name == '대형마트')

summary(marcket1)
summary(marcket2)

jdata <- aggregate(price~goods_name,marcket1, mean)
summary(jdata)

barplot(jdata$price, col = rainbow(67), 
        names.arg = jdata$goods_name,las=2)

plot(jdata$price, type='l')




bdata <- aggregate(price~goods_name,marcket2, mean)
summary(bdata)

barplot(bdata$price, col = rainbow(67), 
        names.arg = bdata$goods_name,las=2)

plot(bdata$price, type='l')








# 과일(배, 사과), 육류(닭/돼지고기), 채소(오이,상추) 등의 가격 변화를 구(state)별로 분석
# 이에 적절한 그래프
# 기간 2018-09, 2018-07

tmp2 <- mp %>% filter(year_month %in% c('2018-09', '2018-07'))

library(sqldf)
sqldf('select * from tmp where ')
