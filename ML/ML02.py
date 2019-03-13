import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mglearn

# 선형회귀 : 현대통계의 꽃, 빅데이터/머신러닝의 관문
# 두 데이터 간의 상관관계를 조사해서
# 이것에 대한 선형식을 구하고
# 이 식을 예측의 도구로 활용
# y = ax + b


# 최소제곱법 : ordinary least squares OLS
# 예측값과 실제값(훈련셋에 있는 y) 사이의 평균제곱오차를
# 최소화하는 절편과 기울기를 찾는 알고리즘
# 평균제곱오차는 예측값과 실제값 사이의 차이를
# 제곱하고 더한 후 데이터 건수로 나눈 수

data, target = mglearn.datasets.make_wave(n_samples=100)

# plt.plot(data, target, 'o')
# plt.show()

# 선형회귀 그래프
# mglearn.plots.plot_linear_regression_wave()
# plt.show()


# 회귀를 위한 선형 모델 생성
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = \
   train_test_split(data, target, random_state=0)

lr = LinearRegression()
lr.fit(X_train, y_train)  # 선형모델 생성을 위한 훈련실시

print('기울기', lr.coef_)     # 가중치weight
print('절편', lr.intercept_)  # 편향bias

print('훈련 측정값 R^2', lr.score(X_train, y_train))
print('검증 측정값 R^2', lr.score(X_test, y_test))

print('예측값 확인', lr.predict(
                    np.array([[-0.11], [0.03]]) ))


# X : 피자 크기
# y : 피자 가격
# 질문 : 12인치 피자의 가격은 얼마일까?
X = np.array([[6],[8],[10],[14],[18]])
y = [7, 9, 13, 17.5, 18]

# 산점도 작성
# plt.plot(X, y, 'ro')
# plt.axis([0,25, 0,25])   # x,y 축 조정
# plt.grid(True)
# plt.show()

lr = LinearRegression()

lr.fit(X, y)    # 모델 생성
print('기울기', lr.coef_)
print('절편', lr.intercept_)
print('결정계수 R^2', lr.score(X, y))


# 선형식 그래프 그리기
# y = ax + b
# plt.plot(X, y, 'ro')
# plt.plot(X, X * lr.coef_ + lr.intercept_ )
# plt.axis([3,23, 3,23])
# plt.grid(True)
# plt.show()

# 예측하기
mypizza = np.array([[12]])
dollar = lr.predict(mypizza)

print('12인치 피자 가격', dollar)


# 배달거리에 따른 배달시간 예측
# 200m 정도 떨어진 곳에서 배달을 시키면 몇분만에 올까?
#
# baedal = pd.read_csv('c:/Java/data/baedal.txt')
#
# # print('배달거리/배달시간\n', baedal)
#
# X = baedal.iloc[:, 0][:, np.newaxis]    # 배달거리 추출
#     # 1차원 데이터를 2차원 행렬로 변환
#     # a = [1,2,3] => a[:, np.newaxis] =>
#     # a = [[1],[2],[3]]
# y = baedal.iloc[:, 1]    # 배달시간 추출
#
# # 산점도 그리기
# plt.plot(X, y, 'bo')
# plt.grid(True)
# plt.show()
#
# lr = LinearRegression()
#
# lr.fit(X, y)
#
# print('기울기 coefficent', lr.coef_)
# print('절편 interceptor', lr.intercept_)
# print('훈련 측정값 R^2', lr.score(X, y))
#
# # 선형식 그리기
# plt.plot(X, y, 'bo')
# plt.plot(X, X*lr.coef_ + lr.intercept_)
# plt.grid(True)
# plt.show()
#
# # 배달거리 200m일때 배달시간은?
# print('배달거리 200m일때 배달시간\n',
#            lr.predict(np.array([[200]])))


# 다변량 선형회귀분석
# 흡연여부와 임신주차에 따른 신생아 몸무게 예측
# 37, 흡연일때 몸무게는?
# 40, 흡연일때 몸무게는?
# 42, 금연일때 몸무게는?

