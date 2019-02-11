# 로지스틱 회귀
logit 함수를 사용한 회귀분석이라는 의미

범주형 값(0,1 or 1,2,3)들을 이용해서
무언가를 예측하거나 분류할 때 사용

# 기존 회귀 vs 로짓 회귀

# logit.txt : 나이, 혈압, 암발생여부
setwd('c:/Java/data')
data <- read.csv('logit.txt', sep='\t', header = F)

str(data)
summary(data)
head(data)

# 나이, 혈압관계 산점도

a<-lm(data$V2~data$V1)
summary(a)
plot(data$V1, data$V2)
abline(lm(V2~V1, data=data),
       col='red', lty=2)

# 나이, 혈압은 연속형 값이므로 선형회귀 분석 가능

# 암발생여부는 범주형값이므로 선형회귀 분석 불가

b<-lm(data$V2~data$V1+data$V3)
summary(b)

plot(data$V1, data$V3)
abline(lm(V3~V1, data=data),
       col='red', lty=2)


로지스틱회귀의 경우 
종속변수 : 이산형
독립변수 : 이산 + 연속

독립변수의 계산값이 종속변수의 계산값과 맞지 않으므로 등호는 불일치
종속변수에 처리를 가해 범위를 맞추는 작업 필요 => logit 변환(odds + log)

odds => probability => chance => 확률

일반회귀식으로는 범주형값을 예측할 수 없으므로
y값의 확률을 이용해서 odds ratio로 변환하여 로그를 취하면
종속 독립변수 값을 등호로 표현할 수 있음


# 로지스틱 함수 그래프
library(e1071)
plot(sigmoid, -5,5)
abline(h=0, lty=2, col='red')
abline(h=1, lty=2, col='red')

# 대학교지원자들의
고등학교 성적으로 합격/불합격 분류
(합격여부(합격1, 불합격0), 성적, 학점, 출신학교 등급)

# 0. 탐색적 분석/
univ <- read.csv('admits.csv', header = T, stringsAsFactors = F)
str(univ)

admit, rank 범주형으로 변환
univ[,1] <- as.factor(univ[,1])
univ[,4] <- as.factor(univ[,4])

summary(univ)

# train / test 분리
library(caret)

set.seed(2018112316)
idx <- createDataPartition(univ[,1], p=0.7, list = F)

train <- univ[idx,]
test <- univ[-idx,]

table(train$admit)
table(test$admit)


# 2.
R에서의 로지스틱 회귀 함수
glm : 레이블이 이항일 때
mulitnom : 레이블이 다항변수일 때

library(e1071)
lr_univ <- glm(formula = admit~., 
               data=train, 
               family = binomial(link='logit'))
# family : 레이블변수의 분포유형

summary(lr_univ)   #로지스틱 회귀모형의 일반적인 정보

pred_univ <- predict(lr_univ, test)

table(pred_univ, test$admit)


# 3. 성능평가

예측한 레이블들은 목표변수의 확률값으로 출력
따라서, 그 확률을 이용해 
성공/실패를 규정짓는 기준점(cut-off)(0.5기준)를 설정해야 함


# 자동 cut-off 예측값 조사
pred_univ <- predict(lr_univ, test, type='response')

round(pred_univ) # 반올림 처리 후 출력

table(round(pred_univ), test$admit)

confusionMatrix(as.factor(round(pred_univ)), test$admit)


# 4. 로지스틱회귀 모형 분석
summary(lr_univ)

# pr(>|z|)
p-value가 0.05보다 작은 변수 : gre, rank2, rank3, rank4
통계적으로 유의미함

rank2~4 순으로 측정값이 마이너스 방향으로 강해짐
=> rank가 낮을수록 함격률 낮아짐

Deviance Residuals: 
      => 모형의 목표변수 실제값과 추정값간의 차이의 4분위값
          중앙값이 0에 가까울 수록 정규분포에 가까움

# Null deviance 와 Residual deviance
일반적으로 회귀모형을 생성하면
먼저 모형의 유의성 검정을 실시해야 함
유의성 검정을 2가지 방식으로 실시한 결과값이 deviance에 표시


Null deviance : 입력변수가 사용되지 않았을 때 (NULL)
                검정실시시 로그를 적용한 확률값으로 계산

Residual deviance : 입력변수가 사용되고 각 변수로 인한 오차값
                    검정실시시 카이제곱 통계량으로 계산

# Residual deviance를 이용한 카이제곱 통계량

두편차의 차를 계산
gap <- lr_univ$null.deviance - lr_univ$deviance

두 편차의 자유도 차를 계산함
dfgap <- lr_univ$df.null - lr_univ$df.residual


카이제곱 검정 실시 (pchisq 함수 사용)
범주형 데이터간 동질성/연관성 여부 검정


options(scipen = 100)
pchisq(gap, dfgap, lower.tail = F)

# iris 데이터셋을 이용한 로지스틱 회귀
# Speices가 3개의 레이블을 가지므로
# 다항 로지스틱 회귀를 적용해야 함

