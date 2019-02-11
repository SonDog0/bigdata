# 컴프리헨션 - 반복문 축약
# 파이썬에는 4가지 종류의 컴프리헨션 지원
# list(py2), set(py2), dict(py3), generator(py3)
# 다양한 데이터 객체에 사용되는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능

# 리스트에 적용하는 컴프리헨션
# 1~10의 정수를 리스트에 저장
numlist=[]
for i in range(1,11) :
    numlist.append(i)
print(numlist)

# for 축약문
# [ 표현식 for 항목 in 반복가능객체]
numlist2=[i for i in range(1,11)]   # 오른쪽에서 왼쪽으로 읽으면 쉬움
print(numlist2)

# ex) 0~ 20사이 짝수를 리스트로 생성
evens=[2*i for i in range(0,11)]
print(evens)

# ex)1~10까지 제곱을 구한 겨로가를 리스트로 생성
squares=[i**2 for i in range(1,11)]
squares=[i*i for i in range(1,11)]
print(squares)

# ex) 다음리스트의 값을 이용해 제곱값을 리스트로 생성
val = [1,2,'A',False,9,100]
# squares2=[v**2 for v in val]   # 오류
# squares2=[v*v for v in val]    # 문자, bool형은 산술연산 불가
# print(squares2)
#
# 조건을 이용한 한술연산
val = [1,2,'A',False,9,100]
squares2=[]
for v in val:
    if (type(v) == int) :
        squares2.append(v**2)
print(squares2)
#
#
# for if 축약문
# [ 표현식 for 항목 in 반복가능객체 if 조건]
val = [1,2,'A',False,9,100]
squares2=[v**2 for v in val if type(v)==int]
print(squares2)
#
#
# # ex) 1~ 50 사이 홀수
# a=[i for i in range(1,51) if i % 2 != 0]
# print(a)
#

# ex) 1~100 제곱수가 아닌 수 - sqrt()함수 사용 - 안맞음
from math import sqrt
# b=[i for i in range(1,101) if sqrt(i) % 1 == 0 ]
b=[i for i in range(1,101) if sqrt(i) % 1 != 0 ]
print(b)

#
# # 다중조건을 사용하는 for 축약문
# # [표현식1 if 조건1 else 표현식2 for 항목 in 반복가능객체]
#
# ex) 1 ~ 100 이하 중 짝수면 even, 홀수면 odd로 구분해서 리스트에 저장
evenodd = ['even' if i%2 == 0 else 'odd' for i in range(1,101)]
print(evenodd)

#
# 중첩 for 문을 사용하는 for 축약문
# [표현식 for 항목1 in 반복가능객체1 for 항목2 in 반복가능객체2]
gugudan = []
for i in range(7,9) :
    for j in range(1,10):
        gugudan.append(i*j)
print(gugudan)

gugu78 = [i*j for i in range(7,9) for j in range(1,10)]
print(gugu78)
#
#
#
#
# 딕셔너리 for 축약문 - {}
# { 키/값 for 키, 값 in zip(반복가능객체, 반복가능객체)}
name=['혜교','지현','수지']
grd=[99,98,95]

kor = {}
# kor[name[0]] = grd[0]
# kor[name[1]] = grd[1]
# kor[name[2]] = grd[2]
# print(kor)

for i in range(len(name)):
    kor[name[i]] = grd[i]
print(kor)

kor2={key:value for key, value in zip(name,grd)}
# kor2={k:v for k, v in zip(name,grd)}
print(kor2)