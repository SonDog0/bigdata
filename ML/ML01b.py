import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pandasql import sqldf
from sklearn.model_selection import train_test_split
import mglearn

# 타이타닉 생존자 KNN 예측2
# 승객명, 좌석등급, 나이, 성별, 요금, 생존여부
# import seaborn as sns
#
pd.set_option('display.expand_frame_repr', False)
# titanic = sns.load_dataset('titanic')
# print(titanic.head())
#
# # 카테고리특성 수치형으로 변환
# titanic['sex'] = pd.Categorical(titanic['sex'])
# titanic['deck'] = pd.Categorical(titanic['deck'])
# titanic['alone'] = pd.Categorical(titanic['alone'])
# #       => 특정 특성을 카테고리형으로 분류해서 level을 추출
# print(titanic['sex'][:5])
#
# titanic['sex'] = titanic['sex'].cat.codes
# titanic['deck'] = titanic['deck'].cat.codes
# titanic['alone'] = titanic['alone'].cat.codes
# #       => 추출된 레벨에 맞춰 적절한 정수값으로 대체
# print(titanic.head())
#
#
# # 결측치 확인
# print(titanic.isnull().sum())
#
# mean = titanic['age'].mean()
# titanic['age'].fillna(mean, inplace=True)
#
# print(titanic.isnull().sum())
#
# # 훈련데이터, 테스트 데이터 추출
# titanic_data = titanic[['pclass','age','sex','fare']]
# titanic_target = titanic[['survived']]
#
#
# # 데이터 분할 및 모델 생성, 정확도 측정
# X_train, X_test, y_train, y_test = \
#     train_test_split(titanic_data, titanic_target, random_state=0)
#
# from sklearn.neighbors import KNeighborsClassifier
# knnclf = KNeighborsClassifier(n_neighbors=3)
#
# knnclf.fit(X_train,y_train)
#
# print(knnclf.predict(X_test))
# print('정확도\n', knnclf.score(X_test, y_test))
#
#
#
# # 새로운 데이터로 확인
# new_titanic = np.array([[2, 35.0, 1,10]])
# result = knnclf.predict(new_titanic)
# print('생존여부 예측(2,35,1)',result)
#
#
# # 타이타닉 생존자 탐색적 분석 - 그래프 위주
# import seaborn as sns
#
# print(sns.set())   # seaborn 설정 초기화


# 훈련/테스트 데이터 읽어오기
# SibSp : 동반 형제자매, 배우자수
# Patch : 동반 부모,자녀수

train = pd.read_csv('c:/Java/data/titanic_train.csv')
test = pd.read_csv('c:/Java/data/titanic_test.csv')

print(train.info())
print(test.info())
print(train.head())
print(test.head())


# # 막대 그래프를 이용해서 각 변수별 생존자 알아보기
# # 성별 생존자 현황
# survived = train[train['survived'] == 1]['sex'].value_counts()
# dead = train[train['survived'] == 0]['sex'].value_counts()
#
# df = pd.DataFrame([survived, dead])
# df.index = ['survived','dead']
# df.plot(kind='bar', stacked=True, figsize=(10,5))
# # df.plot(kind='bar', stacked=False, figsize=(10,5))

plt.show()


# # 승선 등급별 생존자 현황
# survived = train[train['survived'] == 1]['pclass'].value_counts()
# dead = train[train['survived'] == 0]['pclass'].value_counts()
#
# df = pd.DataFrame([survived, dead])
# df.index = ['survived','dead']
# bp = df.plot(kind='bar', stacked=True, figsize=(10,5))
# # bp = df.plot(kind='bar', stacked=False, figsize=(10,5))
# plt.setp(bp.get_xticklabels(), rotation=0)
#
# plt.show()



def titanic_barchart(feature):
    survived = train[train['survived'] == 1][feature].value_counts()
    dead = train[train['survived'] == 0][feature].value_counts()

    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    bp = df.plot(kind='bar', stacked=True, figsize=(10, 5))
    # bp = df.plot(kind='bar', stacked=False, figsize=(10,5))
    plt.setp(bp.get_xticklabels(), rotation=0)

    plt.show()

titanic_barchart('pclass')

titanic_barchart('sibsp')

titanic_barchart('parch')

titanic_barchart('cabin')

titanic_barchart('embarked')


# 자녀수별