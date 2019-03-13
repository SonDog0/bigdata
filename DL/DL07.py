# 신경망의 구조
# 1 네트워크 또는 모델을 구성하는 층 layer
## 2차원 (데이터 , 레이블 ) - 완전연결층(1:1) , 밀집연결층(Dense)(1:N)
## 3차원 (데이터 , 시간 , 레이블 ) - 순환층 LSTM
## 4차원 (가로 , 세로 , 색상수 ) - 합성곱층convolution

# 2 입력데이터와 그와 상응하는 레이블 (특성 feature)

# 3 학습진행 방식을 결정하는 옵티마이저
## 훈련 하는 동안 손실은 최소화 되어야 함
## 각 층마다 여러 손실함수를 가질수있음
## 회귀 - mse
## 분류 - 이항(binary_crossentropy) , 다항(categorical_crossentropy)
## 시퀀스(순환층 LSTM ) - CTC connection temporal classfication

# 4 손실함수를 통해 네트워크가 어떻게 수정되어야 하는지 여부

# 케라스
# 거의 모든 종류의 딥러닝 모델을 간편하게 만들어 훈련시킬수 있는 파이썬용 딥러닝 프레임워크

# MIT 라이센스로 상업적 프로젝트에도 사용 가능
# 동일한 코드로 CPU , GPU에서 실행 가능
# 여러가지 백엔드 엔진에 추가 변동없이 매끄럽게 사용 가능
# -> tensorflow , theano, CNTK , MXNet

# 신경망을 위한 데이터 전처리
# 데이터벡터화 - 모든 입력/타겟은 부동소수float32로 이루어진 텐서여야 함
# 값 정규화 - 데이터를 네트워크에 주입하기 전에 정규화시켜 평균0 표준편차1로 되도록 설정
# 즉 , 값의 범위는 되도록 작아야 하고 ( 0 ~ 1 )
# 모든 특성이 대체로 비슷한 범위를 가져야 함
# 누락된 값 처리 - 제거, 평균/중앙값 , 0 대체

# 과대적합 vs 과소적합
# 기계학습의 근본적인 이슈 - 최적화, 일반화
# 최적화 - 훈련 데이터에서 최고의 성능을 얻고자 하는것
# 일반화 - 훈련된 모델이 이전에 본적 없는 데이터를 얼마나 잘 수행할지 가늠하는 것
# => 더 많은 훈련 데이터를 모으는것이 최선
# => 과대적합을 피하는 방법 : 분할 , 규제 , 교차검증
# 분할 : 훈련 데이터셋을 (train/test)로 나눔
# 규제 : L1 norm , L2 norm , dropout
# 교차검증 : k-fold, 데이터를 n개로 train/test 분할해서 훈련

# 교차검증 : k-fold validation
# 새로운 데이터에 모델이 얼마나 잘 일반화 되는지 알아보기 위해
# 보통 2-way 분할방식을 사용했었음
# 2-way : train/test로 나눠 일반화 정도 확인
# 3-way : train / validation / test


# 3-way 교차검증 순서
# 데이터셋을 (1) 먼저 모델 학습을 위한 '훈련'세트,
# (2) 적절한 모델 선택을 위한 '검증' 세트
# (3) 최종 선택된 모델을 평가하기 위한 '테스트' 세트로 나눔

# 하이퍼매개변수(가중치)를 튜닝해서 훈련데이터로 모델을 학습시킴
# 검증세트로 새로운 모델의 성능을 평가 -> 가장 성능이 좋은 모델의 하이퍼매개변수(가중치) 설정을 선택 ->  최종적으로 모델 선택
# 테스트 세트로 선택된 모델의 일반화 성능을 측정

# DL06e 예제 -> 3way로
from sklearn.datasets import load_boston
from sklearn.model_selection import KFold

boston = load_boston()

x = boston.data
y = boston.target
print('정규화 전 ' , x.mean(), x.std())
from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()
# x = scaler.fit_transform(x)
# print('정규화 후 ' , x.mean() , x.std())
#
# mean = x.mean(axis = 0) # 평균계산
# x -= mean
#
# std = x.std(axis = 0) # 표준편차
# x /= std
#
# y -= mean
# y /= std

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(64,input_dim=13, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(1))

model.compile(loss = 'mean_squared_error' , optimizer='rmsprop' ,metrics=['mae', 'mse'])


# 교차검증 초기화
n = 5
all_scores = []

kf = KFold(n_splits=n , shuffle= True)

from keras.datasets import boston_housing

# 보스턴 주택가격 데이터 불러오기
(xtrain, ytrain) , (xtest ,ytest) = boston_housing.load_data()


# 교차검증 실시 - train / test로 나눠 5번 각각 훈련시킴
for train, test in kf.split(x,y):
    # print('%d 번째 교차 검증 중 ... ' % (n))
    print(train , test)

    history = model.fit(x[train] , y[train] , epochs=1000, validation_data= (x[test] , y[test]) , verbose= 0 )

    val_mse , val_mae = model.evaluate(xtest,ytest,verbose=0)[0:2]
    all_scores.append(val_mae)

for i in range(0,len(all_scores)):
    print(all_scores[i])

# 정규화 처리후 훈련결과 : 평균 1500정도 오차 발생
# 원본 데이터로 훈련결과 : 평균 10달러 정도 오차 발생 