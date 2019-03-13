# 보스턴 주택 가격 예측 (회귀)
# 1970년 중반 보스턴 외곽지역의 범죄율 , 지방세율등의
# 데이터를 토대로 주택가격의 중간값 예측하기

from keras.datasets import boston_housing

# 보스턴 주택가격 데이터 불러오기
(xtrain, ytrain) , (xtest ,ytest) = boston_housing.load_data()

print('훈련데이터 크기',xtrain.shape)
print('검증데이터 크기',xtest.shape)
print('훈련데이터 ' , xtrain[:5])
print('레이블데이터' , ytrain[:10]) # 단위 천달러


# 데이터 정규화
# 서로 범위/크기가 다른 데이터를 신경망에 주입하면 문제발생 => 데이터 정규화 필요
# 평균 0 , 표준편차는 1이 되도록 데이터 값을 보정
mean = xtrain.mean(axis = 0) # 평균계산
xtrain -= mean

std = xtrain.std(axis = 0) # 표준편차
xtrain /= std


xtest -= mean # 훈련데이터와 검증데이터는 같은 스케일로 변환하기 위해 훈련데이터에서 사용한 mean ,std를 사용함
xtest /= std

# 모델 정의
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(64,input_dim=13, activation = 'relu'))
model.add(Dense(32 ,activation='relu'))
model.add(Dense(1)) # 회귀분석은 활성화함수 X

# 손실함수 최적화 함수 정의
model.compile(loss = 'mean_squared_error' , optimizer='rmsprop' ,metrics=['accuracy' ,'mse', 'mae'])
# mae (mean absolute error) : 오차 절대값
# mae가 0.3이면 주택가격은 평균 300 달러 정도 차이남

# # 훈련
# model.fit(xtrain,ytrain,epochs=500)
#
# # 검증
# mse1,mae1,mse2,mae2 = model.evaluate(xtest,ytest)
# print(mse1,mae1,mse2,mae2)

# 회귀분석시 평가방법
# 예측값과 실제값 사이의 오차정도도 평가함
# 아무래도 데이터에 대한 산점도를 그리고
# 회귀계수로 회귀직선을 그었을때
# 예측값에 일치하기란 쉬운것이 아님 - 정확도로 평가 x

# 회귀분석시 평가의 용이성을 위해
# 예측값과 실제값간의 오차관계를
# 그래프로 그려보는것이 좋음

import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns' , 500)
pd.set_option('display.width' , 1000)
# 훈련 상황을 화면에 표시 x , history 변수에만 저장 , validation_data 속성으로 검증 수행
history = model.fit(xtrain,ytrain,epochs=1000 , validation_data = (xtest , ytest) , verbose= 0)

# 저장된 훈련사항 데이터 프레임으로 생성 , epochs 라는 필드 생성 , history의 epoch값 넣기
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

print(hist.head())

plt.figure()
plt.xlabel('epoch')
plt.ylabel('mean absolute err [mae]')

# 훈련시 평균 절대값 오류
plt.plot(hist['epoch'] , hist['mean_absolute_error'] , label = 'train mae')

# 검증시 평균 절대값 오류
plt.plot(hist['epoch'] , hist['val_mean_absolute_error'] , label = 'test mae')

plt.legend()
plt.show()

# plt.figure()
# plt.xlabel('epoch')
# plt.ylabel('mean square error [mse]')
# plt.show()
#
plt.figure()
plt.xlabel('epoch')
plt.ylabel('loss')

plt.plot(hist['epoch'] , hist['loss'] , label = 'loss')
plt.plot(hist['epoch'] , hist['val_loss'] , label = 'val_loss')

plt.show()

# epoch가 1000번 일때 과적합 양상이 보임 => 500번 줄여도 무관
