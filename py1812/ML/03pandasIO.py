import numpy as np
import pandas as pd

# pandas 입출력

# 데이터파일을 읽어 데이터프레임을 생성
# csv, excel , json , ... 등등 지원

phone = pd.read_csv('C:/Java/data/phoneinfo.csv',encoding='euc-kr')

print('핸드폰 사용현황 \n ' , phone)

cols = ['yead' ,'buy',' display', 'age','height' , 'weight' , 'hptime' , 'comtime' , 'datatime' ]
idx = np.arange(1,25)

print('\n###################################################################\n')

phone = pd.read_csv('C:/Java/data/phoneinfo.csv',encoding='euc-kr' , sep = ',' , names = cols ,skiprows=1 , header=None)
phone.index = idx
# 생략될때 set_option

pd.set_option('display.max_columns',100)
print(phone)
# index_col = 0  정수형 index 쓰지않겠음

# 우편번호 데이터 불러오기

zipcode = pd.read_csv('c:/java/data/Seoul-2017.10_utf.csv' )


# 누락된 데이터 처리 : np.nan
zipcode['읍면'] = zipcode['읍면'].replace(np.nan,'')
zipcode['리명'] = zipcode['리명'].replace(np.nan,'')


# 누락된 데이터처리 2 : fillna


zipcode.fillna('', inplace = True)

print(zipcode)

# 누락된 데이터 다루기 - null ,NaN , NA ,None
# 파이썬/pandas 에서는 NaN(float) 또는 None(object) 으로 취급
# 정수형 누락값인 NA는 pandas 에서 취급불가

val1= np.array([1,2,None,4,5])
print(val1 , val1.dtype)
print('\n###################################################################\n')

val2 = np.array([1,2,np.nan,4,5])
print(val2  , val2.dtype)
print('\n###################################################################\n')

val3 = pd.Series([1,2,np.nan , 4 , None])
print(val3.sum() , val3.dtype)
# pandas 시계열에서는 누락값 ( np.nan , none) 뺴고 연산이됨 ..!
print('\n###################################################################\n')

# null값 다루기
# pandas 자료구조에서는 널값을 감지하고 삭제하는 기능 제공

val4 = pd.Series([1,2,np.nan , 4 , None])

print('널값 출력\n' , val4.isnull())
print('정상값 출력1\n' , val4[val4.notnull()])
print('정상값 출력2\n' , val4[~val4.isnull()])
print('널값 제거\n' , val4.dropna())
print('\n###################################################################\n')


val5 = pd.DataFrame( [[1,np.nan,3] ,
                     [np.nan,8,10],
                     [15,20,18]] )

print('널값 출력 \n' ,val5.isnull())
print('정상값 출력1\n' , val5[val5.notnull()])
print('널값 제거1\n' , val5.dropna())

print('널값 제거2\n' , val5.dropna(axis= 0))

# 데이터프레임에서 dropna()를 사용하면
# 행 기준으로 null이 삭제됨

# axis = 1 값을 지정하면 열기준으로 null이 삭제됨


#널값을 다른 값으로 대체하기 - fillna
print('널값 대체하기1\n', val4.fillna('a'))
print('널값 대체하기2\n' , val5.fillna('0'))



# 앞 , 뒤값으로 대체하기
print('열 기준 앞값으로 널값 대체하기 1 \n' , val4.fillna(method='ffill', axis= 0))
print('열 기준 뒤값으로 널값 대체하기 1 \n' , val4.fillna(method='bfill', axis= 0))

print('행 기준 앞값으로 널값 대체\n ' ,val5.fillna(method ='ffill' ,axis=1))
print('행 기준 뒤값으로 널값 대체\n ' ,val5.fillna(method ='bfill' ,axis=1))