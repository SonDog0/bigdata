# 객체 지향 프로그래밍
# 1. 값만 저장하는 클래스 :VO(value object), DTO(data transfer object)

# 보통 VO클래스들은 RDBMS의 테이블과 유사한 구조로 구성

# 사원정보입력 -> employee 클래스에 저장 -> RDBMS로 저장

# 사원정보 조회 -> RDBMS에서 관련정보 추출
# -> employee 클래스에 저장 - > 화면 출력

# 사원정보들 조회 -> RDBMS에서 관련정보 추출
# -> employee 클래스에 저장 - > 리스트에 저장
# -> 추출이 끝날때 까지 반복 -> 화면 출력




# Oracle 10g의 HR 데이터베이스의 Employees 테이블의
# 각 행을 다루기 위해 VO클래스로 작성

class Employee :
    # 생성자
    def __init__(self, empid, fname, lname, email, phone,
                 hdate, jobid, sal, comm, mrgid, deptid):
        self.empid = empid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.hdate = hdate
        self.jobid = jobid
        self.sal = sal
        self.comm = comm
        self.mrgid = mrgid
        self.deptid = deptid

    # 멤버 출력 함수 : 매직 함수
    # 클래스 정의시 기본적으로 제공되는 특수한 함수들
    def __str__(self):
        msg = '%s,%s,%s' % (self.empid, self.lname, self.jobid)
        return msg




# 사원 객체 생성
emp1 = Employee(100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,'','',90)
emp2 = Employee(145,'John','Russell','JRUSSEL','011.44.1344.429268','2004-10-01','SA_MAN',14000,0.4,100,80)


# __str__ 함수 정의 x 시
# print(emp1.empid, emp1.lname, emp1.jobid)
# print(emp2.empid, emp2.lname, emp2.jobid)

# __str__ 함수 정의o
print(emp1)
print(emp2)


# 객체 정보 수정 - 사번 변경
emp1.empid = 999

print(emp1)

# OOP의 캡슐화에 근거해서
# 객체명. 속성으로 값을 수정하거나 읽는 것은 비추
# 이러한 작업은 setter, getter 메서드를 사용해야함
# 자바에서는


class Employee2 :
    # 생성자
    def __init__(self, empid, fname, lname, email, phone,
                 hdate, jobid, sal, comm, mrgid, deptid):
        # 멤버에 접근제한 기능 부여
        # 멤버명 앞에  __ 를 추가하면 private 멤버로 선언
        self.__empid = empid
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jobid = jobid
        self.__sal = sal
        self.__comm = comm
        self.__mrgid = mrgid
        self.__deptid = deptid

    # 멤버 출력 함수 : 매직 함수
    # 클래스 정의시 기본적으로 제공되는 특수한 함수들
    def __str__(self):
        msg = '%s,%s,%s' % (self.empid, self.lname, self.jobid)
        return msg
    # private 멤버에 접근할 수 있도록
    # setter, getter 메서드 생성
    # 멤버명에 set/get 를 붙인 함수 생성
    # 자바에서 사용하는 방식
    def setEmpid(self, empid):
        self.__empid=empid
    def getEmpid(self):
        return self.__empid

    # 한편, 파이썬에서는
    # setter/getter 대신에 @property, @setter를 사용
    # 멤버명앞에 @를 붙여서
    # 함수의 의미를 보조적으로 설명함 - decorator
    @property    # getter와 유시
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self,lname):
        self.__lname = lname





# 사원 객체 생성
emp3 = Employee2(100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,'','',90)
print(emp1.empid)
# print(emp3.empid)   # 캡슐화를 시켰기 때문에 이런식으로는 볼 수 없음
print(emp3.getEmpid())    # empid 조회
emp3.setEmpid(9999)       # empid 변경
print(emp3.getEmpid())

emp3.lname = '수지'
print(emp3.lname)

# VO클래스 만드는 법
# __init__ 로 생성자 만들면서 private 멤버 선언
# __str__로 모든 멤버 변수 출력 기능 정의
# @property, @setter를 이용해서 캡슐화 구현

# ex)HR 데이터베이스 DEPARTMENTS 테이블을 위한
# Department 클래스를 정의
# deptid, dname, mgrid, locid

class Department:
    def __init__(self, deptid, dname, mrgid, locid):
        self.__deptid = deptid
        self.__dname = dname
        self.__mrgid = mrgid
        self.__locid = locid

    def __str__(self):
        msg = '%s,%s,%s,%s' % (self.__deptid, self.__dname, self.__mrgid, self.__locid)
        return msg

    @property
    def deptid(self):
        return self.__deptid

    @deptid.setter
    def deptid(self,deptid):
        self.__deptid = deptid

    @property
    def dname(self):
        return self.__dname

    @dname.setter
    def deptid(self,dname):
        self.__deptid = dname

    @property
    def mrgid(self):
        return self.__mrgid

    @mrgid.setter
    def deptid(self,mrgid):
        self.__mrgid = mrgid

    @property
    def locid(self):
        return self.__locid

    @locid.setter
    def deptid(self,locid):
        self.__locid = locid


dep1 = Department(10,'Administration',200,1700)
print(dep1.dname)

