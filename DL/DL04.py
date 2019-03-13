# 로지스틱 회귀
# 입력된 데이터를 바탕으로 참/거짓을 구분하는 분석 기법

# 공부시간대비 합격여부 분석
x=[2,4,6,8,10,12,14]
#y=['불합격','불합격','불합격','불합격','합격','합격','합격']
y=[0,0,0,0,1,1,1]

# 산점도 작성
import matplotlib.pyplot as plt

# plt.scatter(x,y)
plt.plot(x,y,'bo-')
# plt.show()
# S자 모양의 그래프 출력 - 시그모이드sigmoid

# 시그모이드 함수 식 : 1 / (1+e**(ax+b))
# 자연상수 e : 2.7182...
# 따라서, 우리가 구해야 하는 값 : ax+b
# a: 기울기(경사도), b: 절편(좌우이동)
# 기울기가 작으면 경사도가 낮아짐
# 기울기가 크면 경사도가 높아짐
# 따라서, 오차와의 관계는
# 지수형태의 그래프로 표시

import tensorflow as tf

# x,y 데이터 정의
data = [[2,0],[4,0],[6,0],[8,0],[10,1],[12,1],[14,1]]
x = [x[0] for x in data]
y = [x[1] for x in data]

# a,b 값을 임의로 지정
a = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=1))

b = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=1))

# 회귀식 정의 - 시그모이드 함수
import numpy as np

y_hat = 1 / (1+np.e **(a*x + b))

# 오차 측정식 : MLE( Maximum Likelihood Estimation)
# 오차 = -평균(ylog(h) + (1-y)log(1-h))
loss = -tf.reduce_mean(np.array(y) * tf.log(y_hat)
                       + (1-np.array(y)) * tf.log(1-y_hat))

# 학습률
learn_rate = 0.5

# 경사하강법
gradient_decent = tf.train.GradientDescentOptimizer\
                    (learn_rate).minimize(loss)

# 학습시작
#
# # 텐서플로우로 학습 시도
# with tf.Session() as sess:
#     #텐서플로 변수 초기화
#     sess.run(tf.global_variables_initializer())
#     # 학습 횟수만큼 훈련 - 적절한 기울기 찾음
#     # 총 학습횟수 2000 , 횟수 10회마다 진행상황 출력
#     for step in range(60001):
#         sess.run(gradient_decent)
#         if step % 1000 == 0 :
#             print('훈련횟수 epch %.f , loss %.4f , 기울기 %.4f , 절편 %.4f' % (step,sess.run(loss),sess.run(a), sess.run(b)))


# 결과 : 기울기 -4.6647 , 절편 41.8711
# 공부시간 5 , 13 일떄 합격여부 예측
# 모수에 대한 예측값은 확률로 출력
x = [5,13]
a = -4.6647
b = 41.8711
# 예측값을 넣어 회귀선을 그려봄
z = []

for xx in x:
    z.append(1 / (1+np.e **(a *xx + b)))
    print(1 / (1+np.e **(a *xx + b)))

# 실제값 , 예측값 출력
for i in range(len(x)):
    print('공부시간 = %.3f, 합격여부 = %.3f' %(x[i] , z[i]))

    