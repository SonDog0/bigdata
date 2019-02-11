# 추상 클래스 : abstract class
# 구체적이지 않은 요소가 포함된 클래스
# => 불완전 클래스, 미완성 클래스

# 즉, 추상 메서드를 포함한 클래스를 의미
# 추상메서드 : 메서드는 선언하되 메서드 몸체는 정의X 구현되지 않은 메서드를 의미

# 객체지향의 다향성을 구현하는 요소 중 하나
# 클래스의 상속, 메서드 재정의
#
# class unit:
#     def attack(self):
#         print('공격중')
#
# class marine(unit):
#     def attack(self):
#         print('총 공격중')
#
# class firebat(unit):
#     def attack(self):
#         print('불 공격중')
#
# # 클래스를 객체로 구현해서 공격 실시
# marine1 = marine()
# marine1.attack()
#
# firebat1 = firebat()
# firebat1.attack()

# 부모 클래스도 객체로 생성하여 공격 실시
# unit1 = unit()
# unit1.attack()

# 다른 클래스의 조상 클래스는 객체로 생성되는 것을 막고싶다면? -> 추상클래스로 정의

# 한편, 조상클래스가 객체로 생성되는 것을 막는다면 굳이 메서드 정의도 필요 없음

# 즉, unit 클래스의 attack 메서드는 자식 클래스에서 재정의해서 쓰므로
# 굳이 부모 클래스에서 attack 메서드를 미리 정의해둘 필요가 없음

# 파이썬에서 추상클래스를 정의하려면
# abc 패키지를 import 명령으로 추가해 둠
# abc : abstract base class 약자
from abc import *

class units(metaclass=ABCMeta):

    @abstractmethod   # 추상메서드로 정의
    def attack(self):
        pass

class marine(units):
    def attack(self):
        print('소총 공격')

marine1 = marine()
marine1.attack()
# 추상클래스와 그것을 상속한 클래스간에는 계약이 성립
# 계약 내용 : 추상클래스에 정의된 추상메서드를 반드시 재정의 할 것!!
#             구현시 메서드이름은 추상메서드이름을 쓸것!

#unit1 = units()
#unit1.attack()
# 추상클래스 자체로는 객체 생성 불가능!


# 성적 처리 프로그램에 상속개념을 적용해서 작성
# MidSungJuk - 이름, 국어, 영어, 수학, 총점, 평균, 학점
# FinalSungJuk - 이름, 국어, 영어, 수학, 과학, 미술, 총점, 평균, 학점


# class SungJuk(metaclass=ABCMeta):
#
#     @abstractmethod
#     def __init__(self, name, kor, eng, mat):
#         self.name = self.__class__.__name__
#         self.kor = kor
#         self.eng = eng
#         self.mat = mat
#         self.tot = 0
#         self.mean =0
#         self.grd = '가'
#
#     def __str__(self):
#         msg = '성적결과 %s %s %s %s %s %s %s' % \
#               (self.name,self.kor,self.eng,self.mat,self.tot,self.mean,self.grd)
#         return msg
#
#     @abstractmethod
#     def computeSungjuk(self):
#         pass
#
#     def computeGrade(self):
#         print('학점 계산중')
#
#
# class MidSungJuk(SungJuk):
#     pass
#
# class MidSungJuk(SungJuk):
#     def computeSungjuk(self):
#         self.tot = self.kor + self.eng +self.mat
#         self.mean = self.tot/3

# sj1 = MidSungJuk('',1,2,3)
# sj1.computeSungjuk()
# print(sj1)

# sungjuk클래스를 추상클래스로 만들긴 했지만
# 일반변수와 메서드가 함께 잇어 가독성이 떨어짐
# 적절히 분리해야할 필요 존재
# 따라서, 기능을 담당하는 메서드를 따로 뽑아서
# 추상클래스로 만드는 것이 좋음
from abc import *
class SungJuk(metaclass=ABCMeta):
    def __init__(self, name, kor, eng, mat):
        self.name = self.__class__.__name__
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.mean =0
        self.grd = '가'

    def __str__(self):
        msg = '성적결과 %s %s %s %s %s %s %s' % \
              (self.name,self.kor,self.eng,self.mat,self.tot,self.mean,self.grd)
        return msg

class SungJukService(metaclass=ABCMeta):
    @abstractmethod
    def computeSungjuk(self):
         self.tot = self.kor + self.eng +self.mat
         self.mean = self.tot/3

    def computeGrade(self):
        print('학점 계산중...')

class MidSungJuk(SungJuk, SungJukService):
    def computeSungjuk(self):
        self.tot = self.kor + self.eng +self.mat
        self.mean = self.tot/3

sj1 = MidSungJuk('수지',99,98,96)
sj1.computeSungjuk()
print(sj1)