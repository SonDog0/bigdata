# 경사 하강법
# 평균 제곱근 오차 RMSE 를 통해 알아낸 사실

# 기울기가 크면 오차도 크다
# 기울기가 작으면 오차도 작다
# 즉 , 기울기와 오차간의 상관관계가 존재

# 기울기와 오차간의 관계를 그래프로 출력
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
weights = [] # 기울기
loss = [] # 오차

b = 0 # 절편 0으로 고정 값 설정

for w in range(-20 , 50 ): # 기울기를 -20 ~ 50 까지 설정
    xtrain = np.array([2,4,6,8])
    ytrain = np.array([91,93,91,97]) # 실제값

    pred = w * xtrain + b # 예측값

    weights.append(w)
    loss.append(np.sqrt(mean_squared_error(ytrain , pred)))
    # # mean_squared_error(실제값, 예측값 )
    # 기울기 별 오차 구하기 위한 값

print(weights,'\n',loss)

plt.plot(weights,loss)

# plt.show()

# 기울기와 오차와의 관계는 이차함수 그래프 형태로 출력
# 오차가 가장 작은 지점 ? => 그래프 하단의 볼록한 부분
# 따라서 , 임의의 한 점을 찍고
# 이 점을 그래프 하단지점까지 이동시키는 과정이 필요
# => 미분의 기울기를 이용하는 경사하강법을 적용
# => 즉 임의의 한점을 찍고 ,
# 그 지점을 미분 했을 때, 미분의 기울기가 0에 가까우면 오차도 작음

# 기울기를 구하는 과정
# 임의의 점을 선택 - 미분 실시 - 0인지 여부 확인
# 구해진 기울기의 부호 반대방향으로 임의의 점 선택 - 미분
# 미분 실시 후 - 기울기 0인지 여부 확인 - > 0이 될때 까지 계속 반복

# 정리
# => 임의의점 미분 -> 0아니면 -> 반대부호 방향으로 점선택 -> 미분 -> 0아니면 -> 반대방향 점 선택 ... -> 0이 될때 까지 반복


# 경사하강법 적용시 고려 사항
# 학습률(learning curve) : 기울기의 부호를 반대로 이동시킬때 , 적절한 거리를 찾지못해 너무 멀리 이동시키면
# 중심점을 지나칠 수 있음
# 따라서, 어느 만큼 이동시킬지 신중히 결정해야 함
# 케라스는 자동으로 이동거리를 조절 해 줌

# 텐서플로와 경사하강법을 이용한 선형회귀 예제

# x , y 데이터 설정

data = [[2,81],[4,93],[6,91],[8,97]] # 2차원 텐서 정의
x_data = [x[0] for x in data]
y_data = [x[1] for x in data]

# 기울기 a와 절편 b는 임의의 범위로 설정
# 기울기는 0 ~ 10 , 절편은 0 ~ 100으로 설정

import tensorflow as tf
# tf.random_uniform 함수는 정규분포 난수를 생성하는 함수로, 배열의 shape, 최소값, 최대값을 파라미터로 사용
a = tf.Variable(tf.random_uniform([1],0,10, dtype =tf.float64, seed = 1 ))

b = tf.Variable(tf.random_uniform([1],0,100, dtype =tf.float64, seed = 1 ))

# 선형 회귀식 정의
y = a * x_data + b

# 텐서플로에서 제공하는 평균제곱근 함수 사용
rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))

# 학습률 정의
learn_rate = 0.1

# RMSE를 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learn_rate).minimize(rmse)

# 텐서플로우로 학습 시도
with tf.Session() as sess:
    #텐서플로 변수 초기화
    sess.run(tf.global_variables_initializer())
    # 학습 횟수만큼 훈련 - 적절한 기울기 찾음
    # 총 학습횟수 2000 , 횟수 10회마다 진행상황 출력
    for step in range(2001):
        sess.run(gradient_decent)
        if step % 10 == 0 :
            print('훈련횟수 epch %.f , RMSE %.3f , 기울기 %.3f , 절편 %.3f' % (step,sess.run(rmse),sess.run(a), sess.run(b)))





