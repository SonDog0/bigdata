# 공부시간과 성적과의 관계
# 성적데이터
from keras.optimizers import RMSprop

x_data = [10,18,25,36,40,58,70,86]
y_data = [50,62,74,80,82,89,90,92]

# x_data = [10,20,30,40,50,60,70,80]
# y_data = [1,2,3,4,5,6,7,8]

# x_data = [2,4,6,8]
# y_data = [81,93,91,97]

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
#
# a = tf.Variable(tf.random_uniform([1],0,10, dtype =tf.float64, seed = 1 ))
#
# b = tf.Variable(tf.random_uniform([1],0,100, dtype =tf.float64, seed = 1 ))
#
# y = a * x_data + b
#
# # 평균 제곱근 오차
# # square() : 제곱
# # reduce_mean은 특정 차원을 제거하고 평균구함
#
# rmse = tf.sqrt(tf.reduce_mean(tf.square(y-y_data)))
#
# # 학습률 정의
# learn_rate = 0.01
#
# # RMSE를 최소로 하는 값 찾기
# gradient_decent = tf.train.GradientDescentOptimizer(learn_rate).minimize(rmse)
# # a,b 값을 찾는것 ( 기울기 , 절편 )
#
# # 텐서플로우로 학습 시도
# with tf.Session() as sess:
#     # 세션(Session)은 텐서플로우(TenserFlow)를 실행시켜주는 클래스
#
#     # 텐서플로 변수 초기화
#     # 왜 초기화 ? 나중에 알려준대 ..
#     sess.run(tf.global_variables_initializer())
#
#     # 학습 횟수만큼 훈련 - 적절한 기울기 찾음
#     # 총 학습횟수 2000 , 횟수 10회마다 진행상황 출력
#     for step in range(2001):
#         sess.run(gradient_decent)
#         if step % 10 == 0 :
#             print('훈련횟수 epch %.f , RMSE %.3f , 기울기 %.3f , 절편 %.3f' % (step,sess.run(rmse),sess.run(a), sess.run(b) ))


print('###########################################################################')


## 케라스로 학습 시도

# 모델 생성
model = Sequential()
model.add(Dense(1, input_dim=1 ))

# 비용 계산 함수
# model.compile(loss = 'mse', optimizer='sgd' , metrics=['accuracy'])

rmsprop = RMSprop(lr=0.01)    #학습률 지정
model.compile(loss='mse', optimizer=rmsprop )


# 2000회의 학습 시행
model.fit(x_data , y_data , epochs= 5000, verbose = 1 )


# 결과 출력
print('기울기 %.3f ' %model.get_weights()[0])
print('절편 %.3f ' %model.get_weights()[1])

# 예측하기
ypredict = model.predict(np.array([55]))
print('90시간 공부하면 ?'  , ypredict)