mother = pd.read_csv('c:/Java/data/pregnant.txt', sep='\t')

print(mother['Smoke'][:5])

mother['Smoke'] = pd.Categorical(mother['Smoke'])
mother['Smoke'] = mother['Smoke'].cat.codes

print(mother['Smoke'][:5])


# 산점도 그리기
# plt.plot(mother['Week'], mother['Wgt'], 'go')
plt.scatter(mother['Week'], mother['Wgt'], c=mother['Smoke'])
plt.show()


# 선형회귀식 만들기
lr = LinearRegression()
Xvar = ['Week', 'Smoke']

lr.fit(mother[Xvar], mother['Wgt'])

print('기울기 coefficent', lr.coef_)
print('절편 interceptor', lr.intercept_)
print('훈련 측정값 R^2',
            lr.score(mother[Xvar], mother['Wgt']))


# 선형회귀식으로 그래프 그리기
x = np.linspace(30, 45, 100)
plt.scatter(mother['Week'], mother['Wgt'], c=mother['Smoke'])
# plt.plot(x, x*lr.coef_[0] + lr.intercept_)
                    # 임신주수에 따른 회귀식
plt.plot(x, x*lr.coef_[0] + 0 * lr.coef_[1] + lr.intercept_)
plt.plot(x, x*lr.coef_[0] + 1 * lr.coef_[1] + lr.intercept_)
           # 임신주수, 흡연여부에 따른 회귀식
plt.show()

# 37주, 흡연일때 몸무게는?
# 40주, 흡연일때 몸무게는?
# 42주, 금연일때 몸무게는?
x1 = np.array([[37, 1]])
x2 = np.array([[40, 1]])
x3 = np.array([[42, 0]])

print('37주, 흡연', lr.predict(x1))
print('40주, 흡연', lr.predict(x2))
print('42주, 금연', lr.predict(x3))



# 교호작용을 이용한 선형회귀
# 어떤 변수가 다른 변수에 의존하는 경우를 고려하는 경우
# 즉, 변수간 영향을 주고 받으면서 나타나는 반응효과를 의미
# 여기서는 임신주수와 흡연여부가 서로 영향을 주고 받음으로
# 신생아 몸무게가 달라짐을 알수 있음
# 보통 다변수 회귀분석시 고려해야 하는 사항 중 하나임

mother['weeksmoke'] = mother['Week'] * mother['Smoke']
print(mother['weeksmoke'])

lr = LinearRegression()
Xvar = ['Week','Smoke','weeksmoke']

lr.fit(mother[Xvar], mother['Wgt'])


print('기울기 coefficent', lr.coef_)
print('절편 interceptor', lr.intercept_)
print('훈련 측정값 R^2',
            lr.score(mother[Xvar], mother['Wgt']))


# 선형회귀식 그리기
# wgt = week + smoke + (week*smoke) + a
x = np.linspace(30, 45, 100)
plt.scatter(mother['Week'], mother['Wgt'], c=mother['Smoke'])
plt.plot(x, x*lr.coef_[0] + 0 * lr.coef_[1] + lr.intercept_)
plt.plot(x, x*(lr.coef_[0] + lr.coef_[2]) +
                         1 * lr.coef_[1] + lr.intercept_)
plt.show()



x1 = np.array([[37, 1, 37*1]])
x2 = np.array([[40, 1, 40*1]])
x3 = np.array([[42, 0, 42*0]])

print('37주, 흡연', lr.predict(x1))
print('40주, 흡연', lr.predict(x2))
print('42주, 금연', lr.predict(x3))

# 37주, 흡연 [2660.59315256]
# 40주, 흡연 [3089.89397191]
# 42주, 금연 [3620.63855833]

# 37주, 흡연 [2669.4996115]
# 40주, 흡연 [3086.58585859]
# 42주, 금연 [3636.55172414]






