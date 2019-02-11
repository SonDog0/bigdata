#머신러닝


#traing/test  데이터준비
# 머신러닝을 이용해서 지도학습 기반 모델을 생성할때
#전체 데이터 셋을 사용해서 한꺼번에 분석하지 않고
#학습용/평가용 데이터슷으로 분할 해서 분석 진행 한다.

#보통 일정한 비율로 데이터셋을 훈련/평가 데이터로 분할하는데
#7:3 또는 7.5:2.5 정도로 나눈다.


#ex) iris 데이터셋을 train/text 데이터로 분할.
1) 단순 분할
iris 데이터셋은 총 150개.
7:3 으로 분할 하면 1-5:45로 나눌 수 있다.
train <- iris[1:105,]
test <- iris[106:150,]

table(train[,5])
table(test[,5])

훈련/평가 데이터가 일관성이 없고 편중되어있다.

2)무작위 분할
set.seed(20181119)
idx <-sample(1:150,size=105,replace = F)
idx
train <- iris[idx,]
test <- iris[-idx,]

table(train[,5])
table(test[,5])

그래도 데이터는 일관성이 다소 부족하고 편중되어있다. 
-> 모델의 좋은 성능은 나오기가 어렵다.

3)각 데이터의 특성고 ㅏ분포를 고려해서 데이터를 분할할 필요가있다.
caret 패키지의 createDatePartition 함수 이용

install.packages('caret')
library(caret)


idx <- createDataPartition(iris[,5],p=0.7,list =F)

train <- iris[idx,]
test <- iris[-idx,]

table(train[,5])
table(test[,5])

데이터는 일관성 있게 구축되어있다.
-> 모델의 좋은 성능을 끌어낼수 있는 기반 마련.

#교차검증
전체 데이터를 이용해서 모델 생성 - 과적합 발생.
즉, 훈련 데이터는 잘 적중시키지만, 새로운 데이터에 대해
잘 적중시키지 못하는 문제가 생긴다.

과적합을 어느정도 줄일려면 주어진 데이터의 일부는 훈련데이터로 
사용하고 나머지는 검증 데이터로 사용한다.

훈련/검증 데이터로 분리해서 모델을 생성하는 방법중 하나는 
교차 검증을 이용하는 것이다. 즉, 데이터를 다수의 조각으로 나눈 후
(n 등분)훈련과 검증을 나누어 반복하는 방법이다.

#cvTolls 패키지를 이용해서 교차검증 실시
install.packages('cvTools')
library(cvTools)

cvFolds(15,K=3,type='')
#random,consecutive,interleaved
cvFolds(15,K=3,type='random')
#fold 1,2,3일때 검증 데이터의 idx는 453이다.
cvFolds(15,K=3,type='consecutive')
#fold 1일때 검증데이터의 idx는 12345이다.
cvFolds(15,K=3,type='interleaved')
#fold가 1일때 검증데이터의 idx는 123이다.

set.seed(2018111917)
cv <-cvFolds(150,K=5,type='interleaved')
cv
cv <-cvFolds(nrow(iris),K=5,type='interleaved')
cv

cv$which #교차 검증시 사용할 데이터의 회차 표시
head(cv$subsets) #교차 검증시 데이터 idx 표시

#교차검증 1회차 데이터.
idxK <- cv$subsets[which(cv$which == 1),1]
idxK
trainK1 <- iris[-idxK,]
testK1 <-iris[idxK,]

table(trainK1[5,])
table(testK1[5,])






#caret 패키지를 이용한 교차검증.
createFolds(iris[,5],k=5)
trainK1 <- iris[-cv$Fold1,]
testK1 <-iris[-cv$Fold1,]

table(trainK1[,5])
table(testK1[,5])




