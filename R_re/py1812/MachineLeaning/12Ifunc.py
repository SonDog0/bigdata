# 파이썬 내장함수
# 수학관련 : abs, max, min, round
print(3)
print(-3)
print(abs(-3.5))

print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))

print(round(5.678))
print(round(5.678,1))
print(round(5.678,2 ))

# 자료형 관련 : int str isinstance id type

print(type(1))
print(type('1'))

print(type(int('1')))
print(type(str(1)))

print(isinstance(int('1'), int))

a=10
b=a
print('a의 주소값', id(a))
print('a값의 주소값', id(10))
print('b의 주소값', id(b))

# 문자열을 파이썬 코드로 실행 : eval
print('1+2')
print(eval('1+2'))

print(eval('4%3'))
print(eval('4/3'))
print(eval('4//3'))
print(eval('divmod(4,3)'))

# 아스키코드 변환 : ord ,chr
print(ord('A'))
print(ord('a'))
print(ord('5'))
print(ord('!'))

print(chr(65))
print(chr(97))
print(chr(53))
print(chr(33))


# 데이터 묶기 :zip
print(list(zip('abc','123')))
print(list(zip([9,8,7],[1,2,3])))


# ex) chr(ord('x'))  == 'x' 의 결과는?
# ex) [-8,-7,7,5,-3,5,0,1]  최대 최소
# ex) 16/7의 결과 소수점 4재짜리
# ex) [1,2,3],['혜교','지현','수지']를 만들어 썅

print(chr(ord('x')) == 'x')
print(round(16/7,4))
print(list(zip([1,2,3],['혜교','지현','수지'])))