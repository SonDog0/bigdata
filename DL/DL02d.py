# 케라스를 이용한 회귀 분석

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# 성적 데이터
xtrain  = [2,4,6,8]
ytrain = [81,93,91,97]

# 모델 생성 : 계층layer수 1  , 차원수 1
model = Sequential()
model.add(Dense(1, input_dim=1 ))

# 비용 계산 함수 : rmse
model.compile(loss = 'mse', optimizer='sgd' , metrics=['accuracy'])
# sgd = 경사하강법

# 2500회의 학습 시행
model.fit(xtrain , ytrain , epochs= 2500, verbose = 1 )
# verbose = 진행상황 T/F

# 결과 출력
print('기울기 %.3f ' %model.get_weights()[0])
print('절편 %.3f ' %model.get_weights()[1])

# 예측하기
ypredict = model.predict(np.array([55]))
print('55시간 공부하면 ?'  , ypredict)

ypredict = model.predict(np.array([10]))
print('10시간 공부하면 ?' , ypredict)
