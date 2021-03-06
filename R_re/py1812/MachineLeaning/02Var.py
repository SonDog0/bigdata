"""
# 변수선언

변수는 어떠한 값을 저장하는 메모리상의 공간(그릇)
메모리 상의 공간은 고유주소 (16진수)로 할당되어 있음
개발자가 이러한 공간의 위치를 기억하기 어려움
메모리상의 주소와 문자이름으로 대응시켜
어떤 값을 저장하는데 사용하는 것을 변수라 함

JAVA, C++과는 달리 변수 선언시 자료형을 지정할 필요 X
변수에 저장된 값의 유형을 추론해 변수의 유형을 자동 정의
"""

boolVar = True       # 블리언형
intVar = 123         # 정수형
floatVar = 456.789   # 실수형
strVar = 'ABC'          # 문자형

a, b= 1,2       # 변수값 할당시 하나의 코드로 수행
c=3; d=4
# 생성한 변수의 유형을 확인하려면 Type() 사용
print(type(strVar))
print(a,b)
print(c,d)



"""
# 변수명 규칙

대/소문자 구분, 첫글자 숫자 X, 예약어 사용불가 

True, False, None, and, or, not,
break, continue, return, if, else, 

"""



"""
숫자형 - int, float
논리형 - True, False
문자형 - ''. "", """ """(주석 or 문자열 정의)
"""
str1 ="""
asdf
asdf
asf
asdf
asd
fsadf
"""
print(str1)




# 산술연산자 : + - * / % //(몫) **(제곱)

print(5/3)
print(5//3)
print(5%3)
print(5**3)

# 형변환
print(298/3)            # java와는 달리 형변환 불필요
# print("100"+1)          # java에서는 1001이 뜸 but  python에서는 오류발생 - 문자열은 숫자와 연산 불가
# print(int("100")+1)
# print('987.123'+0.5)
# print(int('987.123')+0.5)   # int 함수로 실수변환 불가
print(float('987.123')+0.5)

# print(123 + '456') # 숫자는 문자열과 연결 불가
print(str(123) + '456')



# 대입연산자  : =
# 단축대입연산자 : +=, -=, *=, /=, //=, **=, %=

e = 1; e += 1 # e=e + 1
              # 자바, C++ 에서는 증가++/감소-- 연산자로 구현
              # 파이썬은 증가/감소 연산자 지원X
print(e)

# 관계연산자 : ==,  >=, <=, <>, !=
# 조건문이나 반복문에 주로 사용

# 논리연산자 : and, or, not
# 하나 이상의 조건문을 판별할 때 사용

# 연산자 우선순위 : (), [], {}  ->  **  -> * / % //  ->  + -


# 콘솔로부터 입력받기 : input
# 육면체 부피 부가하기 - 가로,세로,높이 입력받아 부피 계산

w = int(input('가로크기입력'))
d = int(input('세로크기입력'))
h = int(input('높이크기입력'))

print('부피는 ',w*d*h,'입니다')
