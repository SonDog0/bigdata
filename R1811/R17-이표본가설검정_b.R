# 이표본 가설검정 기본 조건
표본 평균의 분포는 정규분포를 띈다고 가정
평균차이도 정규분포를 띔

이표본 가설검정시 표본분산이 모분산과 동일여부를 지정해야 함
t.test에서는 var.equal 속성으로 정의

따라서, 표본분산과 모집단의 분산 동일여부에 따라 
자유도와t 값을 계산하는 방식이 달라짐 - 수식이 다름

일반적으로 표본분산과 모집단의 분산은 서로 다르다고 보고 검정함

모분산과 동일한 경우 자유도 : -2
모분산과 동일 하지 않은 경우 자유도 : 수식복잡 생략


# 독립
ex) 잔디 깍기 기계 생산 공장
a 공정방식 5명 근로자
b 공정방식 6명 근로자
a=0.1

a <- c(2,4,9,3,2)
b <- c(3,7,5,8,4,3)

t.test(a,b,alternative = c('two.sided'), paired = F)
t.test(a,b,alternative = c('two.sided'), paired = T)  # 안됨

c <- c(131,135,146,165,136,142)
d <- c(130,102,129,143,149,120,139)

t.test(c,d, alternative = c('greater'))

ex) 흡수율 0.1퍼 유의수준 차이가 존재하는가?
x <- c(8,8,3,1,9,7,5,5,12)
y <- c(12,11,10,6,8,9,9,10,11,9,8,10)

t.test(x,y)

t.test(x,y,var.equal=T)

ex) 특정모델 수입이 더 크다

kim <- c(5,4.5,3.4,3.4,6,3.3,4.5,4.6,3.5,5.2,4.8,4.4,4.6,3.6,5.0)
park <- c(3.1,3.7,3.6,4.0,3.8,3.8,5.9,4.9,3.6,3.6,2.3,4.0)

t.test(kim,park, alternative = c('greater'))
t.test(kim,park, alternative = c('greater'),var.equal=T)
t.test(park,kim, alternative = c('greater'),var.equal=T)


# 대응표본 가설검정
종속표본 가설점정 : 서로 연관 있는 표본 paired sample

ex) 부동산 담보가치 평가 10채 0.05수준
zz <- c(235,210,231,242,205,230,231,210,225,249)
ss <- c(228,205,219,240,198,223,227,215,222,245)

t.test(zz,ss,paired = T)


#
library(MASS)
?shoes
shoes

인센티브 제공후 달라졌는가?
b <- c(320,290,421,510,210,402,628,560,360,431,506,505)
a <- c(340,285,475,510,210,500,631,560,365,431,525,619)

t.test(b,a,paired = T)

주간/ 야간 근무시 생산된 풀량품 수 비교 야간에 많이 생산되었는가? 0.05

d <- c(10,12,15,19)
n <- c(8,9,12,15)

t.test(d,n,paired=T,alternative = c('greater'))

당뇨병 치로제 신약 효과 검증

o <- c(51.4,52.0,45.5,54.5,52.3,50.9,52.7,50.3,53.8,53.1)
w <- c(50.1,51.5,45.9,53.1,51.8,50.3,52.0,49.9,50.5,53.0)

t.test(w,o,alternative = 'less',paired = T)

shoes
t.test(shoes$A,shoes$B,paired = T)

be <- c(14,7,4,5,17,12,8,9)
af <- c(2,7,3,6,8,13,3,5)

t.test(af,be,paired=T,alternative = c('less'))


