import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


def titanic_barchart(feature):
    survived = train[train['survived'] == 1][feature].value_counts()
    dead = train[train['survived'] == 0][feature].value_counts()

    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    bp = df.plot(kind='bar', stacked=True, figsize=(10, 5))
    # bp = df.plot(kind='bar', stacked=False, figsize=(10,5))
    plt.setp(bp.get_xticklabels(), rotation=0)

    plt.show()


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

train = pd.read_csv('c:/Java/data/titanic_train.csv')
test = pd.read_csv('c:/Java/data/titanic_test.csv')

# 결측치 처리 중에서
# train 데이터에서 이름 컬럼에서 Mr, Mrs 추출하기
print(train.head())

train['title'] = train['name'].str.extract('([A-Za-z]+)\.')
test['title'] = test['name'].str.extract('([A-Za-z]+)\.')
# 대문자로 시작하면서 하나이상의 소문자로 구성 마지막은 .으로 끝남

# print(train['title'].value_counts())
# print(test['title'].value_counts())

# 승선객의 타이틀은 4가지 정도로 압축
# -> Mr(1), Mrs(2), Miss(3), Other(4)

titles = {'Mr':1,'Mrs':2,'Miss':3,'Capt':4,
          'Dr':5, 'Master':6,'Rev':6,'Major':6,
          'Mlle': 6,'Col':6,'Ms':6,'Lady':6,
          'Mme': 6,'Capt':6,'Jonkheer':6,'Don':6,
          'Countess': 6,'Sir':6}


train['title'] = train['title'].map(titles)
test['title'] = test['title'].map(titles)

# print(train['title'].head())

# 타이틀별 생존여부
# titanic_barchart('title')


# 나이 결측치 처리
# title 별로 나이의 중앙값을 계산 후 데체
print('나이컬럼 결측치 지수 train \n',train['age'].isnull().sum())
print('나이컬럼 결측치 지수 test \n',test['age'].isnull().sum())

print('전체나이의 중앙값 train \n', train['age'].median())
print('전체나이의 중앙값 test \n', test['age'].median())

# 타이틀별 나이 중앙값
print('title별 나이 평균\n',
      train.groupby('title')['age'].median())

# group by를 쓰면 transform 을 써야함
train['age'].fillna(train.groupby('title')['age'].transform('median'),
                    inplace=True)
test['age'].fillna(test.groupby('title')['age'].transform('median'),
                    inplace=True)

print(train.head())

# 나이 범위 조절
# 0~16:child(1)
# 16~26 : 2
# 26~ 46 : 3
# 46~66 : 4
# 66 : 5
train['newage'] = train['age']
# for i in range(len(train)):
#     if train['newage'][i] <= 16:
#         train['newage'][i] = 1
#     elif train['newage'][i] <= 26:
#         train['newage'][i] = 2
#     elif train['newage'][i] <= 46:
#         train['newage'][i] = 3
#     elif train['newage'][i] <= 66:
#         train['newage'][i] = 4
#     else :
#         train['newage'][i] = 5

# for i in range(len(train)):
#     if train.ix[i,'newage'] <= 16:
#         train.ix[i, 'newage'] = 1
#     elif (train.ix[i,'newage'] > 16)\
#         &(train.ix[i, 'newage'] <= 26):
#         train.ix[i, 'newage'] = 2
#     elif (train.ix[i,'newage'] >26)\
#         &(train.ix[i, 'newage'] <= 46):
#         train.ix[i, 'newage'] = 3
#     elif (train.ix[i,'newage'] >46)\
#         &(train.ix[i, 'newage'] <= 66):
#         train.ix[i, 'newage'] = 4
#     else :
#         train.ix[i, 'newage'] = 5


train.ix[(train['newage'] <= 16),'newage'] = 1
train.ix[(train['newage'] > 16)&(train['newage'] <= 26), 'newage'] = 2
train.ix[(train['newage'] > 26)&(train['newage'] <= 46), 'newage'] = 3
train.ix[(train['newage'] > 46)&(train['newage'] <= 66), 'newage'] = 4
train.ix[(train['newage'] > 66), 'newage'] = 5


print(train.head(50))

titanic_barchart('newage')

# 좌석등급별 승선위치별 생존현황
# 승선 위치
# 퀸즈타운Q
# 사우스햄튼S
# 세르부르C

train['newem']=train['embarked']

train.ix[(train['newem'] == 'S'),'newem'] = 1
train.ix[(train['newem'] == 'C'),'newem'] = 2
train.ix[(train['newem'] == 'Q'),'newem'] = 3

print(train['pclass'].head(10))
print(train['embarked'].head(10))