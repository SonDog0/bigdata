# KNN(k-nearest neighbor)
K-최근접 이웃 알고리즘
머신러닝 분류에 자주 사용되는 대표 알고리즘
얼굴인식, 개인영화추천, 질병 유전자 패턴 식별에 활용

KNN의 K는 가장 가까운 이웃하나가 아니고 
훈련데이터 중 새로운 데이터와 가장 가까운 
K개의 이웃을 찾는다는 의미

즉, 하나의 관측값은 
거리가 가까운 K개의 이웃관측값들과 비슷한 특성을 갖는다고 가정
따라서, K개의 이웃의 목표변수 중
다수결로 가장 많은 범주에 속한 값을 결과에 반환

KNN 알고리즘에서는 K를 얼마로 설정하느냐에 따라
결과와 성능이 달라짐
K가 작으면 데이터의 범위가 작아짐 - 이상치에 민감
K가 크면 데이터의 범위가 넓어짐 - 결과가 일반화 경향을 띔

일반적으로 데이터 건수의 제곱근을 K로 설정 

# iris 데이터를 이용한KNN 분류
# 0. 데이터수집 / 전처리 / 탐색적 분석(기술통계)
str(iris)
head(iris, n=5)
tail(iris, n=5)

table(iris$Species)  # 품종 빈도 확인

plot(iris)    # 데이터 분포 확인
plot(iris$Sepal.Length, iris$Sepal.Width)
plot(iris$Petal.Length, iris$Petal.Width)

summary(iris)

# 레이블을 제외한 표준화


# 1. 전체 데이터셋을 train/test로 분리
# 전체 데이터의 70% train
# 전체 데이터의 30% test

set.seed(2018112016)

install.packages('caret')
library(caret)
idx <- createDataPartition(iris[,5],
                           p=0.7, list=F)

train <- iris[idx, ]
test <- iris[-idx, ]

table(train[,5])
table(test[,5])

# KNN 알고리즘을 이용한 모델 생성
install.packages('class')
library(class)

knn_iris <- knn(train=train[,1:4],
                test=test[,1:4],
                cl=train[,5], k=3,
                prob = T)

# knn : train - 훈련데이터셋 지정
# knn : test - 검증데이터셋 지정
# knn : cl - 훈련데이터셋의 레이블 지정
# knn : k - 참고할 이웃 수 지정
# knn : prob - 레이블 추측 확률 표시 여부 지정


knn_iris    # 전체 결과 확인

# 예측값과 실제값을 비교
test[,5]  # 실제값
knn_iris[1:45]  # 예측값

table(test[,5], knn_iris[1:45])  

versicolor로 판단해야 할것을 
virginica로 오판한것이 2건 발생


# 모델 성능 평가
분류 모델의 성능을 평가하는 여러 기준 중
혼동행렬과 ROC 곡선을 활용

# 혼동행렬
caret 패키지의 confusionMatrix 함수 사용

library(caret)
install.packages('e1071')
library(e1071)
confusionMatrix(data=knn_iris[1:45], reference=test[,5])

confusionMatrix : data - 예측값 할당
confusionMatrix : reference - 실제값 할당


# Accuracy : 정확도
# Sensitivity : 민감도 - a 값을 a라고 재대로 측정한 정도
# Pos Pred Value : 재대로 분류 한 비율


# ROC곡선
거짓 긍정비율과 참 긍정비율 관계를 그래프로 표시
참 긍정 : 참인 값에 대해 참으로 예측
(암인 확자를 암환자로 예측)
거짓 긍정 : 거짓인 값에 대해 참으로 예측
(암환자가 아닌데 암환자로 예측 - 제 2종오류와 유사)

오차비율
(error rate)
(FP+FN) / (TP+TN+FP+FN)



install.packages('ROCR')
library(ROCR)

roc_data <- knn_iris[1:45]
roc_data <- roc_data[roc_data != 'setosa']
roc_data <- as.character(roc_data)
roc_data <- as.factor(roc_data)
length(roc_data)


roc_label <- test[,5]
roc_label <- roc_label[roc_label != 'setosa']
roc_label <- as.character(roc_label)
roc_label <- as.factor(roc_label)

length(roc_label)


iris_roc <- prediction(labels = roc_label,
                       predictions = as.numeric(roc_data))

iris_roc_perf <- performance(
  prediction.obj = iris_roc,
  measure = 'tpr', 
  x.measure = 'fpr'
)

