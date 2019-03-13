import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pandasql import sqldf


mpl.rcParams['font.family'] = 'Yj TEUNTEUN Bold'
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 10


# # seaborn에서 제공하는 데이터 셋 - 행성planet
# # 천문학자가 다른별(외행성) 주변에서 발견한 행성 정보
# planets = sns.load_dataset('planets')
#
# print('행성정보\n',planets.keys())
# # print('행성정보\n',planets.describe())
# print('행성정보\n',planets.head())
# print('행성정보\n',planets.tail())
# # print('행성정보\n',planets.count())


# 연도별 발견한 생성수 집계
# years = planets.pivot_table(index=['year'],
#                             aggfunc={'year':'count'})
# print(years)

# planet = planets.groupby('year').sum()
# planet = planets.groupby('year')['number'].sum()
# print('연도별 발견 행성 수 \n',planet)



# 연도별 발견방법(method)별 발견한 행성수 집계

# years = planets.pivot_table(index=['year','method'],
#                             aggfunc={'year':'count'})
# print(years)

# planet = planets.groupby(['year','method'])['number'].sum()
# planet = planets.groupby(['year','method'])['number'].count()
# print('연도별 발견 행성 수 \n',planet)



# 행성데이터를 5년 주기로 발견된 행성 수 조회
# planets['decade5'] = 5*(planets['year']//5)
# planet = planets.groupby('decade5')['number'].count()
# print(planet)
#
#
# planet = planets.pivot_table(index=['decade5'],
#                              aggfunc={'number':'count'})
# print(planet)



# # 행성데이터를 10년 주기로 발견된 행성 수 조회
# planets['decade10'] = 10*(planets['year']//10)
# planet = planets.groupby('decade10')['number'].count()
# print(planet)
#
# planet = planets.pivot_table(aggfunc={'number':'count'},
#                              index=['decade10'])
# print(planet)
#
#
#
#
# # pandasql로 조회
# planets2 = pd.DataFrame(planets)
#
# sql1 = 'select * from planets2 where year = 2010'
# print(sqldf(sql1))


# 문자열을 날짜로 변경하기
# dates = np.array(['2018-12-01 11:35:13 PM',
#                   '2018-08-15 10:27:35 AM',
#                   '2018-12-25 07:25:01 PM',
#                   '2018-12-32 13:25:99 PM'])
#
# for i in range(len(dates)):
#     print(pd.to_datetime(dates[i], errors='coerce',
#                          format='%Y-%m-%d %I:%M:%S %p'))


# # 시계열 데이터 생성하기
df = pd.DataFrame()
#
# # pd.date_range(시작일, 기간, 단위)
df['dates'] = pd.date_range('2001-01-01',periods=100,freq='30T') # M(월),D(일),T(분),H(시),W(주),S(초)
# print(df)
# print(df['dates'].dt.year)
# print(df['dates'].dt.month)
# print(df['dates'].dt.day)
# # print(df['dates'].dt.hour)
# # print(df['dates'].dt.minute)


# # 2001-01-02 12:00 ~ 2001-01-02 19:00 조회
# print(df[(df['dates'] >= '2001-01-02 12:00:00') & (df['dates'] >= '2001-01-02 19:00:00')])

# dates 컬럼을 index 컬럼으로 생성
df = df.set_index(df['dates'])
print(df.loc['2001-01-02 12:00:00':'2001-01-02 19:00:00'])
# print(df.ix['2001-01-02 12:00:00':'2001-01-02 19:00:00'])


# 날짜 계산하기
# 문자열을 Timestamp 함수에 적용하면 바로 날짜형으로 변환
df = pd.DataFrame()

df['도착'] = [pd.Timestamp('2018-12-01'),
            pd.Timestamp('2018-12-05')]

df['출발'] = [pd.Timestamp('2018-12-01'),
            pd.Timestamp('2018-12-09')]

print('여행기간', df['출발'] - df['도착'])