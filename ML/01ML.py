# 파이썬으로 배우는 머신러닝

# 머신러닝 분류 - 지도학습, 비지도학습

# 머신러닝 변천사
# 인공지능 - 신경망 - 머신러닝 - 빅데이터 - 딥러닝

# 파이썬에서 머신러닝을 테스트/구현 하려면
# numpy, scipy, pandas, matplotlib, scikit-learn 등이 필요
# 부수적으로 mglearn 패키지도 설치할것

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import mglearn


# scikit-learn 에서 제공하는 데이터셋 확인
# iris = datasets.load_iris()
# boston
# wine
# cancer
# diabetes
# digits = datasets.load_digits()  # 숫자 필기 이미지

# lands = datasets.fetch_20newsgroups()  # 뉴스그룹 문자 자료
# faces = datasets.fetch_lfw_people()  # 얼굴 이미지 자료

# 훈련데이터와 테스트데이터 생성하기
# 지도학습으로 머신러닝 시스템 구축시 레이블(정답)된 데이터가 필요
# 이러한 데이터를 2개 그룹으로 나눠 작업하는데
# 특정 작업을 위한 모델생성 - 훈련데이터, training
# 생성된 모델의 작동여부 파악 - 검증/테스트 데이터, holdout
# 분할비율은 7:3(추천), 8:2, 7.5:2.5

# scikit - learn 에서는 이러한 작업을 위해 train_test_split 함수 제공
# 데이터는 X로, 레이블은 y로 표기함

# print(iris.data[:5,:])  # 붓꽃 데이터 상위 5개 출력
# print()
# print(iris.target[:5])  # 붓꽃 레이블 상위 5개 출력

# train_test_split으로 train, test 로 나누기
from sklearn.model_selection import train_test_split

# 훈련데이터, 레이블 : X_train, y_train
# 테스트데이터, 레이블 : X_test, y_test

# X_train, X_test, y_train, y_test =\
#     train_test_split(iris.data, iris.target,
#                      train_size=0.7, test_size=0.3,random_state=0)
# print('훈련데이터 갯수\n', X_train.shape)
# print('훈련레이블 갯수\n', y_train.shape)
# print('검증데이터 갯수\n', X_test.shape)
# print('검증레이블 갯수\n', y_test.shape)

# 데이터 살펴보기 - 산점도 행렬 이용
# 산점도 행렬 -  여러 변수의 상관관계를 한눈에 파악
# 머신러닝 사용여부/결측치/이상치/특이값 확인
# irisdf = pd.DataFrame(X_train, columns=iris.feature_names)
# pd.plotting.scatter_matrix(irisdf, c=y_train, s=50,
#                            cmap=mglearn.cm3, alpha=0.8, figsize=(10,10))
# plt.show()


# KNN : K-Nearst Neighbors 분류 알고리즘
# 새로운 데이터에 대한 분류 예측은 그것과 가장 가까운 훈련데이터를 찾아서 분류함

# KNN 예제용 데이터셋 생성
# X, y = mglearn.datasets.make_forge()
# print('KNN 예제 데이터')

# mglearn.discrete_scatter(X[:,0], X[:,1], y)
# plt.show()


# 새로운 데이터 3개를 추가해서 KNN 분류분석
# 추가된 데이터와 가장 가까운 훈련데이터 k개를 찾음
# 단, k가 3이상인 경우 레이블을 정하기 위한 다수결 채택
# 즉, 더 많은 이웃을 가진 데이터가 레이블로 정해짐
# mglearn.plots.plot_knn_classification(n_neighbors=1)
# plt.show() # 1-최근접 사용
#
# mglearn.plots.plot_knn_classification(n_neighbors=3)
# plt.show() # 3-최근접 사용

# KNN 예제용 데이터셋을 이용해서 KNN 알고리즘 적용
# X_train, X_test, y_train, y_test=\
#         train_test_split(X,y, random_state=0)
# 데이터를 자동으로 7:3으로 나뉨

# print('X데이터 크기',X.shape)
# print('훈련X데이터 크기',X_train.shape)
# print('검증y데이터 크기',y_train.shape)

from sklearn.neighbors import KNeighborsClassifier  # KNN 분류기 선언
#
#
# knnclf = KNeighborsClassifier(n_neighbors=3) # KNN분류기 k값 설정
#
# knnclf.fit(X_train, y_train)  # 모델학습
#
# print('모델 검증', knnclf.predict(X_test),y_test)
# print('모델 검증 정확도', knnclf.score(X_test,y_test))
#
# print()

# iris 데이터셋을 통한 KNN분석

# X_train, X_test, y_train, y_test =\
#     train_test_split(iris.data, iris.target,
#                      train_size=0.7, test_size=0.3,random_state=0)
#
# iris = KNeighborsClassifier(n_neighbors=3)
# iris.fit(X_train, y_train)
#
# print('모델 검증', iris.predict(X_test),y_test)
# print('모델 검증 정확도', iris.score(X_test,y_test))



# 새로운 데이터 예측 - 데이터셋에 존재하지 않는 데이터
# new_iris = np.array([[1,1,1,1]])
# result = iris.predict(new_iris)
#
# print('새로운 데이터로 예측',result)
# print('예측한 품종', iris['target'][result])


# 모델 정확도 측정 - confusion matrix
from sklearn.metrics import confusion_matrix

# cfm = confusion_matrix(y_test, iris.predict(X_test))
# print(cfm)


# 오차행렬을 그래프로 표시
import seaborn as sns
#
# sns.heatmap(cfm, square=True, annot=True, cbar=True, fmt='g')
# plt.xlabel('predict')
# plt.ylabel('versicolor/veginica/setosa')
# plt.show()

# 타이타닉 데이터셋을 이용한 KNN 분석1
# 승객명, 좌석등급, 나이, 성별, 생존여부


titanic = pd.read_csv('c:/Java/data/titanic.txt')
print(titanic.head())

titanic_data= titanic.iloc[:, 1:4]
titanic_target= titanic.iloc[:, 4]

print('추출된 데이터', titanic_data.head())
print('추출된 레이블', titanic_target.head())
