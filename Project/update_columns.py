# 컬럼명으로 검색해서 -> NA만들고 -> NA  ROW 삭제

import numpy as np
import pandas as pd


# pandas 입출력
pd.set_option('display.expand_frame_repr', False)
dataframe = pd.read_csv('c:/Java/data/seoul_sub.csv',
                    encoding='euc-kr')


for i in range(0,100,5):
    strr = str(i) + "~" + str(i+4) +"세"
    print(str)
    dataframe.loc[dataframe['연령별'] == strr, '연령별'] = np.nan


dataframe.loc[dataframe['연령별'] == '85세이상' , '연령별'] = np.nan
dataframe.loc[dataframe['연령별'] == '15세미만' , '연령별'] = np.nan
dataframe.loc[dataframe['연령별'] == '15~64세' , '연령별'] = np.nan
dataframe.loc[dataframe['연령별'] == '65세이상' , '연령별'] = np.nan
dataframe.loc[dataframe['연령별'] == '평균연령' , '연령별'] = np.nan
dataframe.loc[dataframe['연령별'] == '중위연령' , '연령별'] = np.nan
dataframe.loc[dataframe['연령별'] == '합계' , '연령별'] = np.nan

dataframe.dropna(axis=0,inplace=True)

print(dataframe)

dataframe.to_csv('seoul_pop.csv',sep=',' , encoding='UTF-8')
