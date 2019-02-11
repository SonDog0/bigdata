from Oracle.hr.HRService import HRService

from Oracle.hr.Employee import Employee

# emp1 = Employee(100,'Steve','King','SKing','515.123.4567','2003-06-17', 'AD_PRES',24000,0.0,0,90)
#
# print(emp1)

hrsrv = HRService()
emp2 = hrsrv.readEmp()
print(emp2)



