
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
son = pd.read_csv('c:/java/ddrdata/Regression.csv')

print(son)


target = son.iloc[:,0]
print(target)

data = son.iloc[:,1:9]
print(data)


# # 회귀를 위한 선형 모델 생성
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#
X_train, X_test, y_train, y_test = \
   train_test_split(data, target, random_state=0)

# print(len(X_train))
# print(len(X_test))
# print(len(y_train))
# print(len(y_test))
#

lr = LinearRegression()
lr.fit(X_train, y_train)  # 선형모델 생성을 위한 훈련실시
#

print('기울기', lr.coef_)     # 가중치weight
print('절편', lr.intercept_)  # 편향bias
#
print('훈련 측정값 R^2', lr.score(X_train, y_train))
print('검증 측정값 R^2', lr.score(X_test, y_test))

