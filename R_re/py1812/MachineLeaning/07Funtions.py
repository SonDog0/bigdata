# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치고 묶고
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하능

# 다른사람과의 협업시 코드가 섞이지 않게 하기 위한 목적으로도 사용됨 - 모듈
"""
# 함수의 유형
입력값 x 리턴값 x
입력값 x 리턴값 o
입력값 o 리턴값 x
입력값 o 리턴값 o !!!
"""





# def 함수명(매개변수):
#    프로그램코드
def saymsg():
    for i in range(1,4):
        print('선생님, 사랑해요')
saymsg()

def saymsg(msg):
    for i in range(1,4):
        fmt='@@선생님, %s@@'
        print(fmt%(msg))
saymsg('사랑해요')
saymsg('미워요')



# 반환값 함수 정의
# def 함수명(매개변수):
#    프로그램코드
#    return 결과값


# def plus(x,y) :
#    print(x+y)    # 반환값이 없는 함수

def plus(x,y) :
   print(x+y)    # 반환값이 없는 함수

sum = plus(1,3)



# 함수의 매개변수 갯수를 동적으로 정의
# plus 함수는 매개변수 2개만 입력받아 합계를 출력
# 만일, 입력한 모든 매개변수의 합계를 출력하려면?
# 매개변수명 앞에 *로 정의해서 함수를 만들면 됨
def manyplus(*args):   # *agrs 동적 매개변수
    sum=0
    for i in args:
        sum = sum+i
    return sum

print(manyplus(1,2,3,5))

# 함수의 결과값은 하나이다!
# 하나의 return문에 여러 결과값을 넘기는 것은 가능
# 여러 결과값은 튜플로 작성됨
# 하지만, 여러 return문으로 결과값을 넘기는 것은 불가능


def calcurate(x,y):
    sum=x+y
    minus=x-y
    multiply=x*y
    divide = x/y

    return sum, minus, multiply, divide
    # return '+'+sum
    # return '-'+minus
    # return 'x'+minus
    # return '%'+minus

print(calcurate(10,5))


# return 문의 또 다른 용도
def say_msg3(msg):
    if msg == '미워요':      # '미워요'가 입력되면 함수 실행 중단
       return
    for i in range(1, 4):
        fmt = '@@선생님, %s@@'
        print(fmt % (msg))


say_msg3('사랑해요')
say_msg3('미워요')

# 매겨변수를 정의했지만
# 매개변수 없이 호출하고 싶다면?
# 매겨변수 선언시 초기값을 지정함
def sum2(x=10,y=10):
    return x+y
print(sum2(5,10))
print(sum2())
print(sum2(100))   # 매개변수는 정의된 순서로 자동 대입
print(sum2(y=100))



# 변수의 유효범위 scope
# 함수 안에서 선언한 변수는 밖에서 접근 가능?
# call by value vs call by reference
# 함수의 내에서 선언된 변수는 함수 내에서만 사용가능

"""
outer = 1
def vartest(outer):   # 여기의 outer는 vartest 전용 변수로 전혀 다른 변수로 식별됨
    outer= outer+3
    print('안',outer)

print('전',outer)    # 함수 호출전
vartest(outer)
print('후',outer)    # 함수 호출후
"""
"""
# 함수안에서 함수 밖 변수에 접근하려면?
# return 문 사용 - 함수내에서 처리한 결과를 외부로 빼냄

outer = 1
def vartest(outer):
    outer= outer+3
    print('안',outer)
    return outer



print('전',outer)    # 함수 호출전

print('후',vartest(outer))    # 함수 호출후
"""

# global 문 사용 - 함수내에서 외부 변수 참조

outer = 1
def vartest():
    global outer     # 외부변수 참조 (비추)
    outer= outer+3
    print('안',outer)


print('전',outer)    # 함수 호출전
vartest() 
print('후',outer)    # 함수 호출후
