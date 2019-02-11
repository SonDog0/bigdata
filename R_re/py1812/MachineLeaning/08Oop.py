"""
# 파이썬 객체지향 프로그래밍

oop : object orientied programming
프로그램을 명령들의 단순 그룹체라고 보는 시각에서 벗어나
하나의 독립된 객체들의 모음이라고 보는 시각에 근거해서
프로그래밍 하는 패러다임

프로그램을 보다 유연하게 작성할 수 있고
프로그램 코드의 재사용을 높일 수 있으며
대규모 소프트웨어 개발시 유지보수가 용이해짐

프로그램의 각 구성요소를 실제세계의 객체와 유사하게
디자인해서 클래스로 정의하는 것에 중점을 둠

"""

"""
# ex) 성적 처리 프로그램 I
# 이름, 국어, 영어, 수학을 입력하면 총점 평균 학점을 출력하는 프로그램 작성

# 입력처리
name = input('이름은?')
kor = int(input('국어'))
eng = int(input('영어'))
mat = int(input('수학'))

# 성적처리
tot = kor+mat+eng
mean = tot/3
if mean >= 90 :
    grd = 'A'
elif mean >= 80 :
    grd = 'B'
elif mean >= 70 :
    grd = 'C'
elif mean >= 60 :
    grd = 'D'
elif mean >= 50 :
    grd = 'E'
else :
    grd = 'F'

# 결과 출력
print('입력 : %s %d %d %d' %(name,kor,eng,mat))
print('결과 : %d %.1f %s' %(tot,mean,grd))
"""

"""
# ex) 성적처리 프로그램 II
# 함수기반 프로그래밍 : 처리코드들을 하나의 이름으로 묶음

# 함수에 너무 많은 기능을 부여해선 안됨
# 하나의 기낭만 부여

def readSungJuk():
    name = input('이름은?')
    kor = int(input('국어'))
    eng = int(input('영어'))
    mat = int(input('수학'))

    return name, kor, eng, mat


def computeSungJuk( kor, eng, mat ):
    tot = kor + mat + eng
    mean = tot / 3
    if mean >= 90:
        grd = 'A'
    elif mean >= 80:
        grd = 'B'
    elif mean >= 70:
        grd = 'C'
    elif mean >= 60:
        grd = 'D'
    elif mean >= 50:
        grd = 'E'
    else:
        grd = 'F'

    return tot,mean,grd


def printSungJuk(name, kor, eng, mat, tot, mean, grd):
    print('입력 : %s %d %d %d' % (name, kor, eng, mat))
    print('결과 : %d %.1f %s' % (tot, mean, grd))

name, kor, eng, mat = readSungJuk()
tot, mean, grd = computeSungJuk(kor, eng, mat)
printSungJuk(name, kor, eng, mat, tot, mean, grd)
"""

# ex) 성적 처리프로그램 III
# oop 기반 프로그래밍 : 함수들과 관련 변수를 하나로 묶음

class SungJukVO():    # 변수들로 구성된 클래스
    pass

class SungJukDAO():   # 처리코드들로 구성된 클래스
    pass

# 객체지향에서 클래스 특성
# 1. 값만 저장하는 클래스 :VO(value object), DTO(data transfer object)
# 2. 기능만을 모아둔 클래스 : DAO(data access object) or BO(business logic object)
# 프로그램이 제공하는 기능 : CRUD(create, read, update, delete)
# 3. UI를 모아둔 클래스 : UO(user interface object)

# OOP의 3대 특성
# 1. 캡슐화 : 관련기능을 한곳에 모아둠, 코드보안성 증대
# 2. 상속 : 기능추가 + 코드 재사용
# 3. 다형성 : 오버로딩(매서드 재정의 : 기능변경) 오버라이딩(매서드 다중정의(같은이름의 함수 추가) : 기능추가)

# oop의 5대 원칙 - SOLID - 찾아보기
# 결합도, 응집도
# S : 단일책임의 원칙


# 클래스 정의
# 현실세계의 사물을 컴퓨터 프로그램에서 다루기 위해
# 이것을 추상화해서 만든 결과물 - 설계도, 틀
# EX) 붕어빵 틀

# 추상화 : 복잡한 개념이나 사물을 단순화시켜
# 핵심적인 개념/기능만 추려내는 것을 의미

# class 클래스명 :
#    클래스 몸체

# 자동차 클래스 정의
class Car:
    #'차' 라고 인지할만 특성 정의
    # 생성자 counstructor : 객체를 생성하는데 사용하는 함수
    # 클래스 내에 선언된 변수 : 속성, 멤버
    def __init__(self, size,color,wheels,doors,isLoad) :  # 생성자constructor
        self.size = size
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.isLoad = isLoad






# 객체 정의
# 클래스를 통해 생성된 결과물
# 여기에는 데이터와 기능을 포함함
# ex) 붕어빵 <- 붕어빵 틀에 밀가루반죽과 팥을 넣어 만듦
# 변수명 = 클래스이름()
redcar = Car(100,'red',4,4, True)
greencar = Car(50,'green',3,4,False)
bluecar = Car(10,'blue',2,2,False)

# 객체의 속성에 접근하려면 . 연산자를 이용
# 즉, 객체명.속성명 형식을 사용해서 객체의 속성을 볼 수 있음
print(redcar.size,redcar.color,redcar.wheels,redcar.doors,redcar.isLoad)











