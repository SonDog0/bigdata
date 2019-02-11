# 클래스 정의
# 현실 세계의 사물을 컴퓨터 프로그램에서 다루기 위해
# 이것을 추상호해서 만든 결과물 = 설계도 , 틀

# 추상화 : 복잡한 개념이나 사물을 단순화시켜
# 핵심적인 개념 / 기능만 추려내는 것을 의미

# class 클래스명:
#   클래스몸체

# 자동차 클래스 정의

class Car:
    # '차' 라고 인지할만한 특성 정의
    # 생성자 constructor : 객체를 생성하는데 사용하는 함수
    # 클래스 내에 선언된 변수 : 속성, 멤버
    def __init__(self, size  , color , wheels , doors , isLoad):
        self.size = size
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.isLoad = isLoad

# 객체 정의
# 클래스를 통해 생성된 실제 결과물
# 여기에는 데이터와 기능을 포함되어있음

# 변수명 = 클래스생성자

redcar = Car(100,'red',4,4 ,True)
bluecar = Car(100,'blue',4,4 ,True)

print(redcar.size,redcar.isLoad)


