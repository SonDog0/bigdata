# 회귀분석

a : mean() -b*mean()
b : corr/sd*sd

ex) 판매원 15명
p <- c(96,40,104,128,164,76,72,80,36,84,180,132,120,44,84)
s <- c(41,41,51,60,61,29,39,50,28,43,70,56,45,31,30)

t: (corr * sqrt(n-2)/sqrt(1-corr^2))
t: ((r-p)/sqrt((1-r^2)/(n-2))
    
cor(p,s)*sqrt(length(p)-2) / sqrt(1-cor(p,s)^2)
cor(p,s)/sqrt((1-cor(p,s)^2)/(length(p)-2))

a=mean(s)-b*mean(p)
a

b=cor(p,s)*(sd(s)/sd(p))
b

y=19.98+0.261*x
19.98+0.261*100

lm(s~p)

# 회귀방정식 자세히 살펴보기
model <- lm(s~p)
options(scipen = 100)
summary(model)


# applewood 구매자 연령 판매이익
b = cor(aw$Profit,aw$Age)*(sd(aw$Profit)/sd(aw$Age))
b
a = mean(aw$Profit)-b*(mean(aw$Age))
a

y=1110.526+15.97x
1110.526+15.97*100
lm(aw$Profit~aw$Age)


# smallbs
setwd('c:/Java/data')
s<-read.csv('smallbs.txt ',header = T,sep='\t')
s

b=cor(s$Earnings,s$Sales)*(sd(s$Earnings)/sd(s$Sales))
b
a = mean(s$Earnings)-b*mean(s$Sales)
a
lm(s$Earnings~s$Sales)

y=1.851736 + 0.08357*x


# funds
f<-read.csv('funds.txt ',header = T,sep='\t')

b= cor(f$Return,f$Assets)*((sd(f$Return))/(sd(f$Assets)))
b
a=mean(f$Return)-b*mean(f$Assets)
a
lm(f$Return~f$Assets)
plot(f$Assets,f$Return)
y=9.92-0.0003933*x



# citycrime
c<-read.csv('citycrime.txt ',header = T,sep='\t')
plot(c$Crimes,c$Police)

b = cor(c$Crimes,c$Police)*(sd(c$Crimes)/sd(c$Police))
b
a=mean(c$Crimes)-b*mean(c$Police)
a
lm(c$Crimes~c$Police)
y=29.34 - 0.9596*x


# oldcars
o<-read.csv('oldcars.txt ',header = T,sep='\t')
plot(o$Price,o$Age)

abline(lm(o$Price~o$Age), col='red')
abline(h=mean(o$Price), lty=3)
abline(v=mean(o$Age), lty=3)


b=cor(o$Price,o$Age)*sd(o$Price)/sd(o$Age)
b
a=mean(o$Price)-b*mean(o$Age)
a
lm(o$Price~o$Age)
y=11.18-0.4788*x


# 잔차와 최소제곱법
sum((yi-y헷)^2)


# 예측값 알아보기 : predict
predict(lm(a,b)) 함수는 b 변수값을 방정식에 넣어
출력된 값을 실제 a값과 비교
예측값 : predict(lm(o$Price~o$Age))
잔차 : o$Price - predict(lm(o$Price~o$Age))
sum((o$Price - predict(lm(o$Price~o$Age)))^2)


# 회귀식의 예측력 평가
예측력 : 추정치의 표준오차

전화횟수 대비 판매량에 대한 회귀식
y=19.98+0.261*x

19.98+0.261*84

predict()

정확한 예측이란? - 정확한 결과값을 도출하는 것을 의미
모든분야에서는 불가능한 것으로 알려져 있음

추정에 있어 추정치x에 근거 
얼마나 정확하게 예측/얼마나 부정확할 수 있나등의
척도가 필요 -> 추정치의 표준오차


편차 제곱합 : sum((o$Price - predict(lm(o$Price~o$Age)))^2)
sqrt(편차제곱합/n-2) # SSR

추정치의 표준오차가 작음 - 추정치가 잘 맞음

# 전화횟수 대비 판매량에 대한 SSR
e <- sum((s - predict(lm(s~p)))^2)
e  
ssr <- sqrt(e/(length(p)))
ssr

model <- lm(s~p)
summary(model)

# 결정계수
결정계수를 통해 회귀식이 얼마나 정확한지 알 수 있음
보통 0~1
즉, 결정계수는 종속변수y의 변동이
독립변수x의 변동에 의해 설명될 수 있는 비율 

결정계수 구하는 방법 2가지
1) 상관계수 제곱
2) ANOVA테이블의 데이터를 이용(회귀변동/총변동)

