# 상관분석
두변수 x,y 가 어떤 관계에 있는지 분석

변수간의 관계를 시각화한 후 상관계수 계산

ex) 판매원 15명
p <- c(96,40,104,128,164,76,72,80,36,84,180,132,120,44,84)
s <- c(41,41,51,60,61,29,39,50,28,43,70,56,45,31,30)

plot(p,s)

abline(v=mean(p),col='red')
abline(h=mean(s),col='blue')


#상관계수 공식
공분산/(x표편*y표편)
cov(p,s)/(sd(p)*sd(s))
공분산 : 시그마((xi-x바)(yi-y바))/(n-1)
cor(p,s)

sum((p-mean(p))*(s-mean(s)))/(sd(p)*sd(s)*(length(p)-1))


ex) applewood 구매자연령 판매이익
setwd('c:/Java/data')
aw <- read.csv('applewood.txt',header = T, sep=' ', stringsAsFactors = F)

library(stringr)
aw
summary(aw)
age <- aw$Age
aw$Profit <- aw$Profit

aw$Profit <- str_remove_all(aw$Profit,',')

aw$Profit <- str_remove_all(aw$Profit,'\\$')

aw$Profit <- as.integer(aw$Profit)

summary(aw$Profit)
head(aw$Profit)


plot(age,pf)
abline(v=mean(age), col='red')
abline(h=mean(pf), col='blue')



ex) ggplot2 에서 제공하는 economic
umemploy 수와 pce, psavert의 상관관계 분석 실시
library(ggplot2)

with(economics,plot(unemploy,pce))
with(economics,abline(v=mean(unemploy)))
with(economics,abline(h=mean(pce)))
with(economics,cor(unemploy,pce))

plot(economics$pce,economics$unemploy)
cor(economics$pce,economics$unemploy)


plot(economics$psavert,economics$unemploy)
cor(economics$psavert,economics$unemploy)


ex) MASS 패키지의 Cars93 데이터셋 사용
highway/city 연비
weight의 상관관계 분석


attach(Cars93)
  plot(MPG.highway,Weight)
  abline(v=mean(MPG.highway),col='red')
  abline(h=mean(Weight),col='blue')
  cor(MPG.highway,Weight)
  
  plot(MPG.city,Weight)
  abline(v=mean(MPG.city),col='red')
  abline(h=mean(Weight),col='blue')
  cor(MPG.city,Weight)
  
detach(Cars93)


plot(Cars93$MPG.highway,Cars93$Weight)
cor(Cars93$MPG.highway,Cars93$Weight)


plot(Cars93$MPG.city,Cars93$Weight)
cor(Cars93$MPG.city,Cars93$Weight)




# 상관행렬
install.packages('corrplot')
library(corrplot)

str(iris)
plot(iris[,seq(1:4)])

# corrplot
# 빨강 : 음의 상관관계
# 파랑 : 양의 상관관계

cor <- cor(iris[,1:4])
corrplot(cor)  
corrplot(cor, method='pie')
corrplot(cor, method='square')
corrplot(cor, method='color')
corrplot(cor, method='shade')  
corrplot(cor, method='ellipse')  
corrplot(cor, method='number')  


# car93
library(corrplot)
library(MASS)
str(Cars93)
Cars93$MPG.city
Cars93$MPG.highway

Cars93$Cylinders
Cars93$RPM
Cars93$Weight
Cars93$EngineSize
Cars93$Horsepower

plot()





# 놀이동산 만족도
주말이용여부, 동반자녀수, 공원까지 거리
기구만족도, 게임만족도, 대기시간 만족도
청결 만족도, 전체 만족도
setwd('c:/Java/data')
parks<-read.csv('parks.csv',header=T,stringsAsFactors = F)
cors <- parks([,4:8])
corrplot(cors)


mtcars
str(mtcars)
cors <- cor(mtcars[,1:4])
corrplot(cors,method = 'number')

상관계수 유의성 검정
판촉전화횟수와 판매량이 서로 관련언 없는데 
상관계수가 양으로 나온것은 아닌가?

  0.05 양측
  2.160

ex) 판매원 15명
p <- c(96,40,104,128,164,76,72,80,36,84,180,132,120,44,84)
s <- c(41,41,51,60,61,29,39,50,28,43,70,56,45,31,30)

t: (corr * sqrt(n-2)/sqrt(1-corr^2))
t: ((r-p)/sqrt((1-r^2)/(n-2))

cor(p,s)*sqrt(length(p)-2) / sqrt(1-cor(p,s)^2)
cor(p,s)/sqrt((1-cor(p,s)^2)/(length(p)-2))

# applewood
구매자의 연령 판매이익

cor(aw$Age,aw$Profit)

library(stringr)

summary(aw)

aw$Profit <- str_remove_all(aw$Profit,',')
aw$Profit <- str_remove_all(aw$Profit,'\\$')
aw$Profit <- as.integer(aw$Profit)

cor(aw$Age,aw$Profit)/sqrt((1-cor(aw$Age,aw$Profit)^2)/(length(aw$Profit)-2))


ex) 대학교 맥주와 혈중알콜 농도 사이 관계 조사 18명
임계값 : 2.120

b <- c(6,7,7,4,5,3,3,6,6,3,3,7,1,4,2,7,2,1)
a <- c(0.1,0.09,0.09,0.1,0.1,0.07,0.1,0.12,0.09,0.07,0.05,0.08,0.04,0.07,0.06,0.12,0.05,0.02)

plot(b,a)
cor(b,a)

cor(b,a)/sqrt((1-cor(b,a)^2)/(length(b)-2)) # 4.966187
