# 피마 인디언 당뇨병 예측하기
# 1~8열 : 환자 상태 (요인)
# 9열 : 당뇨병 여부

from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import tensorflow as tf

seed = 190118

# 동일한 결과 출력을 위해 난수 설정
np.random.seed(seed)
tf.set_random_seed(seed)


# 당뇨병 데이터 읽어오기

data= pd.read_csv('c:/java/data/indian.csv' ,header=None)
x = data.iloc[:,0:8]
y = data.iloc[:,8]

print(x.head(10))
print(y.head(10))

# 신경망 구성
# 입력변수 : 8
# 출력변수 : 1

model = Sequential()

model.add(Dense(20,input_dim=8 , activation='relu')) # 입력층
# 8개의 변수를 20개의 경우의수로 만듦
model.add(Dense(12,activation='relu')) # 은닉층
model.add(Dense(8,activation='relu')) # 은닉층
model.add(Dense(1, activation='sigmoid')) # 출력층

# 손실함수, 매개변수 최적화 정의
# model.compile(loss= 'mean_squared_error' , optimizer= 'adam' , metrics=['accuracy'])
model.compile(loss= 'binary_crossentropy' , optimizer= 'adam' , metrics=['accuracy'])

# 훈련
model.fit(x,y,epochs=1000)

# 최종정확도
print(model.evaluate(x,y)[1])
# 0.785 # 은닉층 1 , loss func = mse
# 0.833 # 은닉층 1, loss func = cce
# 0.803 # 은닉층 2 , loss func = mse
# 0.809 은닉층 2 , loss func = cce

# 0 , 1 단항 => 시그모이드
# 0 , 1 다항 => 엔트로피

# 예측하기 ( 22, 23번행 )
# 8	99	84	0	0	35.4	0.388	50	 0
# 7	196	90	0	0	39.8	0.451	41	 1

new_one = np.array([[8,99,84,0,0,35.4,0.388,50]])
y_predict = model.predict(new_one)
print(y_predict)
# 0.06

new_one = np.array([[7,196,90,0,0,39.8,0.451,41]])
y_predict = model.predict(new_one)
print(y_predict)
# 0.93


