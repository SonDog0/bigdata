# 확률분포
# 모든 확률변수는 특정한 확률분포를 가짐
# 확률분포 - 일어날 수 있는 미래의 결과들의
# 범위에 대한 가능성을 보여줌

# 확률분포 : 일정한 패턴을 확률값이 퍼져있는것을 의미

# 이산확률 분포
베르누이, 이항(binom), 다항(multinom), 
초기하(hyper), 기하(geom), 음이항, 포아송(pois)

# 연속확률 분포
균등(unif), 정규(norm), 지수(exp), 
감마, 베타,T(t),카이제곱(chisq),F(f)


# 베르누이 확률분포
sample(c(0,1),1)  # 비복원 추출

p <- sample(c(0,1),10, replace = T)
table(p)
plot(p, col='red')
plot(density(p), col='red') # 확률밀도 곡선

# 출현확률 가중치 50% 부여
p2 <- sample(c(0,1),10, replace = T, prob=c(0.5, 0.5))
plot(density(p2), col='red')

p3 <- sample(c(0,1),10, replace = T, prob=rep(0.5, times=2))
plot(density(p3), col='red')



# 이항분포 : binom 함수 사용

R에서 확률분포 명령은 다음접두사를 결합해서 사용
d : 확률 밀도함수       (시점)
p : 누적 분포함수       (범위)
q : 분위수 계산 함수
r : 특정분포 난수 생성 함수


x <- dbinom(0:20, size=20,prob=0.5)
plot(0:20,x,type='h',col='blue')


ex) 1개의 동전을 4회 던졌을 때, 
앞이 나올 횟수를 확률변수 x라 할때, 
확률분포는?
단, 성공확률은 0.5라 가정

x<- dbinom(0:4,size = 4, prob=0.5)
x
plot(0:4, x, type='h',col='blue')

ex) 교통사고 10건중 6건은 음주운전 사고라 할 때
교동사고 8건중 음주사고가 6건일 확률은?

x<- dbinom(6,size = 8, prob=0.6)
x

ex) 부산-서울간 항공기 운항횟수는 5번
연착할 확률이 0.2 일때 한번도 연착하지 않을 확률은?

x<- dbinom(0,size = 5, prob=0.2)
x

ex) 통화실패확률 5%

dbinom(0,size = 6, prob=0.05)
dbinom(1,size = 6, prob=0.05)
dbinom(6,size = 6, prob=0.05)

# 과학지수 표기로 출력 -> 원래수로 출력
options('scipen'=100)


# 다항분포: (n!/(x1!*x2!*...*xk!))(p^x1*p^x2*...*p^xk)
보통 3가지 이상의 상황이 설정된 실험에서 사용
다른 분포에 비해 활용도는 떨어짐
한가지 상황을 정하고 성공/실패에 대한 실험이 대부분

베르누이 : 주사위 5가 나올 확률
이항 : 주사위 5가 3번 나올 확률
다항 : 주사위 5가 1번 , 3이 2번 나올 확률

dmultinom(c(1,2,0),prob=c(1/6, 1/6, 4/6))

ex) 자동차 점유율 8명중 현대:2, 수입:3,기아:1,GM:2 일확률
현대:32%, 기아:30%,수입:14%, GM:11%,르노:7%,쌍용:6%

dmultinom(c(2,3,1,2,0,0),prob=c(0.32,0.14,0.3,0.11,0.07,0.06))

ex) 1-1,2or3-2,4or5or6->3

dmultinom(c(1,2,3),prob=c(1/6,2/6,3/6))

# 초기하분포:kCm*(N-kCn-m)/(NCn)
ex) 빨주노초파 색의 공이 2개씩 있는상자에서
특정색의 공 하나 뽑을 확률? 2/10
다음 실험에서도 이 색의 공을 뽑을 확률?1/9

# kCi*(N-kCn-i)/(NCn)
# dhyper(i,k,N-n,n)
# i: 성공 횟수
# k: 성공 전체 갯수
# N-n: 실패 전체 갯수
# n: 비복원 추출 수


dhyper(x,m,n,k)
x: 뽑을 공의 수
m: 대상 공
n: 나머지 공
k: 비복원 추출 수
?dhyper
dhyper(2,2,8,2)

# 50명 40명 노조 5명뽑을때 4명 노조일 가능성
dhyper(4,40,10,5)

# 16대 5대 기준이상 매연 8대 뽑을때 3대 매연
dhyper(3,5,11,8)

# 16대 5대 기준이상 매연 8대 뽑을때 3대 이하 매연
sum(dhyper(0:3,5,11,8))

# 100, 불량 15 20개 뽑기, 불량 3개 이상
1 - sum(dhyper(0:2,15,85,20))

# factorial(n), ncol(combn(N,n)) = choose(N,n)
factorial(3)
combn(3,1)
?combn

ncol(combn(letters[1:4], 2))
ncol(combn(4,2))
choose(4,2)


# 포아송 분포 : (ㅅ^x e^-ㅅ)/x!
이항분포 다음으로 가장 많이 활용
일정한 시간과 공간 내에서 발생하는 사건의
발생횟수와 그에 따른 확률을 구할 때 사용

조건 : 가능성이 희박한 사건, 성공확률이 낮고 n이 큼
np<5, nq<5 일때


일정한 시공간에서 일어나는 사건의 발생횟수!

따라서, 사건의 발생횟수, 평균(람다)만 알면 확률값을 계산하기 쉬움

람다: 일정단위시간 , 단위공간에서 무작위로 발생하는 사건의 평균 횟수

ex) 평균3회 발생할때 0회 ~ 10회 발생할 확률값을 구하고 
이것에 대한  포아송분포 그래프

a<-dpois(c(0:10),lambda = 3)
plot(a, type='h')

ex) 포아송:3, 5일확률
dpois(5,lambda = 3)

ex) 포아송:20, 15일확률
dpois(15,lambda = 20)

ex) 포아송:3, 5일확률
dpois(5,lambda = 3)

ex) 포아송:0.3, 1일확률
dpois(1,lambda = 0.3)

ex) 포아송:20/500, 0일확률, 1일 확률
dpois(0,lambda = 0.04)
dpois(1,lambda = 0.04)

ex) 빵 100개 건포도 1000개 빵1개에 건도포 10~15개 있을 확률
sum(dpois(c(10:15),lambda = 10))



ex) 불량률 2% 100개추출 불량이 3개 이상 포함될 확률
sum(dpois(c(3:100),lambda = 2))

sum(dbinom(c(3:100), size=100,prob=0.02))




ex) 어떤 지역에 허리케인이 강타할 확률(p) 0.05
30(n)년동안 적어도 한번 허리케인 강타
sum(dbinom(c(1:30), size=30,prob=0.05))

b<-(1-dpois(0,lambda = 1.5))
plot(b, type='l')

ex) 회원 5% 연체 100명조사 10명이 연체 확률
dbinom(10,size=100,prob=0.05)
dpois(10,lambda = 5)

