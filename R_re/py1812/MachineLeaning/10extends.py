# 클래스 상속
# 부모클래스로 부터 변수, 함수들을 물려받아 새로운 클래스를 만드는 과정
# 한번 정의된 데이터유형(함수,클래스)을 필요에 따라 다시 재활용해서 반복되는 코드를 줄일수 있음
# 상속의 장점 - 중복코드 배제, 유지보수 용이, 통일성 유지, 다형성 구현 용이

# class 클래스이름(부모클래스)

# 스타크래프트 유닛을 상속개념을 이용해서 구현
# 테란 진영 유닛을 클래스로 작성
# 해병대, 의무관, 화염방사병
#

# class 해병대:  # 공격력 10인 유닛
#     def __init__(self, life, energy, attack):
#         self.name = self.__class__.name
#         self.life = life
#         self.energy = energy
#         self.attack = 10
#
#     def __str__(self):
#         msg = '%s %s %s %s' % \
#               (self.name, self.life, self.energy, self.attack)
#         return msg
#     def attack(self):
#         print('플라즈마 소총으로 공격중')
#
#
# class 의무관:  # 공격력 1인 유닛
#     def __init__(self, life, energy, attack):
#         self.name = self.__class__.name
#         self.life = life
#         self.energy = energy
#         self.attack = 1
#
#     def __str__(self):
#         msg = '%s %s %s %s' % \
#               (self.name, self.life, self.energy, self.attack)
#         return msg
#
#     def heal(self):
#         print('지정한 유닛을 치료중')
#
#
# class 화염방사병:  # 공격력 20인 유닛
#     def __init__(self, life, energy, attack):
#         self.name = self.__class__.name
#         self.life = life
#         self.energy = energy
#         self.attack = 20
#
#     def __str__(self):
#         msg = '%s %s %s %s' % \
#               (self.name, self.life, self.energy, self.attack)
#         return msg
#
#     def attack(self):
#         print('화염방사기로 공격중')


class unit:  # 테란 유닛의 조상클래스
    def __init__(self, life, energy):
        self.name = self.__class__.__name__
        self.life = life
        self.energy = energy


    def __str__(self):
        msg = '%s %s %s' % \
              (self.name, self.life, self.energy)
        return msg
    def attack(self):
        pass

class marine(unit):
    def __init__(self,life,energy):
        super().__init__(life,energy)  # 부모클래스에 생성된 생성자를 호출
        self.power =10

    def __str__(self):
        # 메서드 오버라이딩 : 함수 재정의
        # 상속관계에 있어서 부모 클래스에서 정의된 함수를
        # 자식 클래스에 적합하도록 재작성하는 것을 의미
        msg = super().__str__()
        return ('%s %s') % (msg, self.power)

    def attack(self):
        print('플라즈마 소총으로 공격중')

marine1 = marine(100,100)
print(marine1)
marine1.attack()

class firebat(unit):

    def attack(self):
        print('화염방사기 공격중')

firebat1 = firebat(200,100)
print(firebat1)
firebat1.attack()

class medic(unit):

    def attack(self):
        print('치료중')

medic1 = medic(150,200)
print(medic1)
medic1.attack()


print()



# 성적 처리 프로그램에 상속개념을 적용해서 작성
# MidSungJuk - 이름, 국어, 영어, 수학, 총점, 평균, 학점
# FinalSungJuk - 이름, 국어, 영어, 수학, 과학, 미술, 총점, 평균, 학점

class SungJuk:
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

    def computeSungjuk(self):
        self.tot = self.kor + self.eng +self.mat
        self.mean = self.tot/3

    def computeGrade(self):
        print('학점 계산중')


class MidSungJuk(SungJuk):
    pass

sj1 = MidSungJuk('혜교',99,98,97)
sj1.computeSungjuk()
print(sj1)

class FinalSungJuk(SungJuk):
    def __init__(self, name, kor, eng, mat, sci, art):
        super().__init__(name,kor,eng,mat)
        self.sci = sci
        self.art = art

    def __str__(self):
        msg = super().__str__()
        msg = '%s %s %s' % (msg, self.sci, self.art)
        return msg

    def computeSungjuk(self):
        super().computeSungjuk()
        self.tot = self.tot + self.sci + self.art
        self.mean = self.tot / 5

sj2 = FinalSungJuk('지수',99,98,97,96,95)
sj2.computeSungjuk()
print(sj2)
