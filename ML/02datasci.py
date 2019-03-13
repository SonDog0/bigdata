import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 미국 질병통제센터에서 수집한
# 연도별 신생아 성별 출생수 데이터
# birth.csv를 이용해서 그래프 작성

births = pd.read_csv('c:/Java/data/births.csv')

print(births.head(10))
print(births.tail(10))

# 피벗 테이블로 집계기능을 사용해서 그래프 생성

# 년도 별로 그룹핑해서 출생수로 집계( 피벗테이블 이용 )
# birth_year = births.pivot_table('births',
#                                 index='year',columns='gender',
#                                 aggfunc='sum')
#
# birth_year.plot()
# plt.show()


# # 월 별로 그룹핑해서 출생수로 집계( 피벗테이블 이용 )
# birth_month = births.pivot_table('births',
#                                 index='month',columns='gender',
#                                 aggfunc='sum')
#
# birth_month.plot()
# plt.show()


# groupby 함수를 이용한 집계 처리
# birth_year = births.groupby(['year'])['births'].sum()
# print(birth_year)
# birth_year.plot()
# plt.show()

# birth_month = births.groupby(['month'])['births'].sum()
# # print(birth_year)
# birth_month.plot()
# plt.show()


# 연도별 성별 출생수
births_M = births[births['gender'] == 'M']
births_M_year = births_M.groupby(['year'])['births'].sum()
births_M_year.plot()

births_F = births[births['gender'] == 'F']
births_F_year = births_F.groupby(['year'])['births'].sum()
births_F_year.plot()

plt.show()



