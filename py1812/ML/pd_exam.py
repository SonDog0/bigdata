import numpy as np
import pandas as pd

# ex) titanic 데이터셋
# 생존자 수 확인

pd.set_option('display.expand_frame_repr' , False)

titanic = pd.read_csv('c:/Java/data/titanic.csv')

print(titanic.head(10))

# 데이터프레임에 새로운 항목 추가

titan = pd.DataFrame()

titan['Name'] = ['혜교','지현']
titan['Age'] = [38,25]
titan['Sex'] = ['femail','femail']

print(titan.head(10))

person = pd.Series(['수지' , 23 , 'femail' ], index=['Name','Age','Sex'])

titan.append(person,ignore_index=True)

print(titan.head(10))

# 타이타닉 데이터 구조 파악

print('데이터 구조 파악 (행,열)\n',titanic.shape)
print('기술적 통계 파악\n' , titanic.describe())

# 타이타닉 데이터 중 첫번째 승객 정보 출력
print('1번째 승객 정보1\n', titanic[:1])
print('1번째 승객 정보2\n', titanic.iloc[0])

titanic = titanic.set_index(titanic['Name'])
print('1번째 승객 정보3\n', titanic.loc['Braund, Mr. Owen Harris'])

print('5~10번째 승객정보\n' , titanic.iloc[4:10])

# 조건검색하기

print('생존여부\n' , (titanic['Survived'] == 1).head(5) )

print('생존여부\n' , (titanic[titanic['Survived'] == 1]).head(5))

print('남자 승객 생존 여부 \n' , ((titanic['Survived'] == 1) & (titanic['Sex'] == 'mail')).head(20))

print('25세 이상 여자 승객 생존 여부\n' , titanic[ (titanic['Age'] > 25) & (titanic['Survived'] == 1)  & (titanic['Sex'] =='female')][ ['Age','Sex','Survived'] ])

# 데이터프레임에 새로운 항목 추가

titan = pd.DataFrame()

titan['Name'] = ['혜교','지현']
titan['Age'] = [38,25]
titan['Sex'] = ['femail','femail']

print(titan.head(10))

person = pd.Series(['수지' , 23 , 'femail' ], index=['Name','Age','Sex'])

titan.append(person,ignore_index=True)

print(titan.head(10))


nums= [10,20,30,40,50]
idx=['a','b','c','d','e']

df = pd.DataFrame(nums,idx)

print(df)

# 열 추기 하기

floats = [1.5,2.5,3.5,4.5,5.5]
df['floats'] = floats
print('수정된 데이터 프레임 \n ', df)

# 컬럼명 수정하기
df.columns =['ints','floats']
print('수정된 데이터 프레임 \n ', df)

# 행 추가하기
df = df.append({'ints' : 60 , 'floats' : 6.5} , ignore_index=True)
print('수정된 데이터 프레임 \n ', df)
df = df.append(pd.DataFrame( {'ints' : 60 , 'floats' : 7.5} , index=[6,] ))
print('수정된 데이터 프레임 \n ', df)

# 데이터프레임 합치기 - join
# 두 데이터 프레임을 합치는 기준은 index
# index가 없는 데이터를 합치는 경우 NaN으로 저장

df.index = ['a','b','c','d','e','f','g']
print('수정된 데이터 프레임 \n ', df)

# 조인할 데이터 프레임 생성
df2 = pd.DataFrame([1,4,9,16,25] , index= ['a','b','x','y','z'] , columns=['newOne'])
print(df2)

# index가 같지않으면 NaN값으로 초기화
df3 = df.join(df2)
print(df3)

# 일치하는 인덱스 위주
df3 = df.join(df2,how='inner')
print('innerjoin_DF\n', df3)

# 일치하지 않는 인덱스 위주
df3 = df.join(df2,how='outer')
print('outerjoin_DF\n',df3)

# left join
df4 = df.join(df2,how='left')
print('leftjoin_DF\n',df4)


# 데이터프레임 시각화
# 데이터프레임의 데이터를 이용해서 간단한 그래프 생성
# matplotlib의 plot함수를 데이터프레임에 내장시켜
# 언제든 그래프를 그릴수 있게 해 줌

data1 = [10,20,30,40,50]
data2 = [1.5,2.5,3.5,4.5,5.5]
idx = np.arange(1,6)
# idx = ['a','b','c','d','e']

data = pd.DataFrame(data1, index = idx)
data.columns = ['int']
data['float'] = data2
print('#####')
print(data.loc[1])

# 데이터프레임.plot.그래프유형
#
import matplotlib.pyplot as plt
# data.plot()
# data.plot.bar()
# data.plot.box()
# data.plot.pie(x='int' , y = 'float')
# data.plot.scatter(x = 'int' ,y = 'float') #산점도


# 데이터셋을 이용한 시각화하기
from sklearn import datasets

iris = datasets.load_iris()
df_iris = pd.DataFrame(iris.data,columns=iris.feature_names)
print(df_iris)

df_iris.plot.scatter(x='petal length (cm)',y= 'petal width (cm)')

#
df_iris.plot.scatter(x='sepal length (cm)', y = 'sepal width (cm)')
plt.show()