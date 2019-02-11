# 연관성 분석
데이터 내부에 존재하는 연관성 
즉, 항목간의 상호관계 혹은 종속관계를 찾아내는 분석

대표적인 예 : 마케팅에서의 장바구니 분석

젊은 기혼 남성들은 기저귀와 백주를 동시에 구매함
=> 어린 자녀의 귀저귀를 사러 마트에 가서 
자신 혹은 아내와 같이 마실 맥주를 동시에 구매한다는 규칙을 알아냄
=> 따라서 상품 진열시 귀저귀와 맥주를 가까이 진열하여 매출 증가를 기대
    
고객이 구매한 장바구니를 살펴봄으로써 상품들의
연관성(규칙)을 발견하고 분석함으로써
상품을 사기 위해 움직이는 동선에 관련 상품을 진열하거나
관련 상품끼리의 묶음 상품을 개발
    
한편, 연관성을 일반화하거나 어느정도까지 신뢰할 수 있을까 등의 판단기준이 필요
=> 지지도support, 신뢰도confidence, 향상도lift


구매기록 데이터
맥주, 오징어, 치즈
소주, 맥주, 라면
맥주, 오징어, 사이다, 콜라
사이다, 오징어, 라면
치즈, 라면, 계란

# 신뢰도
ex) 맥주를 구매할 때, 어떤 상품을 추천할까?
상품A를 구매했을 때, 상품B를 함께 구매한 거래수

상품A에 대한 상품B의 신뢰도 =>
      상품A, 상품B 동시 출현 횟수 / 상품A출현 횟수

맥주-오징어 : 2/3
맥주-치즈 : 1/3
맥주-소주 : 1/3
맥주-라면 : 1/3

ex) 오징어와 잘어울리는 상품은 ?
오징어-맥주 : 2/3
오징어-사이다 : 2/3


# 지지도
상품A, 상품B 동시 출현 횟수/전체 횟수

맥주-오징어 : 2/5

=> 지지도는 신뢰도보다 높을 수 없음
단지, 같거나 작을뿐

# 향상도
상품A 기준 신뢰도가 동일한 상품B,C가 존재할 때,
어떤 상품을 더 추천해야 좋을지를 판단할 필요 존재

상품A,B의 신뢰도 / (상품B 등장횟수/전체거래수)

1 : 독립관계
1 초과 : 두 상품이 서로 양의 상관관계 
1 미만 : 두 상품이 서로 음의 상관관계

ex)
오징어-맥주 : 2/3
오징어-사이다 : 2/3

(2/3)/(3/5)
(2/3)/(2/5)

=> 맥주의 출현횟수가 사이다의 출현횟수보다 크므로
맥주가 인기상품이라는 것을 알 수 있음
하지만, 향상보를 구해보면 오히려 오징어 - 사이다의 향상도가 더 높음


# 상관성 분석 알고리즘
아프리오리(A Priori) 알고리즘
데이터들의 발생빈도를 기반으로
각 데이터간의 연관관계를 밝히는 방법


# 상관성 분석 패키지
install.packages('arules')
library(arules)

setwd('c:/Java/data')
연관규칙분석을 위해 데이터들을 매출이력(transaction) 형식으로 읽어와야 함

carts <- read.csv('carts2.txt',sep = '/',
                  header = T, stringsAsFactors = F)
carts <- as.matrix(carts)
carts <- as(carts,'transactions')
carts


inspect(carts)
summary(carts)
# density of 0.4 : 전체행렬중 1의 비율
# length distribution sizes : 거래 상품수

희소행렬의 크기 5 x 8 = 40
총 판매된 제품 수 : 40 * 0.4 = 16
평균 판매 횟수 16/5 = 3.2


itemFrequency(carts)
# => 상품의 거래비율을 출력
# => 전체 상품에 대한 지지도 수준으로 출력

ar <- apriori(carts, 
              parameter = list(supp=0.4, conf=0.6,
                               target='rules'))

# 신뢰도 0.5, 지지도 0.4 상품들의 상관성 분석
inspect(sort(ar))

# lhs : 규칙이 작동하기 위한 조건
# rhs : 규칙



# 상관관계를 그래프로 표시
install.packages('igraph')
library(igraph)

# 데이터 구조 변경
# 연관규칙rules을 행렬구조로 변경

# 상관성 그래프를 그리기 위한 규칙 생성

rules <- labels(ar, ruleSep=' ')
rules <- sapply(rules, strsplit, ' ',
                USE.NAMES = F)

rm <- do.call('rbind',rules)
rm

redg <- graph.edgelist(rm[,1:2], directed = F)
redg <- graph.edgelist(rm[-c(1:3),1:2], directed = F)
redg

plot.igraph(redg, vertex.label=V(redg)$name,
            vertex.label.cex=1.2,
            vertex.label.color='black',
            vertex.label.size=20,
            vertex.color='gray',
            vertex.fream.color='blue')


# 상관성을 막대그래프로 표시
itemFrequencyPlot(carts, support=0.4,
                  cex.names=0.8)

# 상관성을 그래프로 표시
install.packages('arulesViz')
library(arulesViz)


plot(ar, method='graph')
plot(ar, method='paracoord')
plot(ar, method='grouped')


# 장바구니 분석 2
x <- data.frame(
  beer=c(0,1,1,1,0),
  bread=c(1,1,0,1,1),
  cola=c(0,0,1,0,1),
  diapers=c(0,1,1,1,1),
  eggs=c(0,1,0,0,0),
  milk=c(1,0,1,1,1) )

carts <- as.matrix(x,'transaction')
carts

inspect(carts)

ar <- apriori(carts, 
              parameter = list(supp=0.4, conf=0.6,
                               target='rules'))

