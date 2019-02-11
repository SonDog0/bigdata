"""
# DAO 클래스
data access object
데이터베이스의 데이터에 접근하기 위한 역활 담당
MVC 패턴에서는 서비스클래스와 DAO 객체로 나눠 프로그래밍함

DAO : 주로 DB를 사용해서 데이터를 조죄하거나 조작하는 기능 담당
서비스 : DB 작업전 데이터를 처리하는 기능을 담당

성적처리 프로그램에서의 MVC
Model (데이터)          : VO 클래스
View (데이터 출력/입력)  : 화면출력
Controller (흐름제어)   : service + dao
"""
class Student:
    def __init__(self,name,kor,eng,mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__mean = 0.0
        self.__grd = '가'

#setter/getter
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value
    @property
    def kor(self):
        return self.__kor
    @kor.setter
    def kor(self, value):
        self.__kor = value
    @property
    def eng(self):
        return self.__eng
    @eng.setter
    def eng(self, value):
        self.__eng = value
    @property
    def mat(self):
        return self.__mat
    @mat.setter
    def mat(self, value):
        self.__mat = value

    @property
    def tot(self):
        return self.__tot

    @tot.setter
    def tot(self, value):
        self.__tot = value

    @property
    def mean(self):
        return self.__mean

    @mean.setter
    def mean(self, value):
        self.__mean = value

    @property
    def grd(self):
        return self.__grd
    @grd.setter
    def grd(self, value):
        self.__grd = value

    #멤버변수 전체 출력
    def __str__(self):
        msg ='%s %d %d %d' % (self.__name,self.__kor,self.__eng,self.__mat)
        return  msg

#성적 처리 서비스 클래스
class SungJukService:
    def readSungJuk(self):
        #성적데이터 입력받은후 성적 클래스 객체로 생성
        name = input('이름은?')
        kor = int(input('국어는?'))
        eng = int(input('영어는?'))
        mat = int(input('수학은?'))
        return  Student(name,kor,eng,mat)

    def computeSungJuk(self,std):
        #총점 편귱 학점 계산
        std.tot = std.kor + std.eng + std.mat
        std.mean = std.tot / 3
        std.grd = '가'
        if std.mean >= 90:
            std.grd = '수'
        elif std.mean >= 80:
            std.grd = '우'
        elif std.mean >= 70:
            std.grd = '미'
        elif std.mean >= 60:
            std.grd = '양'

    def printSungJuk(self,std):
        msg = "%s %d %d %s" % (std.name,std.tot,std.mean,std.grd)
        print(msg)

    def saveSungJuk(self):  # DB에 성적 저장
        pass

    def readOneSungJuk(self):  # 성적조회
        pass

    def readAllSungJuk(self):  # 모든 성적 조회
        pass

    def modifySungJuk(self):  # 성적 수정
        pass
    def removeSungJuk(self):  # 성적 삭제
        pass
#oop로 만든 성적 처리 프로그램 실행 성적데이터 생성(1)
# std1=  Student("혜교",89,97,95)
# print(std1)
# #성적데이터생성2
# name = input('이름은?')
# kor = int(input('국어는?'))
# eng = int(input('영어는?'))
# mat = int(input('수학은?'))
# std2 = Student(name,kor,eng,mat)
# print(std2)

#성적데이터 생성 (3)
# sjsrv = SungJukService()
# std3 = sjsrv.readSungJuk()
# print(std3)
#
# sjsrv.computeSungJuk(std3)
# sjsrv.printSungJuk(std3)
"""
#객체 지향 개념 정리
클래스는 데이터와 기능을 함꼐 묶어
프로그램을 효율적으로 작성하는 것을 도와준다.

한편 파이썬에서 제공하는 모든 클래스는 계층구조로 이뤄져 있으며 사용자가 작성한 클래스도
사실 파이썬이 미리 정의해 둔 클래스를 상속해서 만드는 것이다.

이썬이 미리 정의해 둔 클래스를 조상 클래스라 한다.
__str__ 함수 : 조상클래스에서 미리 정의해 둔 특수한 함수이다
객체가 가지고 있는 정보나 값을 문자열로 만들어 return 하는 기능을 담당한다.
"""
class HellWorld:
    pass
hw = HellWorld
print(hw)

#생성된 객체의 메모리 주소값이 출력된다. 따라서 개발자는
# __str__함수를 재정의해서 의미있는 문자열을 출력하는데 사용한다.
#즉, 객체를 대표ㅕ하는 문자열을 return 하도록 재작성하는것.

#한편 print함수는 ()안의 변수를 문자열 형태로 출력한다.
#따라서, ()안의 ㅇ변수가 어떤 종류이던지 간에 무조건 문자열 형태로 변환해서
#출력하는데 해당 객체의 __str__ 함수를 자동으로 호출한다.