adjustedR^2가 중요!


# 신뢰구간 예측구간 구하기
추정치의 표준오차와 결정계수를 통해
회귀식의 종속변수 예측력에 대한
전반적인 평가를 내렸었음

회귀식의 예측력을 표현하는 또 다른 방식은
독립변수의 특정값을 알아보는 것

신뢰구간 예측을 위한 선형회귀 가정
1)X값은 Y값에 각각 대응 -Y값은 정규분포
2)X,Y 값의 평균은 회귀직선 위에 놓임
3)추정치 표준오차는 동일
4)Y값은 확률적으로 독립적
  ->X에 의해Y가 변함

ex) 전화횟수 대비 판매량에 대한 회귀식을 토대로 50회에대한 95% 신뢰구간과 예측구간

19.9632+0.2608*50 # 33.0032





신뢰구간 : t * s *sqrt((1/표본수)+편차제곱/sum(편차제곱))
s: 추정치에 대한 표준 오차

t: 95%신뢰구간, DF : 13 => 2.160
e <- sum((s - predict(lm(s~p)))^2)
s <- sqrt(e/(length(p)))
s


편차제곱/편차제곱합
(x-mean(x))^2  /  sum((x-mean(x)^2))
e2 <- ((50-mean(p))^2/sum((p-mean(p))^2))



2.160*s*sqrt((1/(length(p)))+e2)


예측구간 : t * s *sqrt(1+(1/표본수)+편차제곱/sum(편차제곱))
2.160*s*sqrt(1+(1/(length(p)))+e2)




# 신뢰구간/예측구간 그래프
fitplot(model)


# 신뢰구간 예측구간 함수
model <- lm(s~p)

coef(model)   # 회귀계수(기울기, 절편)
fitted(model)[1:15]  # 추정값
residuals(model)  # 추정치의 표준오차 : 잔차
deviance(model)   # 잔차제곱합
confint(model)    # 회귀계수 신뢰구간

ps <- data.frame(p,s)


predict(model, interval = 'confidence', newdata = data.frame(p=50))    # 신뢰구간
predict(model, interval = 'prediction', newdata = data.frame(p=50))    # 예측구간




# 신뢰구간

phone <- seq(min(p),max(p),1)
csales <- predict(model, interval='confidence', newdata=data.frame(p=phone))

plot(p,s)
abline(lm(s~p), col='black')
lines(phone, csales[,2],col='red', lty=2)
lines(phone, csales[,3],col='red', lty=2)


# 예측구간
psales <- predict(model, interval='prediction', newdata=data.frame(p=phone))
lines(phone, psales[,2],col='blue', lty=2)
lines(phone, psales[,3],col='blue', lty=2)


ex)시간대비 몸무게
MASS ChickWeight

library(MASS)
str(ChickWeight)
chick1 <- ChickWeight[ChickWeight$Chick == 1,]


with(chick1, plot(Time, weight))
abline(m, col='red')

with(chick1, cor(weight,Time))

m <- with(chick1, lm(weight~Time))
summary(m)

coef(m)
y=24.47 + 7.988*x

predict(m)
conf <- predict(m, interval = 'confidence')
pref <- predict(m, interval = 'prediction')

lines(chick1$Time, conf[,2], col='blue', lty=3)
lines(chick1$Time, conf[,3], col='blue', lty=3)

lines(chick1$Time, pref[,2], col='orange', lty=3)
lines(chick1$Time, pref[,3], col='orange', lty=3)



predict(m, newdata = data.frame(c(3,21)))