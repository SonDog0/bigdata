from oracle.hr.Employee import Employee
from oracle.hr.Department import Department

class HRService:

    def readEmp(self):
        empid = int(input('사번?'))
        fname = input('이름')
        lname = input('성')
        email = input('이메일')
        phone = input('폰번')
        hdate = input('입사일')
        jobid = int(input('JOBID'))
        sal = int(input('월급'))
        comm = int(input('커미션'))
        mgrid = int(input('매니저ID'))
        deptid = int(input('부서ID'))
        return  Employee(empid,fname,lname,email,phone,hdate,jobid,sal,comm,mgrid,deptid)

    def readDept(self):
        deptid = int(input('부서ID'))
        dname = input('부서이름')
        mgrid = int(input('매니저ID'))
        locid = int(input('위치ID'))
        return  Department(deptid, dname, mgrid, locid)


    @staticmethod
    def readEmp2():
        print('정적 메서드 호출 - reademp')

    @staticmethod
    def readDept2():
        print('정적 메서드 호출 - readdept')
