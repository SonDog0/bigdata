# pandas
# 행에 '열 레이블index'를 부착한 다차원 행렬인
# 데이터프레임 자료구조를 제공하는 패키지
# 핵심요소는 dataframe, series 시계열, index 지수

# pandas 의 창시자 중 한명은 해지펀드 애널리스트로 일하며
# 파이썬에서 금융 시계열 자료를 다루기 위한 목적으로 개발

# numpy 기반 행렬은 산술연산에 적합한 자료구조
# pandas는 numpy 행렬을 대상으로 data muging / wrangling
# 시간을 줄여주는 효과가있음

# data muging/wrangling : data prepreocessing
# 원 origin 자료를 또 다른 형태의 자료로 변환하거나
# 매핑하는 작업을 의미

import numpy as np
import pandas as pd

# 가단한 시계열 자료 생성
# 시간적 흐름에 따라 기록한 데이터
# 통계량의 변화가 시간의 움직임에 따라 발생함
a = pd.Series([0.0,0.25,0.5,0.75,1.0])
print('시계열자료\n' , a )
print('시계열자료값\n' , a.values )
print('시계열자료\n' , a.index)
print('시계열 2번자료\n', a[2])
print('시계열 3,4번자료\n', a[3] , a[4])

b = pd.Series([1.0,1.25,1.5,1.75,2.0] , index = ['a' ,'b','c','d','e'])


print('시계열자료\n' , b )
print('시계열자료값\n' , b.values )
print('시계열자료\n' , b.index)
print('시계열 2번자료\n', b['b'])
print('시계열 3,4번자료\n',b['c':'d'] )

# pandas에서 정수형 인덱스를 사용하는 경우
# 파이썬의 slice연산과 혼동 될 위험이 존재
# 따라서, pandas만의 특별한 인덱서indexer 기능 제공
print('####################################')

c = pd.Series(['a','b','c','d','e'] , index = [1,3,5,7,9])

print('1번 데이터\n' , c[1])
print('2~3번 데이터 ',c.loc[2:4]) # pandas indexer
print('2~3번 데이터 ',c.iloc[2:4]) # python indexer

# 간단한 데이터프레임 자료 생성
# 파이썬 딕셔너리의 특수한 형태
# 시계열이 인덱스를 가진 1차원 배열이라면(벡터)
# 데이터프레임은 행과 열이름을 가진 2차원 배열(행렬)

area = {'seoul' : 423967,
        'pusan' : 170312,
        'deajeon' : 149995,
        'inchoun' : 141297,
        'kwangju' : 120163}

pop = {'seoul' : 38332521,
        'pusan' : 26448193,
        'deajeon' : 19651127,
        'inchoun' : 19552860,
        'kwangju' : 12882135}

states = pd.DataFrame({'pop' : pop , 'area' : area})

print('지역정보\n' , states)
print('면적정보\n' , states.area)
print('지역정보 인덱스\n' , states.index)
print('지역정보 컬럼\n' , states.columns)

# 리더십 데이터를 pandas DF로 생성하기
data = { 'manager' : [1,2,3,4,5] ,
         'date' : ['10/24/14','10/28/14','10/01/14','10/12/14','05/01/14'],
         'country' : ['US','US','US','UK','UK'],
         'gender' : ['M','F','F','M','F'],
         'age':[32,45,25,39,99],
         'q1':[5,4,5,5,5],
         'q2' : [3,5,2,5,5],
         'q3' : [3,5,5,5,2],
         'q4' : [3,3,4,0,0],
         'q5' : [2,2,1,2,1,] }

idx = np.arange(1,6)
leadership = pd.DataFrame(data, index=idx)
print('리더십 데이터프레임 \n', leadership)

print('나이컬럼 : \n' , leadership.age)
print('질문 컬럼 : \n' , leadership.iloc[:,5:10] )
print('질문 컬럼 : \n' , leadership.loc[:,'q1':'q5'])

# ex )
print('#############################')
df = pd.DataFrame(np.arange(1,26).reshape(5,5) , index= list('abcde'), columns=['x','y','z','10','20'])

print(df)

print('a,b,c,행 10,20열 출력 \n',df.iloc[0:3,:])

