import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pandasql import sqldf
from sklearn.model_selection import train_test_split

pd.set_option('display.expand_frame_repr', False)
# 타타닉 데이터셋을 이용한 KNN 분석1
#

titanic = pd.read_csv('c:/Java/data/titanic.txt')
print(titanic.head())
# print(titanic.tail())

# 결측치 여부 확인
print(titanic.isnull().sum())

# 결측치 처리 - 제거
# titanic = titanic.dropna()
# titanic = titanic.reset_index(drop=True)

# 결측치 처리 - 0으로 대체
# titanic.fillna(0,inplace=True)

# 결측치 처리 - 평균/중앙/최대/최소값으로 대체
median = titanic['Age'].median()
mean = titanic['Age'].mean()
titanic.fillna(mean,inplace=True)


titanic_data = titanic.iloc[:,1:4]
titanic_target = titanic.iloc[:, 4]

# print(titanic_data.head())
# print(titanic_target.head())

print(titanic_data.isnull().sum())



# 카테고리 특성을 수치형으로 변환
# 좌석 등급 : 1st, 2st, 3st => 1,2,3
# 성별 : male, female => 0,1

for i in range(len(titanic_data)):
    try:
        if titanic_data['PClass'][i] == '1st':
            titanic_data['PClass'] = 1
        elif titanic_data['PClass'][i] == '2st':
            titanic_data['PClass'] = 2
        elif titanic_data['PClass'][i] == '3st':
            titanic_data['PClass'] = 3
        else:
            titanic_data['PClass'] = 3
    except:
        pass



for i in range(len(titanic_data)):
    try:
        if titanic_data['Sex'][i] == 'male':
            titanic_data['Sex'] = 0
        elif titanic_data['Sex'][i] == 'female':
            titanic_data['Sex'] = 1
    except:
        pass

print('전처리 완료 데이터', titanic_data.head())

# 데이터 분할
X_train, X_test, y_train, y_test = \
    train_test_split(titanic_data, titanic_target,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knnclf = KNeighborsClassifier(n_neighbors=3)

knnclf.fit(X_train,y_train)

print(knnclf.predict(X_test))
print('정확도\n', knnclf.score(X_test, y_test))



# 새로운 데이터로 확인
new_titanic = np.array([[2, 35.0, 1]])
result = knnclf.predict(new_titanic)
print('생존여부 예측(2,35,1)',result)