# 활성화 함수의 중요성
# 입력값과 가중치의 곱의 합으로 나온 결과를
# 한번 더 정제하기 위한 목적의 함수
# 여러 노드가 보내주는 값을 적절하게 필터링해서
# 출력층으로 값을 보내줘야만 올바른 분석을 할 수 있는 결과 도출

# 활성화 함수의 종류
# 시그모이드(sigmoid) : 초기 신경망에서 사용했던 활성화 함수
# MLP 신경망에서 발생된 문제 떄문에 더이상 사용하지 않는 활성화 함수
# 가중치 소멸 문제 : vanishing gradient
# 간단한 이항 분류에서는 사용 가능함


# tanh : 하이퍼블릭 탄젠트
# 시그모이드 함수의 y값을 -1~1로 확장
# 여전히 은닉층 수가 증가하면 가중치 소멸 문제 발생

# ReLu : 힌튼 교수가 제안 - 시그모이드 함수의 대안
# x가 0보다 작으면 모든값을 0으로,
# x가 0보다 크면 x값 그대로 사용

# ReLu -6 : X가 0보다 크면 그대로 사용하되
# 6을 넘지 않도록 조정

# softmax : 입력받은 값들이 0 ~ 1 사이의 값으로 출력하되
# 출력값의 총합이 항상 1이 되도록 함
# 주로 범주형 데이터 분석시 사용하는 활성화 함수




# 활성화 함수
# sigmoid
import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    y = []
    for i in x:
        y.append(1 / (1 + np.e **  -i ))

    return y


# x = np.arange(-10,10,0.2)
# print(x)
# sig = sigmoid(x)
#
# plt.plot(x,sig)
# plt.show()

# tanh
def tanh(x):
    y = []
    for i in x:
        y.append(np.sinh(i) / np.cosh(i))
    return y


# x = np.arange(-10,10,0.2)
# print(x)
# tan = tanh(x)
# plt.plot(x,tan)
# plt.show()
#

# ReLu
def relu(x):
    zeros = np.zeros(len(x)) #입력값 갯수만큼 영행렬 생성
    y = np.max([zeros , x ] , axis = 0 ) # 행기준 최댓값 비교
    return y
#
#
# x = np.arange(-10,10,0.2)
# print(x)
# rel = relu(x)
# plt.plot(x,rel)
# plt.show()

# softmax
def softmax(x):
    y= np.exp(x) / np.sum(np.exp(x),axis=0)
    return y



x = np.array([2.0,1.0,0.1])
softmax = softmax(x)
print(softmax) # 총합이 1인지 확인

plt.plot(x,softmax)
plt.show()

# 손실함수 loss function
# 비용cost함수라고도 함
# 신경망이 잘 학습하고 있는지를 나타내주는 지표
# 손실loss, 비용 cost , 출력값과 실제값 사이의 오차를 의미
# 신경망에서는 이것들이 최소하되도록 하는 과정이 학습임
# 따라서, 손실이 최소화 된다는것은 학습이 잘 되고 있다는것을 의미
# 딥러닝에서 손실함수는 평균제곱오차 MSE(회귀) mean_squared_error 와
# 교차엔트로피 오차 CEE(분류) binary_crossentropy 를 사용함


# 학습 최적화 방법
# 텐서플로에서는 optimizer로 설정

# 경사하강법 SGD - 확률적 경사 하강법 : 무작위 값을 대입
# 모멘텀 - SGD + 무작위 값에 탄성을 부여 (정확도 개선)
# 아다그라드adagrad - 학습률에 탄성을 부여 ( 보폭크기 개선 )
# 무작위 값 대입 횟수를 조절
# RMSprop - adagrad의 보폭 민감도를 개선
# Adam - 무작위값에 탄성부여, 학습률에도 탄성 부여, 즉, 정확도 개선 + 보폭크기 개선

import keras
keras.optimizer.Adam(lr = 0.0001 , beta_1 = 0.9 , beta_2 = 0.9999 , elpsilon = 1e-08 , decay = 0.0)


# AWS deeplearning framework 찾아보기 ( 외국에서핫함 ) MX_net


