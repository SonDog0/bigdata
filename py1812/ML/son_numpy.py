import numpy as np

k = np.array([1,2,3,4,5])
print('원본',k)

k_sub = k[1:3]
print('추출한 참조본', k_sub)

k_sub[0] = 100
k_sub[1] = 200

print('수정된 참조본', k_sub )
print('원본', k )

# 유니버셜 함수 - numpy 제공하는 범용 함수
l= np.array(range(1,10))

print('합', l.sum())
print('표준편차',np.std(l))
print('평균',np.mean(l))
print('중앙값',np.median(l))
print('분산',np.var(l))
print('누적합',np.cumsum(l))

print('최대값' , np.max(l))
print('최소값' , np.min(l))

print('곱연산' , l * 2 )
print('제곱연산' , l ** 2 )
print('제곱근' , np.sqrt(l) )

m = np.array([ [1,2,3] , [4,5,6], [7,8,9] ] )
print('열 합계', m.sum(axis= 0 ) )
print('행 합계', m.sum(axis= 1 ))

# 배열 객체 채우기
# 원소의 값이 없는 배열을 만들고
# 실행중에 각 원소에 값을 하나씩 채우는 방식

o = np.zeros((3,3))
print('3x3 영행렬\n' , o)
p = np.ones((5))
print('원소가 1인 1x5벡터',p)

q = np.arange(5)
print('원소가 0부터 4까지 1x5 벡터 ', q)

# boolean indexing
# 배열의 원소를 가리키기 위해 정수 인덱스 상ㅇ
# 한편 bool 값을 이용한 인덱싱 가능
bool = [[True,False,True] , [True,False,True] , [True,False,True] ]

ba = np.array(bool)
print(m[ba])

# 구조화 배열 - 데이터베이스 테이블과 유사
# 즉, 각 열마다 다른 자료형을 사용할 수 잇게 해 줌
schema = np.dtype([('name','S10') ,('age','i4'), ('height' ,'f') ])
data = np.array( [('smith',39,175.1) , ('darwin' , 10,120) ] ,dtype = schema )

print('스키마가 정의 된 배열' ,data)
print('이름만 츨력', data['name'])
print('darwin의 나이 출력', data[1]['age'])

schema = np.dtype([('name' , 'U10')])
data = np.array([('혜교')] , dtype = schema)
print(data)

# 개인정보가 저장된 벡터를 이용해서
# 구조화 배열 생성하기
name =['alice', 'bob', 'cathy' , 'doun' ,'hue']
age = [25,45,37,19,65]
weight = [55.5,85.2,61.2,61.5,120]

schema = {'names' : ('name', 'age','weight'),
          'formats' : ('U10' , 'i4','f4')}

personal = np.zeros(5 , dtype= schema)

print(personal)

personal['name'] = name
personal['age'] = age
personal['weight'] = weight

print(personal)

print('1행만 출력' ,personal[0])
print('이름만 출력' ,personal['name'])
print('나이가 30보다 작은 사람만 출력' ,personal['age'] <  30)
print('나이가 30보다 작은 사람만 출력' ,personal[personal['age'] <  30] ['name'])

# 배열의 크기 / 구조변형 - reshape
# 만들어진 배열의 데이터는 유지하면서 형태를 변경

origin = np.array([[1,1,1,1] , [2,2,2,2] , [3,3,3,3]] )

print(origin)


# 3x4 행렬을 6x2 행렬로 변환
transform = origin.reshape(6,2)
print(transform)

transform = origin.reshape(4,3)
print(transform)

transform = origin.reshape(12,1)
print(transform)

transform = origin.reshape(1,12)
print(transform)

origin = np.arange(12)
transform = origin.reshape(3,4 )
print(transform)

# -1 넣으면 자동으로 계산
transform = origin.reshape(4,-1 )
print(transform)

# 전치행렬 t - 행렬의 축을 바꿈

origin = np.arange(1,16)
transform = origin.reshape(3,5)
print('3x5 행렬 \n' , transform)
# broadcasting

transform  = np.transpose(origin.reshape(3,5))
print('전치 5x3 행렬 \n' , transform)


# broadcasting - 두 배열 합치기
# 일반적으로 두개의 행렬을 연산하는 경우
# 각행렬의 크기는 서로 같아야함
# 한편, numpy에서는 서로 다른 크기를 가진 행렬간 연산 가능
# 이때, 크기가 작은 행렬을 자동으로 확장(broadcast) 해서
# 행렬의 크기를 맞춰주기 때문
# 파이썬의 리스트와 확연히 구분되는 기능

# 브로드캐스팅 연산 가능한 3가지 경우
# m x n 배열과 m x 1 배열
# m x n 배열과 1 x n 배열
# m x 1 배열과 1 x n 배열

a = np.array([[0,0,0] , [10,10,10] , [20,20,20] ,[30,30,30] ])
b = np.array([[0,1,2] , [0,1,2] , [0,1,2] , [0,1,2] ])
c = np.array([ 0,1,2 ] )
d = np.array([ [0],[10],[20],[30] ])

print(a)
print(b)
print(c)
print(d)

e =  a  +b
print('a+b 값\n',e)

e = a + c
print('a+c값\n',e)

e = a + d
print('a+d값\n',e)

e = c + d
print('c+d값\n',e)

e = a + 5
print('a + 5\n' , e )

# numpy로 생성된 배열중
# 1차원은 벡터 vector
# 2차원은 행렬 matrix
# 3차원은 텐서 tensor

# ! 배열을 부분적으로 slice로 한 결과는
# 원본 배열의 복사본이 아니고 참조본임
# 따라서, 참조본을 수정하면 원본에도 영향을 미침

