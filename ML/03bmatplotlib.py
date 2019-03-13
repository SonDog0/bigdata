import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# 그래프 한글 지정
mpl.rcParams['font.family'] = 'Yj TEUNTEUN Bold'
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 10

# 그래프 스타일 지정하기
# plt.style.use('classic')  # 고전
# plt.style.use('seaborn-whitegrid')  # seaborn
# plt.style.use('fivethirtyeight')  # 강조,굵게

# plt.style.use('ggplot')  # 지지플롯
# plt.style.use('bmh')  # 해커스타일
# plt.style.use('dark_background')  # 프리젠 테이션
# plt.style.use('grayscale')  # 회색조 ...? 먹는건가?
# plt.style.use('seaborn-pastel')  # 파스텔 - 안먹는거같음
# plt.style.use('seaborn-dark')  # 어두운 색

# mpl.rcParams['font.family'] = 'Yj TEUNTEUN Bold'
# mpl.rcParams['axes.unicode_minus'] = False
# mpl.rcParams['font.size'] = 10
#
# x = np.linspace(0,10,1000)   # 지정한 구간을 구간수로 분활
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.cos(x),'r',label='코사인')
# ax.legend()
# plt.show()



# 기본 산점도
x = np.linspace(0,10,50)
y = np.sin(x)

fig = plt.figure()
ax = plt.axes()
ax.scatter(x,y)
plt.show()



# # 고급 산점도 ( 버블효과 )
# rnd = np.random.RandomState(0)
#
# x = rnd.randn(100)
# y = rnd.randn(100)
#
# colors = rnd.randn(100)
# sizes = 1000* rnd.randn(100)
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(x,y,s=sizes, alpha=0.5, c=colors)
# plt.show()


# 아이리스 데이터셋 버블차트
# x: sepal.length, y :sepal.width
# size: petal.length, color: iris.target

# from sklearn import datasets
# iris =datasets.load_iris()
# data = iris.data
#
# # print(iris.target)
#
# x = data[:,0]
# y = data[:,1]
#
# sizes = data[:,2]
#
# # colors = list(iris.target)
# # for i in range(len(colors)):
# #     if colors[i] == 0:
# #         colors[i] == 'red'
# #     elif colors[i] == 1:
# #         colors[i] == 'blue'
# #     elif colors[i] == 2 :
# #         colors[i] == 'green'
# # print(colors)
#
# colors = pd.DataFrame(iris.target)
# colors[colors == 0] = 'red'
# colors[colors == 1] = 'blue'
# colors[colors == 2] = 'green'
#
# print(colors)
#
# colors = list(colors.iloc[:,0])
# print(colors)
#
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(x,y, alpha=0.5, s=50*sizes, c=colors)
# plt.show()

# 한 화면에 여러 그래프 그리기 - subplot
# subplot 함수 인자 = 행수/열수/번호
# x1 = np.linspace(0,5)
# x2 = np.linspace(0,2)
#
# y1 = np.cos(2*np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2*np.pi * x2)

# fig = plt.figure()
# plt.subplot(211)     # 2행 1열 짜리 표 중 첫번째
# plt.plot(x1,y1,'ro--')
# plt.subplot(212)     # 2행 1열 짜리 표 중 두번째
# plt.plot(x2,y2,'b*-.')
# plt.show()


# plt.subplot(121)     # 2행 1열 짜리 표 중 첫번째
# plt.plot(x1,y1,'ro--')
# plt.subplot(122)     # 2행 1열 짜리 표 중 두번째
# plt.plot(x2,y2,'b*-.')
# plt.show()


# plt.subplot(221)     # 2행 1열 짜리 표 중 첫번째
# plt.plot(np.random.randn(5))
#
# plt.subplot(222)     # 2행 1열 짜리 표 중 첫번째
# plt.plot(np.random.randn(5))
#
# plt.subplot(223)     # 2행 1열 짜리 표 중 첫번째
# plt.plot(np.random.randn(5))
#
# plt.subplot(224)     # 2행 1열 짜리 표 중 첫번째
# plt.plot(np.random.randn(5))
#
# plt.show()



