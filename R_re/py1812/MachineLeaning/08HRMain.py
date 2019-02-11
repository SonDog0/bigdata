from oracle.hr.Department import Department
from oracle.hr.HRService import HRService
from oracle.hr.Employee import Employee
"""
emp1 = Employee(100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,0.0,0,90)
print(emp1)

hrsrv = HRService()
emp2 = hrsrv.readEmp()
print(emp2)

dept1 = Department(10,'Administration',200,1700)
print(dept1)

dept2 = hrsrv.readDept()
print(dept2)
"""


"""
# Oop에서 공유 객체 사용 방식
클래스 메서드 vs 정적 메서드

일반적으로 클래스에서 선언된 함수에 접근하려면
먼저, 클래스에 대한 객체를 생성해야만 했음
ex)객체명 = 클래스명() => 객체명.함수명()

한편, 클래스의 함수를 바로 접근할 수도 있는데
이러한 메서드를 정적 메서드라고 함
즉, 클래스에 대한 객체선언 없이 바로 함수 호출가능
함수정의시 @staticmethod라고 선언해야 함

정적 메서드 호출방법은
'클래스명.정적메서드명' 형식으로 함
"""

HRService.readEmp2()
HRService.readDept2()