from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
son = pd.read_csv('c:/java/ddrdata/Regression.csv')

target = son.iloc[:,0]
data = son.iloc[:,1:9]

X_train, X_test , y_train , y_test = train_test_split(data, target , random_state= 0)


log = LogisticRegression(solver='liblinear')
clf = log.fit(X_train , y_train)

print('훈련정확도' , log.score(X_train , y_train))
print('검증정확도' , log.score(X_test , y_test))