# 타이타닉 데이터 셋을 이용한 예제
# 탑승객 중 성별 생존자 비율
titanic = sns.load_dataset('titanic')
pd.set_option('display.expand_frame_repr', False)

# print('타이타닉 key \n',titanic.keys())
print('타이타닉 info \n',titanic.describe())
# print('타이타닉\n',titanic.head())
# print('타이타닉\n',titanic.tail())

# survived = titanic.groupby('sex')['survived'].mean()
# print('성별 생존자 평균 비율',survived)


# # 탑승객 중 나이별 생존자 비율
# survived = titanic.groupby('age')['survived'].mean()
# print('나이별 생존자 평균 비율',survived)


# # 탑승객 중 나이별 생존자 비율(범위지정)
# ages = pd.cut(titanic['age'], [0,15,30,50,80])
# survived = titanic.pivot_table('survived',[ages])
# print('연령별 생존자 평균 비율',survived)


# 탑승객 중 요금별 생존자 비율
# survived = titanic.groupby('fare')['survived'].mean()
# print('요금별 생존자 평균 비율',survived)

# fares = pd.cut(titanic['fare'], [0,8,15,31,515])
# survived = titanic.pivot_table('survived',[fares])
# print('요금대별 생존자 평균 비율',survived)



# 탑승객중 성별, 좌석 등급별 생존자 비율
# survived = titanic.groupby(['sex','pclass'])['survived'].mean()
# survived = titanic.groupby(['sex','pclass'])['survived'].mean().unstack()

# survived = titanic.pivot_table('survived',['sex','pclass']).unstack()
# print('성별 좌석 등급별',survived)

# 성별 나이별
# ages = pd.cut(titanic['age'],[0,15,30,50,80])
# survived = titanic.pivot_table('survived',['sex',ages]).unstack()
# print('성별 좌석 등급별',survived)


# 성별 요금 별 생존자 비율
# fares = pd.cut(titanic['fare'],[0,100,200,300,600])
# survived = titanic.pivot_table('fare',['sex',fares])
# print(survived)

# 성별, 좌석 등급별 총 생존자와 평균 요금
# survived = titanic.pivot_table(index=['sex','pclass'],
#                                aggfunc={'survived':'sum', 'fare':'mean'})
# print(survived)



# 탑승객중 성별 생존자 비율
# DataFrame만을 이용해서 처리
# print(len(titanic), titanic['sex'].count(), titanic.count())
#
# m_survied = titanic[titanic['sex']=='male']['survived'].sum()
# print(m_survied)
#
# f_survied = titanic[titanic['sex']=='female']['survived'].sum()
# print(f_survied)




# R의 데이터프레임에서 sql 질의로 조회하려면
# sqldf 패키지를 사용했음
# pandas 데이터프레임에서 sql 질의로 조회하려면
# pandasql 패키지 사용

from pandasql import sqldf

sql = 'select * from titanic'
sql2 = 'select * from titanic limit 10'
sql3 = 'select sum(survived) from titanic where sex = "male" and survived = 1'
# print(sqldf(sql))
# print(sqldf(sql2))
print(sqldf(sql3))





# iris 데이터 셋
# 데이터 프레임으로 바꾸는게 세상중요함!
from sklearn import datasets
iris = datasets.load_iris()
target = iris.target

print(iris.DESCR)

iris = pd.DataFrame(iris.data)
iris.columns=['sl','sw','pl','pw']
iris['cl'] = target



# versicolor 품종의  sepal length/width 를 출력
sql11 = 'select sl, sw from iris where cl = 1'
print(sqldf(sql11))

# setosa 품종의  sepal length/width 를 출력
sql12 = 'select sl, sw from iris where cl = 0'
print(sqldf(sql12))
