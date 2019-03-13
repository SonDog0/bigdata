# # 학습된 모델 저장과 재사용
# # 학습이 끝난 후 테스트 결과가 만족스러울 때
# # 이를 모델로 저장해 두면 새로운 데이터에 바로 사용 가능
#
#
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf
#
# iris= pd.read_csv('c:/java/data/iris.csv',header=None)
#
# x = iris.iloc[:,0:4]
# y = iris.iloc[:,4]
#
# from sklearn.preprocessing import LabelEncoder
#
# le = LabelEncoder()
# le.fit(y)
# y = le.transform(y)
#
# from keras.utils import np_utils
# y = np_utils.to_categorical(y)
#
# seed = 190121
# np.random.seed(seed)
# tf.set_random_seed(seed)
#
# model = Sequential()
#
# model.add(Dense(10,input_dim=4, activation='relu'))
# model.add(Dense(3,activation='softmax'))
#
# model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy','mse']) #정확도,오차
#
# model.fit(x,y,epochs=1000)
#
# print('%.4f'% model.evaluate(x,y)[1])
#
# # 훈련 모델 저장하기
from keras.models import load_model
# model.save('models/iris.h5')


model = load_model('models/iris.h5')
# h5 파일 ( 딥러닝 모델저장 확장자 )
# 파일 직렬화 ? 다시볼때 한번더 알아보기 )

new_one = np.array([[6.4,2.7,5.3,1.9]])
y_predict = model.predict(new_one)
print(y_predict)
print(y_predict[0][0],y_predict[0][1],y_predict[0][2])