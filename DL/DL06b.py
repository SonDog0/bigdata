# 다중 분류 - iris 붓꽃 분류
# 활성화 함수 : softmax
# 다항 분류 : 카테고리 변수로 변환 => 원핫인코딩
# 손실 함수 : categorical_crossentropy

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf



iris= pd.read_csv('c:/java/data/iris.csv',header=None)

x = iris.iloc[:,0:4]
y = iris.iloc[:,4]

# 타겟 데이터가 문자형이면 -> 정수형으로 변환해서 범주화 ( 원핫인코딩 )
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(y)
y = le.transform(y)

print(y[:150])

# # 확인
# cnt_1 = 0
# cnt_2 = 0
# cnt_3 = 0
# for i in range(0,150):
#     if y[i] == 0:
#         cnt_1 += 1
#     elif y[i] == 1:
#         cnt_2 += 1
#     else:
#         cnt_3 += 1
#
# print(cnt_1)
# print(cnt_2)
# print(cnt_3)
#

# 활성화 함수는 입력데이터에 대해 0,1 로 결과를 출력함
# 0,1,2, 값을 갖는 iris 데이터를 0,1 형태로 재인코딩 해야함
# => 원핫인코딩으로 형태를 바꿔 재작성
#       0 1 2
# 0 : [ 0 0 0 ]
# 1 : [ 0 1 0 ]
# 2 : [ 0 0 1 ]

from keras.utils import np_utils
y = np_utils.to_categorical(y)
print(y[:150])

# 난수지정
seed = 190121
np.random.seed(seed)
tf.set_random_seed(seed)

# 모델생성
model = Sequential()
# 층을 순차적으로 쌓기위해 Seq 객체 선언
model.add(Dense(10,input_dim=4, activation='relu')) #입력
model.add(Dense(3,activation='softmax')) # 출력 # 0 , 1 , 2 원핫인코딩한거
# 원핫인코딩으로 출력결과를 재작성하는 경우
# 출력컬럼수 만큼 출력층 노드 지정 [ 0 0 1 ] => 3
# 활성함수는 softmax로 지정

# 손실함수, 최적화함수 정의
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy','mse']) #정확도,오차

# 훈련
model.fit(x,y,epochs=1000)

# 정확도 확인
# print('%.4f'% model.evaluate(x,y)[1])

# 예측 검증
# 6.4 2.7 5.3 1.9
# 5.7 2.6 3.5 1.0
# 4.5 2.3 1.3 0.3

new_one = np.array([[6.4,2.7,5.3,1.9]])
y_predict = model.predict(new_one)
print(y_predict)
print(y_predict[0][0],y_predict[0][1],y_predict[0][2])
#
# new_one = np.array([[7,2.2,4.6,1.5]])
# y_predict = model.predict(new_one)
# print(y_predict)
