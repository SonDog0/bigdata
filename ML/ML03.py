import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mglearn

# 로지스틱 회귀
# 주로 분류를 하기 위한 알고리즘
# 주로 예 1 아니오 0 등의 이진분류에 많이 사용
# 의료, 통신, 데이터마이닝 분야의 호귀 분류를 위한 예측모델로 활용

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X , y = mglearn.datasets.make_forge()
logr = LogisticRegression()
clf = logr.fit(X,y)
print('무슨값이지 ? ', X[:,0])
mglearn.discrete_scatter(X[:,0], X[:,1] , y )


logr = LogisticRegression(solver='liblinear')
# solver : scikit-learn 20.x 이상부터는 명시적 지정 필요
# liblinear : 이항회귀 , 작은 데이터셋에 적합한 알고리즘
# newton-cg, lbfgs : 다항 회귀 , L1 제약 사용
# sag, sega : 다항 회귀 ,L2 제약 사용 , 확률적 평균 경사 하강법 알고리즘 사용

#
#
clf = logr.fit(X,y)
#
# print('R^2 측정값' , clf.score(X,y))
mglearn.plots.plot_2d_separator(clf , X , fill= False , eps = 0.5 , alpha=.7)
#
# plt.show()

# 유방암 진단을 로지스틱 회귀로 분석하기
from sklearn import datasets
cancer = datasets.load_breast_cancer()

print('유방암 데이터' , cancer.data[:5])
print('유방암 구조' ,  cancer.feature_names)

X_train, X_test , y_train , y_test = train_test_split(cancer.data, cancer.target , random_state= 0)
print('타겟? ' , cancer.target)
log = LogisticRegression(solver='liblinear')
clf = logr.fit(X_train , y_train)

print('훈련정확도' , logr.score(X_train , y_train))
print('검증정확도' , logr.score(X_test , y_test))


# 입학여부를 로지스틱 회귀로 분석하기
# admit , gre , gpa , rank

admit = pd.read_csv('c:/java/data/admits.csv')

print('입학자료\n',admit[:5])

# 간단한 탐색적 분석
print(admit.head())
print('admit.describe()' , admit.describe())
print('admit.std()', admit.std())
admit.hist()
plt.show()

# 순위 항목을 더미변수로 생성
rank_dummy = pd.get_dummies(admit['rank'], prefix = 'rank')
print('더미변수', rank_dummy)

# 범주형 변수를 수치형 변수로 바꾸는
# 원핫인코딩 방식처럼 rank 컬럼의 각 값을
# 개별 컬럼으로 생성


cols_origin = ['admit' , 'gre' , 'gpa']
df = admit[cols_origin].join(rank_dummy.ix[: , 'rank_2' : ])
# rank_2 ~ rank_4 컬럼과 기존 컬럼을 합쳐서
# 새로운 데이터 프레임을 생성함

print(df.head())


# train , test 데이터 셋으로  나눔
data = df.iloc[:,1:6]
target = df['admit']

print('입학자료',data[:5])
print('결과자료',target[:5])

X_train , X_test , y_train , y_test = train_test_split(data, target , random_state= 0)



logr = LogisticRegression(solver='liblinear')
logr.fit(X_train,y_train)

print('훈련정확도' , logr.score(X_train, y_train))
print('검증정확도' , logr.score(X_test , y_test))


print('절편' , logr.coef_)
print('기울기' ,logr.intercept_)


# 더미변수
# 범주형 변수를 연속형 변수로 바꾼 것
# 선형회귀나 로지스틱 회귀 분석은
# 설명변수는 수치형 변수여야 사용 할 수 있는 기법

# 설명변수에 범주형 변수가 포함되어 있다면
# 그 변수를 더미변수로 변환해야 분석이 가능
# 즉, 범주형 변수를 연속형 변수스럽게 만들어야 한다는 의미

# 더미변수는 원래 범주형 변수의 범주갯수보다 1개 적게 생성
# 예를 들어, 변수가 성별인 경우 남자여부, 여자여부 중
# 더미변수는 하나만 생성하면 된다는 의미
# 변수가 대학년(1/2/3/4)인 경우  1/2/3 학년 여부 또는 2/3/4 학년 여부 중 하나만 생성하면 됨

# 더미변수를 이용하면 회귀 계수식에서
# 특정 변수의 효과를 0 또는 임의의 상수값으로 만들 수 있음
# 예를 들어 회귀식이 y = ax1 + bx2 + c 가 있고
# x2가 성별변수라 할 때
# x2 : 0 이면 => y = ax1 +c
# x2 : 1 이면 => y = ax1 + b + c
# 따라서, 더미변수를 통해 회귀식의 절편만 변경해서 회귀직선을 평행하게 위/아래로 움직이는 역할을 함  