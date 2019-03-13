# Big Mart Sales 데이터 셋을 이용한 회귀분석
# 상품의 특징 (weight, fat content, type, mrp)
# 매장의 특징 (year, size, location, type)

# 상품무게별 평균 판매량
# 상품가격mrp별 평균 판매량
# 매장크기별 평균 판매량
# 지역별 평균 판매량

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.expand_frame_repr', False)

bigmart = pd.read_csv('c:/Java/data/bigmartsales1.txt')

# print(bigmart.head())


# 결측치 조사 및 처리
print(bigmart.isnull().sum())

bigmart.dropna(inplace=True)

print(bigmart.isnull().sum())


# 산점도 확인
# plt.scatter(bigmart['Item_Weight'],
#             bigmart['Item_Outlet_Sales'])
# plt.show()
#
# plt.scatter(bigmart['Item_MRP'],
#             bigmart['Item_Outlet_Sales'])
# plt.show()


# 선형회귀 모델 생성 1
data1 = bigmart['Item_Weight'][:, np.newaxis]
data2 = bigmart['Item_MRP'][:, np.newaxis]


target = bigmart['Item_Outlet_Sales']

X_train, X_test, y_train, y_test = \
    train_test_split(data1, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

# print('훈련 정확도', lr.score( X_train, y_train))
# print('검증 정확도', lr.score( X_test, y_test))

print('훈련 정확도', '%.5f' % lr.score( X_train, y_train))
print('검증 정확도', '%.5f' % lr.score( X_test, y_test))

print('기울기,절편', lr.coef_, lr.intercept_)


# 선형회귀직선 그려보기
# plt.scatter(bigmart['Item_Weight'],
#             bigmart['Item_Outlet_Sales'])
# x = np.linspace(3, 23, 100)
# plt.plot(x, x*lr.coef_ + lr.intercept_, 'r')
# plt.show()


# 선형회귀 모델 생성 2
X_train, X_test, y_train, y_test = \
       train_test_split(data2, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 선형회귀직선 그리기
# plt.scatter(bigmart['Item_MRP'], bigmart['Item_Outlet_Sales'])
# x = np.linspace(25,275,100)
# plt.plot(x, x*lr.coef_ + lr.intercept_, 'r')
# plt.show()


# 선형회귀 모델 생성 3
bigmart['Outlet_Size'] = pd.Categorical(bigmart['Outlet_Size'])
bigmart['Outlet_Size'] = bigmart['Outlet_Size'].cat.codes

data3 = bigmart['Outlet_Size'][:, np.newaxis]

X_train, X_test, y_train, y_test = \
    train_test_split(data3, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 선형회귀 모델 생성 4 - 지역별
bigmart['Outlet_Location_Type'] = pd.Categorical(bigmart['Outlet_Location_Type'])
bigmart['Outlet_Location_Type'] = bigmart['Outlet_Location_Type'].cat.codes

data4 = bigmart['Outlet_Location_Type'][:, np.newaxis]

X_train, X_test, y_train, y_test = \
    train_test_split(data4, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 선형회귀 모델 생성 5 - 종류별
bigmart['Outlet_Type'] = pd.Categorical(bigmart['Outlet_Type'])
bigmart['Outlet_Type'] = bigmart['Outlet_Type'].cat.codes

data5 = bigmart['Outlet_Type'][:, np.newaxis]

X_train, X_test, y_train, y_test = \
    train_test_split(data5, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 선형회귀 모델 생성 6 - 상품특성 모두
bigmart['Item_Fat_Content'] = pd.Categorical(bigmart['Item_Fat_Content'])
bigmart['Item_Fat_Content'] = bigmart['Item_Fat_Content'].cat.codes

bigmart['Item_Type'] = pd.Categorical(bigmart['Item_Type'])
bigmart['Item_Type'] = bigmart['Item_Type'].cat.codes

bigmart['Item_Identifier'] = pd.Categorical(bigmart['Item_Identifier'])
bigmart['Item_Identifier'] = bigmart['Item_Identifier'].cat.codes

data6 = bigmart.ix[:, ['Item_Weight','Item_Fat_Content',
            'Item_Visibility','Item_Type','Item_MRP']]

X_train, X_test, y_train, y_test = \
       train_test_split(data6, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 각 특성이 회귀분석 영향을 미치는 정도
col = ['Item_Weight','Item_Fat_Content',
            'Item_Visibility','Item_Type','Item_MRP']
coef = pd.Series(lr.coef_, col).sort_values()
coef.plot(kind='bar')
plt.show()



# 선형회귀 모델 생성 7 - 매장특성 모두
data7 = bigmart.ix[:, ['Outlet_Establishment_Year',
            'Outlet_Size','Outlet_Location_Type',
            'Outlet_Type']]

X_train, X_test, y_train, y_test = \
       train_test_split(data7, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 각 특성이 회귀분석 영향을 미치는 정도
col = ['Outlet_Establishment_Year',
            'Outlet_Size','Outlet_Location_Type',
            'Outlet_Type']
coef = pd.Series(lr.coef_, col).sort_values()
coef.plot(kind='bar')
plt.show()


# 선형회귀 모델 생성 8 - 상품/매장 특성 모두
bigmart['Item_Identifier'] = pd.Categorical(bigmart['Item_Identifier'])
bigmart['Item_Identifier'] = bigmart['Item_Identifier'].cat.codes

bigmart['Outlet_Identifier'] = pd.Categorical(bigmart['Outlet_Identifier'])
bigmart['Outlet_Identifier'] = bigmart['Outlet_Identifier'].cat.codes

data8 = bigmart.iloc[:, 0:10]

X_train, X_test, y_train, y_test = \
       train_test_split(data8, target, random_state=0)

lr = LinearRegression()

lr.fit(X_train, y_train)

print('훈련 정확도', lr.score( X_train, y_train))
print('검증 정확도', lr.score( X_test, y_test))
print(['기울기,절편', lr.coef_, lr.intercept_])


# 편향bais vs 분산variance
# 편향 : 학습 알고리즘에서 발생되는 오차의 정도
# 적당히 낮은 편향 - 과적합
# 너무 높은 편향 - 미적합

# 분산 : 데이터셋에 포함된 변동성 여부
# 적당히 낮은 분산 - 노이즈noise가 적음
# 너무 높은 분산 - 노이즈가 많음

# 학습 알고리즘 상에서 기대 오차를 분석하는 한가지 방법으로
# 편향, 분산을 내제하고 있는 데이터는 어떤 모델링으로
# 줄일 수 없는 오류의 총합으로 여김
# 따라서, 편향, 분산의 trade-off를 이해해서
# 적절한 학습의 효과가 나도록 데이터 셋의 특성을 잘 조합해야 함


# 리지, 라쏘 회귀
# 가중치에 제약조건을 설정해서 회귀를 구하는 알고리즘
# 이를 통해 모델의 복잡도를 다소 낮춰 적정한 편향,분산 통해
# 적절한 회귀분석 모델을 구함

# 일반적인 회귀분석 : 회귀계수(절편,기울기) 추정량 구함
# 잔차의 제곱합을 최소로 하는 최소제곱법 사용

# 실제 회귀모델은 단일 변수가 아닌 다중변수가 많음
# 설명변수 증가 => 변수간 강한 상관관계 => 다중공선성 문제발생
# => 최소제곱법을 이용한 회귀계수 추정량 커짐 => 정확도 저하

# 따라서, 중요한 변수를 선정하고, 중요하지 않은 변수는 제외
# => feature selection (: 변수 소거와는 다름)
# 중요하지 않은 변수에 해당하는 coef의 절대값을 낮춤

# 라쏘 회귀 (L1-norm 패널티)
# 원래의 최소제곱법에 제약을 가함
# 중요하지 않은 변수의 회귀계수는 축소 => 0으로 지정
# 기울기를 완전히 줄여 특정 특성이 모델에 주는 영향을 제외시킴


# 리지 회귀 (L2-norm 패널티)
# 원래의 최소제곱법에 제약을 가함
# 중요하지 않은 변수의 회귀계수는 축소 => 0에 가깝게 지정
# 기울기를 줄여 특정 특성이 모델에 주는 영향을 축소시킴


# 엘라스틱넷 회귀
# 라쏘회귀와 리지회귀의 제약을 합친 회귀모형



# 리지 회귀
from sklearn.linear_model import Ridge, Lasso

X_train, X_test, y_train, y_test = \
       train_test_split(data6, target, random_state=0)

lrR = Ridge()
lrR.fit(X_train, y_train)


print('릿지 훈련 정확도', lrR.score(X_train, y_train))
print('릿지 검증 정확도', lrR.score(X_train, y_train))


# alpha : 특정 특성의 영향을 어느 정도
# 제외시킬 것인지 그 비율을 지정하는 변수
# 값이 낮으면 모델의 복잡도가 증가 (특성수 증가) - 성능개선

# alpha = 0.1
lrR = Ridge(alpha=0.1)
lrR.fit(X_train, y_train)

print('릿지 훈련 정확도 (a=0.1)', lrR.score(X_train, y_train))
print('릿지 검증 정확도 (a=0.1)', lrR.score(X_train, y_train))
print('사용한 특성수', np.sum(lrR.coef_ != 0) )


# alpha = 0.01
lrR = Ridge(alpha=0.01)
lrR.fit(X_train, y_train)

print('릿지 훈련 정확도 (a=0.01)', lrR.score(X_train, y_train))
print('릿지 검증 정확도 (a=0.01)', lrR.score(X_train, y_train))
print('사용한 특성수', np.sum(lrR.coef_ != 0) )

# alpha = 0.3
lrR = Ridge(alpha=0.3)
lrR.fit(X_train, y_train)

print('릿지 훈련 정확도 (a=0.3)', lrR.score(X_train, y_train))
print('릿지 검증 정확도 (a=0.3)', lrR.score(X_train, y_train))
print('사용한 특성수', np.sum(lrR.coef_ != 0) )



# 라쏘 회귀
from sklearn.linear_model import Lasso

X_train, X_test, y_train, y_test = \
       train_test_split(data6, target, random_state=0)

lrL = Lasso()
lrL.fit(X_train, y_train)

print('라쏘 훈련 정확도', lrL.score(X_train, y_train))
print('라쏘 검증 정확도', lrL.score(X_train, y_train))


# alpha = 0.1
lrL = Lasso(alpha=0.1)
lrL.fit(X_train, y_train)

print('라쏘 훈련 정확도 (a=0.1)', lrL.score(X_train, y_train))
print('라쏘 검증 정확도 (a=0.1)', lrL.score(X_train, y_train))
print('사용한 특성수', np.sum(lrL.coef_ != 0) )


# alpha = 0.01
lrL = Lasso(alpha=0.01)
lrL.fit(X_train, y_train)

print('라쏘 훈련 정확도 (a=0.01)', lrL.score(X_train, y_train))
print('라쏘 검증 정확도 (a=0.01)', lrL.score(X_train, y_train))
print('사용한 특성수', np.sum(lrL.coef_ != 0) )

# alpha = 0.3
lrL = Lasso(alpha=0.3)
lrL.fit(X_train, y_train)

print('라쏘 훈련 정확도 (a=0.3)', lrL.score(X_train, y_train))
print('라쏘 검증 정확도 (a=0.3)', lrL.score(X_train, y_train))
print('사용한 특성수', np.sum(lrL.coef_ != 0) )





