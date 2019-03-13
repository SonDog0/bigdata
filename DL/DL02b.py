# 평균제곱근 오차

# 최소제곱법을 이용해서 회귀직선을 그어 보았지만
# 다양한 상황에 적합한 직선을 긋기에 부족
# 즉, 여러개의 변수로 구성된 데이터에 대한 회귀직선을
# 긋기에는 무리가 있음

# 따라서, 여러 변수로 구성된 데이터의 경우
# 임의의 선을 그린 후 이 선의 오차를 평가하고
# 조금씩 수정해 나가는 방법이 필요
# 주어진 선의 오차를 평가하는 방법 : 평균제곱근 오차

# 공부시간과 성적에 대한 상관/회귀 분석
X = [2,4,6,8]
y = [81,93,91,97]

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

plt.scatter(X,y)
plt.axis([1,9,75,100])
# plt.show()

# '최소 제곱법'에서는 공식을 이용해서 기울기 / 절편 계산 => 변수 하나일때만 가능
# '평균 제곱근 오차'는 기울기와 절편에 아무값이나 대입해서 여러 선을 그리고
#  각각 선마다 오차를 구하고 이 오차를 최소화하는 방식을 사용

# 평균제곱근오차 (RMSE, Root Mean_Square_Error) : (실제값 - 예측값)의 제곱 합 의 제곱근

# 제곱합의 제곱근 => abs개념 , 제곱합을 하고 제곱근을 씌워서 부호 제거


# 시도 # 1 : 기울기 = 3 , 절편 = 76
a = 3
b = 76


# 예측값을 넣어 회귀선을 그려봄
z = []
for xx in X:
    z.append(a*xx + b)

plt.plot(X,z,'ro-')

# 실제값 , 예측값 출력
for i in range(len(X)):
    print('공부시간 = %.f, 실제점수 = %.f , 예측점수 = %.f' %(X[i] , y[i] , z[i]))

# 오차 측정
# mean_squared_error(실제값, 예측값 )
MSE = mean_squared_error(y , z )
print(np.sqrt(MSE))

# 기울기가 크면 오차도 크다
# 기울기가 작으면 오차도 작다
# 즉 , 기울기와 오차간의 상관관계가 존재


# 시도 # 2 : 기울기 = 5 , 절편 = 76

a = 5
b = 76

z=[]
for xx in X:
    z.append(a*xx + b)
plt.plot(X,z,'go-')

MSE = mean_squared_error(y , z )
print(np.sqrt(MSE))


# 실제값 , 예측값 출력
for i in range(len(X)):
    print('공부시간 = %.f, 실제점수 = %.f , 예측점수 = %.f' %(X[i] , y[i] , z[i]))


# 시도 # 3 : 기울기 = 1 , 절편 = 76
a = 1
b = 76

z=[]
for xx in X:
    z.append(a*xx + b)
plt.plot(X,z,'bo-')

MSE = mean_squared_error(y , z )
print(np.sqrt(MSE))

# 실제값 , 예측값 출력
for i in range(len(X)):
    print('공부시간 = %.f, 실제점수 = %.f , 예측점수 = %.f' %(X[i] , y[i] , z[i]))


plt.show()



