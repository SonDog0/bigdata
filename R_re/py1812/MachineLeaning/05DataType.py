"""
파이썬 고급 자료형
파이썬은 기본적으로 숫자/문자 자료형을 제공
하지만, 이것만으로는 프로그래밍 하기에 부족함
이런 불편함을 해소하기 위해 리스트, 튜플, 사전,집합
자료형을 제공함
"""

"""
리스트 자료형
순차적 데이터를 관리하는 자료구조
다른 언어의 배열과는 달리
서로 다른 자료형의 데이터를 함께 다룰 수 있음
"""

# 리스트의 각 요소는 []를 사용해서 접근
msg = 'Hello, World!!'         # 문자열 정의
print(msg[0],msg[len(msg)-1])  # 문자열의 첫번째와 마지막 글자 출력
# => 문자는 문자열의 부분집합 => 리스트 형태로 접근 가능

# 파이썬에서는 자료형을 변수명 뒤에
list1_list = []                    # 빈 리스트
list2_list = [1,2,3,4,5]           # 정수 리스트
list3_list = ['a','b','c','d']     # 문자 리스트
list4_list = [1,2,3,'a','b','c']   # 혼합 리스트
print(list4_list)

# 리스트를 이요한 간단한 연산
# 요소 존재여부 파악 : in/not in
print(1 in list1_list)


# 길이 연산 : len()
print(len(list4_list))

# 특정값 참조 : [인덱스]
print(msg[3])
print(list4_list[5])


# 주민번호에서 성별 여부 판별
jumin1='123456-1234567'
jumin2=[1,2,3,4,5,6,2,3,4,5,6,7,8]

if jumin1[7] == '1':
    print('남자')
else :
    print('여자')

if jumin2[6] == 1 :
    print('남자')
else :
    print('여자')

# 주민번호에서 생년월일 추출
for i in range(0,6):
    print(jumin1[i], end='')

# 특정범위 내 요소들을 추출할 때는 slice 사용
# [l:j:step]
print(jumin1[0:6])
print(jumin1[:6])
print(jumin1[7:])             # 생년월일 이후 데이터 출력

print(jumin1[0:6:2])          # 홀수자리만 출력
print(jumin1[::-1])           # 역순 출력

# 인덱스 초과 - 오류 - string index out of range
# print(jumin1[100])
print(jumin1[:100:2])  # 오류 안뜸

# 리스트를 이용한 통계함수 작성
# 중앙값 계산 : 짝수, 홀수일 때 계산
# val = [1,2,3,4,5,6,7,8,9]
val = [1,2,3,4,5,6,7,8,9,10]
sum(val)
sum(val)/len(val)
min(val)
max(val)

mid = int(len(val)/2)
# print(val[mid])  # 1~9의 중앙값

print(val[mid-1:mid+1])

# 리스트 조작함수
# 요소추가 : append
list=[]
list.append(1)
list.append(2)
list.append(3)
print(list)

# 요소추가 : insert(위치, 값) (지정한 위치에 추가)
list.insert(1,10)
print(list)

# 요소 제거 : pop(), pop(위치)
list.pop()   # 마지막 요소 제거
print(list)
list.pop(0)  # 지정된 자리 요소 제거
print(list)

# 요소제거 : remove(값)
list.remove(2)   # 순서값 2가 없어지는게 아니라 값 2가 없어짐
print(list)

# 모두 제거 : clear()
list.clear()
print(list)

# 정렬하기 : sort
list=[6,3,7,2,1,10]
list.sort()
print(list)

#  특정요소 위치 파악 : index(값)
print(list.index(6))   # sort를 시켜서 sort된 값의 인덱스값이 나옴

# 리스트의 특정 요소 갯수 : count(값)
print(list.count(7))    # 7은 1개가 있다

