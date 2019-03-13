# 다중 선형 회귀
# 시간대비 성적 데이터
# 좀 더 정확한 예측을 하려면 더 많은 요인(factor)이 필요함
# 공부시간 외에 성적에 영향을 끼칠수 있는 다른 요인필요
# 과외시간을 추가함 => 항이 추가 => 기울기 하나 더 추가
# y = ax1 + bx2 + c

times = [2,4,6,8]
lession = [0,4,2,3]
sungjuk = [81,93,91,97]

data = [[2,0,81],[4,4,93],[6,2,91],[8,3,97]]
xdata1 = [x[0] for x in data]
xdata2 = [x[1] for x in data]
ydata = [x[2] for x in data]




import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

a = tf.Variable(tf.random_uniform([1],0,10, dtype =tf.float64, seed = 1 ))

b = tf.Variable(tf.random_uniform([1],0,10, dtype =tf.float64, seed = 1 ))

c = tf.Variable(tf.random_uniform([1],0,100, dtype =tf.float64, seed = 1 ))

y = a * xdata1  + b * xdata2 + c

# 평균 제곱근 오차
# square() : 제곱
# reduce_mean은 특정 차원을 제거하고 평균구함

rmse = tf.sqrt(tf.reduce_mean(tf.square(y-ydata)))

# 학습률 정의
learn_rate = 0.1

# RMSE를 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learn_rate).minimize(rmse)
# a,b 값을 찾는것 ( 기울기 , 절편 )

# 텐서플로우로 학습 시도
with tf.Session() as sess:
    # 세션(Session)은 텐서플로우(TenserFlow)를 실행시켜주는 클래스

    # 텐서플로 변수 초기화
    # 왜 초기화 ? 나중에 알려준대 ..
    sess.run(tf.global_variables_initializer())

    # 학습 횟수만큼 훈련 - 적절한 기울기 찾음
    # 총 학습횟수 2000 , 횟수 10회마다 진행상황 출력
    for step in range(2001):
        sess.run(gradient_decent)
        if step % 10 == 0 :
            print('훈련횟수 epch %.f , RMSE %.3f , 기울기1 %.3f, 기울기2 %.3f, 절편 %.3f' % (step,sess.run(rmse),sess.run(a), sess.run(b) , sess.run(c) ))