iris_roc_perf

plot(x=iris_roc_perf)
lines(x=c(0,1), y=c(0,1),
      col='red', lty=2)

# AUC : 그래프 면적 계산
ROC 곡선을 이용한 평가는 직관적이지만,
여러 모델을 비교하기 위해서는
수치로 계량화 하는것이 좀더 편리함

범위는 0.5~1
대체로 0.7 이상이면 양호한 모델,
0.8이상일 경우 뛰어난 모델로 평가함

install.packages('pROC')
library(pROC)

auc(실제값, 예측값)

auc(test[,5], knn_iris[1:45])
auc(roc_label, as.numeric(roc_data))


# wine 데이터를 이용한KNN 분류

archive.ics.uci.edu/ml -> winequality 데이터셋
winequality-white.csv 파일을 다운로드한 후
wine_w.csv로 파일 변경

setwd('c:/Java/data')
wine <- read.csv('wine_w.csv',header = T, sep = ';', stringsAsFactors = F)


# 0. 데이터 수집 / 전처리 / 탐색적 분석(기술통계)
str(wine)

acidity : 산도
acid : 구연산
sugar : 당도
chlorides : 염화물
dioxide : 이산화황
density : 밀도
ph : 수소이온농도
sulphates : 황산염
alcohol : 알콜 함유량
quality : 와인 품질  (레이블)


head(wine)
tail(wine)

table(wine[,12])    # quality 빈도표

plot(wine[,c(1:5,12)]) # 데이터 분포 확인
plot(wine[,c(6:12)]) 


# 도수 분포표로 quality 빈도 확인
q<-barplot(table(wine[,12]),
        ylim=c(0,2500))
text(x=q, y= table(wine[,12]),
     labels = table(wine[,12]),
     pos = 3)

# quality 변수의 범위는 3 ~ 9
# 도수분포표로 확인해보니
# 3~6이 전체의 약 78%

# 3~6은 good으로 7~9는 best로 정함
# 새로운 레이블 변수를 생성

wine$grade[wine$quality <= 6] <- 'good'
wine$grade[wine$quality >= 7] <- 'best'

head(wine)

# 새로만든 레이블과 기존 레이블 간 빈도확인
table(wine$grade, wine$quality)


# 1. KNN을 위한 전처리 - 표준화
summary(iris)  # max, min 확인
summary(wine)  # 변수간 단위가 다름, 표준화 필요


변수간 척도(단위)가 다를 때 
단위가 큰 변수가 전체 결과에 
지배적인 영향을 미칠 수 있으므로
표준화를 거치면 모든 변수가 
평균 0 분산 1 인 정규분포를 따르게됨
scale 함수를 사용해서 각 변수를 표준화

std_wine <- scale(wine[,1:11], center = T, scale = T)
# => 결과를 행렬로 출력
std_wine <- as.data.frame(std_wine)
std_wine <- cbind(std_wine, grade=wine[,13])
# => grade 변수를 std_wine 데이터 프레임에 결합
summary(std_wine)

# 2. train/test 데이터셋으로 분리
set.seed(2018112115)
library(caret)

idx <- createDataPartition(std_wine[,12],
                           p=0.7, list=F)
train <- std_wine[idx,]
test <- std_wine[-idx,]

table(train[,12])
table(test[,12])


# 3. KNN 알고리즘 분류모델 생성
library(class)

knn_wine3 <- knn(train = train[,1:11],
                test = test[,1:11],
                cl=train[,12], k=3,
                prob = T)


knn_wine

table(test[,12],knn_wine3[1:1469] )  # 간단 성능 평가
summary(train)

knn_wine5 <- knn(train = train[,1:11],
                test = test[,1:11],
                cl=train[,12], k=5,
                prob = T)
table(test[,12],knn_wine5[1:1469] )



# 4. 성능평가

library(e1071)
confusionMatrix(data=knn_wine3[1:1469], reference=test[,12])

confusionMatrix : data - 예측값 할당
confusionMatrix : reference - 실제값 할당

library(ROCR)

wine_roc <- prediction(labels = test[,12],
                       predictions = as.numeric(knn_wine3))
wine_roc_perf <- performance(wine_roc,
                             'tpr', 'fpr')
plot(wine_roc_perf)
lines(c(0,1), c(0,1), col='red', lty=2)


library(pROC)

auc(test[,12], as.numeric(knn_wine3))
auc(test[,12], as.numeric(knn_wine5))

