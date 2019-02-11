# 나이브베이즈 알고리즘
조건부 확률을 이용한 분류 알고리즘

조건부확률 : 어떤사건 A가 일어났을때
              사건B가 일어날 확률

베이즈 정리 : 두 확률변수의 사전확률과 
              사후확률 사이의 관계를 나타내는 정리

P(A∩B) = P(A)P(B|A)
P(A∩B) = P(B)P(A|B)

P(A|B) = P(A)P(B|A)/P(B)

# P(A|B) : B일때 A의 사후확률
# P(A) : A의 사전확률
# P(B|A) : A일때 B의 가능도(likehood)
# p(B) : 정규화 상수 - 무시하는 경우가 많음


# 영화마케팅 문제를 베이즈 정리로 해결함
# 영화관객의 성향을 설문조사로 정리
# 관객의 속성으로 영화취향을 파악

사전확률 :
조건부 확률 : P(A|B)
주변확률 : P(B|A)
  => 두사건이 동시에 일어 날 때 
      하나의 특정사건에 주목하여 그것이 일어날 확률

P(B) : 20대, 여 , IT, 미혼, 애인없음
P(A) : 공포영화를 선택할 확률

P(B|A)= P(20대, 여 , IT, 미혼, 애인없음|공포)
  => P(20대 | 공포) * P(여|공포) * P(IT|공포) * P(미혼|공포) * P(애인없음|공포)

P(A) : 액션
P(B|A)= P(20대, 여 , IT, 미혼, 애인없음|액션)


P(A) : 로맨틱
P(B|A)= P(20대, 여 , IT, 미혼, 애인없음|로맨틱)

P(A) : 코매디
P(B|A)= P(20대, 여 , IT, 미혼, 애인없음|코매디)


# 입사지원시 조건에 따라 합격여부 판별
# 나이, 장래희망유무, 인터뷰태도, 고교성적, 합격여부
사전확률
P(B) = 나이, 장래희망유무, 인터뷰태도, 고교성적
P(A) = 합격여부 확률


수집한 데이터의 수 :20
테스트 변수값 : 적음/없음/좋음/보통 -> ???

P(합격여부=합격)  = 13/20
P(합격여부=불합격) = 7/20

P(나이 = 적음|합격) = 4/13
P(나이 = 적음|불합격) = 3/7

P(장례희망 = 없음|합격) = 1/13
P(장례희망 = 없음|불합격) = 7/7

P(태도 = 좋음 | 합격) = 3/13
P(태도 = 좋음 | 불합격) = 1/7

P(성적 = 보통 | 합격) = 2/13
P(성적 = 보통 | 불합격) = 3/7

P(합격 | 적음/없음/좋음/보통) = 
  13/20 * (4/13 * 1/13 *3/13 *2/13)

P(불합격 | 적음/없음/좋음/보통) = 
  7/20 * (3/7 * 7/7 *1/7 *3/7)


# 나이브 베이즈에서 - 나이브 : 단순화
모든 변수가 서로 독립이라고 가정하고 확률 계산
사후확률값 자체를 아는것이 중요한 것이 아니고
각각의 사후확률의 크기를 비교하는 것만으로도 충분
따라서, 수식의 분모는 상수처럼 취급

각 변수의 상호작용을 고려해서 확률을 구하려면
수식이 상당히 복잡해지기 때문에 각 변수를
독립사건처럼 단순화함으로써 수식이 닺ㄴ순해지는
효과를 얻을 수 있음




# 0. 데이터 확인/ 전처리/기술통계

install.packages('mlbench')
library(mlbench)
?HouseVotes84

vote84 <- HouseVotes84

str(vote84)
# 투표안건 : 장애아동, 물프로젝트비용,
예산안채틱, 의료수가 동결, 특정국가 원조,
학교낸 종교단체 허용여부, 방위성 조사, 반군 원조,
mx미사일, 이민정책, 합성연료 감출,
교육비 지출, 

table(vote84$Class)


# 1. train/ test 데이터셋 분리
set.seed(2018112117)
library(caret)

idx <- createDataPartition(vote84[,1],
                           p=0.7, list=F)
train <- vote84[idx,]
test <- vote84[-idx,]

table(train[,1])
table(test[,1])

# 2. naive bayes 알고리즘 적용해서 분류모델 생성
e1071 패키지의 naiveBayes 함수 이용
library(e1071)
nb_vote84 <- naiveBayes(formula=Class~.,
                        data=train, laplace = 0)
nb_vote84

# 각 투표안건에 대한 민주당/공화당 대비 y/n 확률
# 즉, 주변확률에 대한 likehood를 측정한 것
nb_vote84$tables[1:2]


pred_vote84 <- predict(nb_vote84, newdata = test)

head(pred_vote84)

# 간단한 성능평가
library(caret)
confusionMatrix(data= pred_vote84,
                reference = test$Class,
                )


# ROC 곡선, AUC 값 조사
library(ROCR)
vote_roc <- prediction(labels = test[,1],
                       predictions = as.numeric(pred_vote84))
vote_roc_perf <- performance(vote_roc,
                             'tpr', 'fpr')
plot(wine_roc_perf)
lines(c(0,1), c(0,1), col='red', lty=2)



library(pROC)
auc(test[,1], as.numeric(pred_vote84))





# iris 데이터 셋 - 나이브 베이즈

# 1. train/test 데이터셋 분리
set.seed(2018112214)

str(iris)

library(caret)
idx <- createDataPartition(iris[,5], p=0.7, list = F)
train <- iris[idx,] 
test <- iris[-idx,]

table(train$Species)
table(test$Species)


# 2. 나이브 베이지 정리
library(e1071)

nb_iris <- naiveBayes(formula = Species~.,
                      data=train, laplace=0) 
# 라플라스 : 특정변수의 발생확률이 0에 가까우면
# 전체 추정결과가 왜곡될 가능성이 존재
# 따라서, 0에 가까운 발생확률에 소량의 값을 추가함으로써
# 왜곡되는 것을 방지하는 기능
# 보정방법 : laplace = 1

nb_iris

pred_iris <- predict(object=nb_iris, newdata = test)

pred_iris


# 3. 성능평가
confusionMatrix(data= pred_iris,
                reference= test$Species)

library(ROCR)
roc_iris <- prediction(labels = test[,5],
                       predictions = as.numeric(pred_iris))
vote_iris_perf <- performance(roc_iris,
                             'tpr', 'fpr')
plot(wine_roc_perf)
lines(c(0,1), c(0,1), col='red', lty=2)



library(pROC)
auc(test[,5], as.numeric(pred_iris))


# movie 데이터 셋 - 나이브베이즈
# 1
setwd('c:/Java/data')
mv <- read.csv('movies.csv',header = T, stringsAsFactors = F, sep=',')

str(mv)
summary(mv)

library(caret)

idx <- createDataPartition(mv$장르,p=0.7,list=F)

train <- mv[idx,]
test <- mv[-idx,]

table(train$장르)
table(test$장르)

train$장르 <- as.factor(train$장르)
test$장르 <- as.factor(test$장르)


# 2 나이브 베이즈
library(e1071)

nb_mv <- naiveBayes(formula=장르 ~ .,
                    data= train, laplace=0)

nb_mv

pred_mv <- predict(object=nb_mv,
                 newdata = test)

pred_mv


# 3 성능확인
confusionMatrix(data= pred_mv,
                reference = test$장르)





# tatanic 데이터 셋 - 나이브베이즈

