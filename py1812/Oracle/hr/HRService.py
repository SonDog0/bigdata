
from Oracle.hr.Employee import Employee

class HRService:
    def readEmp(self):
        empid = int(input('사번은?'))
        fname = input('이름?')
        lname = input('성은?')

        return Employee(empid,fname ,lname ,'','','','',0,0.0,0,0)


    def readDept(self):
        pass

