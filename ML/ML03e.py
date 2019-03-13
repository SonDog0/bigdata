import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 타이타닉 데이터셋을 이용해서
# 로지스틱 회기분석 결정경계 확인하기

titanic = sns.load_dataset('titanic')

medians = titanic['age'].median()
titanic['age'].fillna(medians,inplace = True)

target = titanic['survived']
datacol = ['pclass' ,'sex' ,'age','fare']

df = titanic[datacol]

titanic['sex'] = pd.Categorical(titanic['sex'])
titanic['sex'] = titanic['sex'].cat.codes

dummy_sex = pd.get_dummies(titanic['sex'] , prefix= 'sex')
df = df[datacol].join(dummy_sex.ix[:,'sex_1'])

dummy_pc = pd.get_dummies(titanic['pclass'] , prefix= 'pclass')
df = df.join(dummy_pc.ix[:,'pclass_2'])

data = df.ix[:,['age','fare']] #결정경계 대상 컬럼 지정

target = titanic['survived']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train , X_test , y_train, y_test = train_test_split(data, target , random_state= 0)

logr = LogisticRegression(solver='liblinear')
logr.fit(X_train , y_train)
logr.score(X_train , y_train)

print('훈련 정확도' , logr.score(X_train , y_train))
print('검증 정확도' , logr.score(X_test , y_test))

x_min = X_test.iloc[:,0].min() - 0.5 # x축 최소/최대
x_max = X_test.iloc[:,0].max() + 0.5

y_min = X_test.iloc[:,1].min() - 0.5  # y축 최소/최대
y_max = X_test.iloc[:,1].max() + 0.5

xx , yy = np.meshgrid(np.arange(x_min, x_max, 0.02) , np.arange(y_min, y_max, 0.02))
# 예측값으로 이용할 데이터 범위 지정

results = logr.predict(np.c_[xx.ravel(), yy.ravel() ])
# 데이터 범위를 이용해서 예측값 조사

results = results.reshape(xx.shape)
plt.pcolormesh(xx,yy,results, cmap= plt.cm.Set1)
# https://matplotlib.org/examples/color/colormaps_reference.html  / ref. cmap
# 예측값에 따라 적절한 색상을 지정

plt.scatter(X_test.iloc[:,0], X_test.iloc[:,1], c= y_test , cmap=plt.cm.Paired , edgecolors= 'k')



plt.show()
