
# 그래프 한글 출력하기
import matplotlib as mpl

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 그래픽 스타일 지정하기
# x = np.linspace(0,10,1000)# 지정한 구간을 구간수로 분산 0 ~ 10 1000구간
#
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x,np.sin(x) ,'r', label = '사인')
# ax.legend()
# # plt.style.use('classic')
#
# plt.style.use('ggplot')
#
# mpl.rcParams['font.family'] = 'BM YEONSUNG'
# mpl.rcParams['axes.unicode_minus'] = False
# mpl.rcParams['font.size'] = 10
#
#
# plt.grid()  # 모눈 표시
#
# plt.show()


# 기본 산점도
# x = np.linspace(0,10,30)
# y= np.sin(x)
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(x,y)
# plt.show()


# 고급 산점도
# rnd = np.random.RandomState(0)
# x = rnd.randn(100)
# y = rnd.randn(100)
#
# colors = rnd.randn(100)
# sizes = 1000 * rnd.randn(100)
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(x,y, s=sizes , alpha=0.5, c = colors)
# plt.show()
#


# iris 데이터셋을 이용해서 버블형 산점도 작성
# s : sepal.length y : sepal.width,
# size : petal.length, color : iris.target

from sklearn import datasets

# iris = datasets.load_iris()
# data = iris.data
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(data[:,0] , data[:,1] ,s = data[:,2] , alpha=0.45 , c = iris.target
#            )
# plt.show()


# 한 화면에 여러 그래프 그리기 -subplot
# subplot 함수 인자 = 행수 / 열수 / 번호
#
# x1 = np.linspace(0,5)
# x2 = np.linspace(0,2)
#
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2 * np.pi * x2)
#
# fig = plt.figure()
# plt.subplot(211)
# plt.plot(x1,y1,'ro-')
#
# plt.show()


# 타이타닉 예제
pd.set_option('display.expand_frame_repr', False)
titanic = sns.load_dataset('titanic')
print('타이타닉', titanic.keys())
print('타이타닉 info', titanic.describe())
print('타이타닉 상위5', titanic.head())
print('타이타닉 하위5', titanic.tail())

# 탑승객중 성별 생존자 평균비율

survived = titanic.groupby('sex')['survived'].mean()
print('성별 생존자 평균 비율' , survived)

# 탑승객 중 나이별 생존자 평균 비율

survived = titanic.groupby('age')['survived'].mean()
print('나이별 생존자 평균 비율' , survived)


# 탑승객 중 나이별 생존자 평균 비율 (범위지정)
ages = pd.cut(titanic['age'],[0,15,30,50,80] )
survived = titanic.pivot_table('survived', [ages] )
print('나이대별 생존자 평균 비율' , survived)

# 탑승객 중 요금대별 생존자 평균 비율
fares = pd.cut(titanic['fare'],[0,100,300,400,550] )
survived = titanic.pivot_table('survived', [fares] )
print('요금별 생존자 평균 비율' , survived)

# 탑승객 중 성별, 좌석등급별 생존자 평균 비율
survived = titanic.groupby(['sex','pclass'])['survived'].mean().unstack()
print('성별, 좌석 등급별  생존자 평균 비율' , survived)
 ,m