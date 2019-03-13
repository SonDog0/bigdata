# 더미변수를 이용해서
# 타이타닉 데이터셋에 대해
# 로지스틱 회귀분석 실시

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mglearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# titan = pd.read_csv('c:/java/data/titanic.csv')
# pd.set_option('display.max_columns', 500)
# print(titan)
#
# suv_dummy = pd.get_dummies(titan['Survived'], prefix = 'suv' )
# print('더미변수', suv_dummy)
#
#
# cols_origin = ['Pclass' , 'Name' , 'Sex' ,'Age','SibSp', 'Parch','Ticket','Fare','Cabin','Embarked']
#
# df = titan[cols_origin].join(suv_dummy.ix[: ,'suv_1'])
# print(df.head())
#
#
#
#
#
# data = df.iloc[:,0:10]
# target = df['suv_1']
# print('###########')
# print(data)
# print(target)
#
# X_train, X_test , y_train , y_test = train_test_split(data, target , random_state= 0)
# print(X_train)
# print(y_train)

#
# logr = LogisticRegression(solver='liblinear')
# logr.fit(X_train,y_train)
#
# print('훈련정확도' , logr.score(X_train, y_train))
# print('검증정확도' , logr.score(X_test , y_test))


titanic = sns.load_dataset('titanic')

# null 여부 체크 - 나이는 중앙값으로 대체

print(titanic.isnull().sum())

medians = titanic['age'].median()
titanic['age'].fillna(medians , inplace = True)

print(titanic.isnull().sum())
print(titanic.head())

# 로지스틱 회귀에 사용할 변수 추출
datacol = ['pclass','sex','age','fare']
data = titanic[datacol]
target = titanic['survived']

print(data.head())
print(target.head())

# 범주형 변수를 수치형 변수로 변환 후 더미변수 생성

data['sex'] = pd.Categorical(data['sex'])
data['sex'] = data['sex'].cat.codes

print(data['sex'].head())

dummy_sex = pd.get_dummies(data['sex'] , prefix = 'sex')
print(dummy_sex.head())

data = data[datacol].join(dummy_sex.ix[:, 'sex_1' ])

print(data.head())

dummy_pclass = pd.get_dummies(data['pclass'] , prefix='pclass')
data = data.join(dummy_pclass.ix[:, 'pclass_2' :])

print(data.head())

# 로지스틱 회귀에 사용할 data, target 추출
data = data.iloc[:, 2:]
print(data.head())
print(target.head())

# 로지스틱 회귀분석 실시
X_train , X_test, y_train , y_test = train_test_split(data, target , random_state=0)
lgr = LogisticRegression(solver='liblinear')

lgr.fit(X_train, y_train)

print('훈련 정확도',lgr.score(X_train,y_train))
print('검증 정확도',lgr.score(X_test,y_test))

print(lgr.coef_)
print(lgr.intercept_)

plt.show()