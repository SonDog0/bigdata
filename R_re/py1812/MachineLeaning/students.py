class Student:
    # 생성자
    def __init__(self, name, kor,eng,mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__mean = 0.0
        self.__grd = '가'

    # setter/getter - 컨트롤 제이 - porps 누르기
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # 멤버변수 전체 출력
    def __str__(self):
        msg='%s %d %d %d' %(self.__name, self.__kor, self.__eng, self.__mat)
        return msg


std1 = Student('수지',99,98,99)
print(std1)  # Student 클래스의 __str__ 함수 호출







