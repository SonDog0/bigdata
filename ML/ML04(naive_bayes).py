# 나이브베이즈 분석
# 베이즈 정리 , 주어진 설명변수에 대한
# 모든 특성들이 조건부 확률에 근거한 알고리즘

# sklearn에서 구현된 나이브 베이즈 알고리즘은 총 세가지
# GaussianNB : 연속형 데이터
# bernoulliNB : 이진데이터
# MultinomialNB : 텍스트 데이터


# 피마 인디언 당뇨병 데이터를 이용한 나이브베이즈 분석
# 8개의 개인 특성을 토대로 당뇨병 여부 파악
# 1950년대 미국 인디언 강제이주 정책으로
# 피마부족의 절반이 아리조나로 추방하고 이들을 위한 자치구를 만듦
# 초원을 누비던 이들이 콜라와 햄버거를 먹으며
# 소파에 앉아 티비만 시청하게 됨
# 생활습관이 변하면서 이주인디언 절반이 비만/당뇨병 발병
# 식생활 변화와 비만/당뇨의 역학 관계 연구

# 임신횟수preg , 공복혈당plas, 혈압pres, 피부주름두께thick, 인슐린insul, 체질량bmi, 당뇨병가족력pedi, 나이age, 당뇨여부

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

indian = pd.read_csv('c:/java/data/indian.csv' , names =['preg','plas','pres','thick','insul','bmi','pedi','age','class'])

pd.set_option('display.max_columns', 500)

print(indian.head())

#EDA
print(indian.isnull().sum())
print(indian.describe())

indian.hist()


sns.countplot(indian['preg'])
sns.countplot(indian['age'])

# plt.show()

# 훈련 검증 데이터 분리
# data = indian.iloc[0:8]

data = indian[['preg','plas','pres','thick','insul','bmi','pedi','age']] # 나눠 쓰는거 이렇게 하면되네 ..!
target = indian['class']



# print(data)
# print(target)

X_train , X_test, y_train, y_test = train_test_split(data, target, random_state=0)

# 당뇨병 데이터가 연속형 데이터 이므로 가우시안 나이브베이즈
#

gnb = GaussianNB()

gnb.fit(X_train, y_train)

print('훈련 정확도',gnb.score(X_train, y_train))
print('검증 정확도',gnb.score(X_test, y_test))

# 오차행렬 출력
predict = gnb.predict(X_test)
print('' , confusion_matrix(y_test,predict))


# 로지스틱 회귀 분석
from sklearn.linear_model import LogisticRegression

logr =LogisticRegression(solver='liblinear')
logr.fit(X_train, y_train)

print('훈련 정확도' , logr.score(X_train , y_train))
print('검증 정확도' , logr.score(X_test , y_test))


# 나이브베이즈 vs 로지스틱 회귀분석
# 데이터셋이 작을때 (250~350) : 나이브베이즈
# 데이터셋이 클 때 : 로지스틱 회귀


# 위스콘신 유방암 데이터를 이용한 나이브베이즈 분석
# 30개 세포핵 특성을 기반으로 양성/음성 판단


# 로튼
