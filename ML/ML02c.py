# 보스톤 집값 데이터를 이용한 선형회귀분석

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, LinearRegression

boston = datasets.load_boston() # 특성수 13개

X, y = mglearn.datasets.load_extended_boston()

#기본 선형 회귀
Xtrain, Xtest, ytrain, ytest = train_test_split(
                     X, y, random_state=0 )

lr = LinearRegression().fit(Xtrain, ytrain)

print('훈련 정확도', lr.score(Xtrain, ytrain))
print('검증 정확도', lr.score(Xtest, ytest))   #특성이 너무 많음
print('사용한 특성수', np.sum(lr.coef_ != 0))

#릿지 회귀


ridge = Ridge().fit(Xtrain, ytrain)
#각 특성들이 모델에 주는 영향을 최소화하는 방향으로 회귀모형 생성

print('릿지 훈련 정확도', ridge.score(Xtrain, ytrain))
print('릿지 검증 정확도', ridge.score(Xtest, ytest))
print('사용한 특성수', np.sum(ridge.coef_ != 0))

#alpha = 0.1
ridge = Ridge(alpha=0.1).fit(Xtrain, ytrain)

print('릿지 a=0.1 훈련 정확도', ridge.score(Xtrain, ytrain))
print('릿지 a=0.1 검증 정확도', ridge.score(Xtest, ytest))
print('사용한 특성수', np.sum(ridge.coef_ != 0))

ridge = Ridge(alpha=0.5).fit(Xtrain, ytrain)

print('릿지 a=0.5 훈련 정확도', ridge.score(Xtrain, ytrain))
print('릿지 a=0.5 검증 정확도', ridge.score(Xtest, ytest))
print('사용한 특성수', np.sum(ridge.coef_ != 0))

ridge = Ridge(alpha=0.05).fit(Xtrain, ytrain)

print('릿지 a=0.05 훈련 정확도', ridge.score(Xtrain, ytrain))
print('릿지 a=0.05 검증 정확도', ridge.score(Xtest, ytest))
print('사용한 특성수', np.sum(ridge.coef_ != 0))


# #라소 회귀
from sklearn.linear_model import Lasso
#
lasso = Lasso().fit(Xtrain, ytrain)
# #제약에 따라 특정 특성들의 영향을 제외시키는 방향으로 회귀모형 생성
#
print('라소 훈련 정확도', lasso.score(Xtrain, ytrain))
print('라소 검증 정확도', lasso.score(Xtest, ytest))
print('사용한 특성수', np.sum(lasso.coef_ != 0))
#
#

#alpha = 0.01
lasso = Lasso(alpha=0.1).fit(Xtrain, ytrain)

print('라소 a=0.1 훈련 정확도', lasso.score(Xtrain, ytrain))
print('라소 a=0.1 검증 정확도', lasso.score(Xtest, ytest))
print('사용한 특성수', np.sum(lasso.coef_ != 0))
#
lasso = Lasso(alpha=0.3).fit(Xtrain, ytrain)

print('라소 a=0.3 훈련 정확도', lasso.score(Xtrain, ytrain))
print('라소 a=0.3 검증 정확도', lasso.score(Xtest, ytest))
print('사용한 특성수', np.sum(lasso.coef_ != 0))

lasso = Lasso(alpha=0.5).fit(Xtrain, ytrain)

print('라소 a=0.5 훈련 정확도', lasso.score(Xtrain, ytrain))
print('라소 a=0.5 검증 정확도', lasso.score(Xtest, ytest))
print('사용한 특성수', np.sum(lasso.coef_ != 0))

lasso = Lasso(alpha=0.05).fit(Xtrain, ytrain)

print('라소 a=0.05 훈련 정확도', lasso.score(Xtrain, ytrain))
print('라소 a=0.05 검증 정확도', lasso.score(Xtest, ytest))
print('사용한 특성수', np.sum(lasso.coef_ != 0))



