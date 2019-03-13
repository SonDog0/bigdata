from typing import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mglearn

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets

# iris 데이터 셋 불러오기
iris = datasets.load_iris()

data = iris.data[:,:2] # 다항에서는 첫번째 두 컬럼 만 선정
target = iris.target


logr =LogisticRegression(solver='saga' , multi_class= 'multinomial', verbose=1)
logr.fit(data, target)

print('훈련 정확도',logr.score(data, target))

# 다항 로지스틱 회귀 분석시 결정 경계 확인
x_min = data[:,0].min() - 0.5 # x축 최소/최대
x_max = data[:,0].max() + 0.5

y_min = data[:,1].min() - 0.5  # y축 최소/최대
y_max = data[:,1].max() + 0.5

xx , yy = np.meshgrid(np.arange(x_min, x_max, 0.02) , np.arange(y_min, y_max, 0.02))
# 예측값으로 이용할 데이터 범위 지정

results = logr.predict(np.c_[xx.ravel(), yy.ravel() ])
# 데이터 범위를 이용해서 예측값 조사

results = results.reshape(xx.shape)
plt.pcolormesh(xx,yy,results, cmap= plt.cm.Set1)
# https://matplotlib.org/examples/color/colormaps_reference.html  / ref. cmap
# 예측값에 따라 적절한 색상을 지정

plt.scatter(data[:,0], data[:,1], c=target , cmap=plt.cm.Paired , edgecolors= 'k')

# plt.show()





# numpy 고급
# 배열 생성 : zeros , ones , arange , linsapace
print(np.zeros(5)) # 5개의 0으로 채워진 1차원 배열
print(np.arange(10)) # 0 ~ n-1로 채워진 배열
print(np.linspace(0,100, 5 )) # 구간을 지정한 수만큼 분할 ( 0부터 100까지 5개의 원소로 균등분할)


# c_

# ravel : n차월 배열을 1차원 배열로 변경
a = np.arange(12)  # [ 0 1 2 3 4 5 6 ... 12 ]
b = a.reshape(3,4)  # [[0,1,2,3] , [4,5,6,7] ...]
print(b)
c = b.flatten() # [ 0 1 2 3 4 5 6 ... 12 ]
print(c)
d = b.ravel() # [ 0 1 2 3 4 5 6 ... 12 ]
print(d)

# c_ : 행의 수나 열의 수가 같은 2개이상의 배열을
# 연결해서 더 큰 배열을 만들떄 사용
a = np.ones((2,3))
b = np.zeros((2,2))
result = np.hstack([a,b]) # 같은 행의 크기를 가진 배열을 합침 [ [ 1 1 1 0 0 ] , [ 1 1 1 0 0 ] ]
# 2행 3열 hstack  2행 2열 => 2행 5열 ( 새로운 열 추가 )
print(result)
c = np.zeros((1,3))
result = np.vstack([a,c]) # 같은 열의 크기를 가진 배열을 합침 [ [ 1 1 1 ] , [ 1 1 1 ] , [ 0 0 0 ] ]
# 2행 3열 vstack 1행 3열 => 3행 3열 ( 새로운 행 추가 )
print(result)

x = np.array([1,2,3])
y = np.array([4,5,6])

result = np.c_[x,y] # 1차원 배열을 연결해서 2차원으로 생성
# [ [ 1 4 ]
#   [ 2 5 ]
#   [ 3 6 ] ]
print(result)


# meshgrid
# 변수가 2개인 2차원 함수의 그래프를 그리기위해
# 2차원 영역에 대한 좌표값의 쌍이 필요
# 즉, x(0 ~ 2), y(0~4)라는 두 변수의 좌표값의 쌍은
# (0 0) (0 1) (0 2) (0 3) (0 4) (1 0) (1 1) ... (2 4)
d = np.arange(3)
e = np.arange(5)
X , Y = np.meshgrid(d,e)
print(X)
print(Y)

Z = [list(zip(x,y)) for x , y in zip(X,Y)]
print(Z)


# pcolormesh

# 내장된 칼라맵을 이용해서 히트맵을 그려주는 함수
rand = np.random.rand(20,20)
print(rand)
plt.pcolormesh(rand, cmap=plt.cm.tab20)
plt.show()