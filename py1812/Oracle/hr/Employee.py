# 사원정보 클래스

class Employee:
    def __init__(self,empid,fname,lname,email,phone,hdate,jobid,sal,comm,mgrid,deptid):

        self.__empid = empid
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jobid = jobid
        self.__sal = sal
        self.__comm = comm
        self.__mgrid = mgrid
        self.__deptid = deptid
        pass

    def __str__(self):
        msg = '%d %s %s %s %s %s %s %d %.2f %d %d' % (self.__empid,self.__fname,self.__lname,self.__email,self.__phone,self.__hdate,self.__jobid,self.__sal,self.__comm,self.__mgrid,self.__deptid)
        return msg

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self):
        return self.__empid

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self):
        return self.__fname


    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self):
        return self.__lname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def hdate(self):
        return self.__phone

    @property
    def hdate(self):
        return self.__hdate

    @hdate.setter
    def hdate(self):
        return self.__hdate


    @property
    def jobid(self):
        return self.__jobid

    @jobid.setter
    def jobid(self):
        return self.__jobid

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self):
        return self.__sal

    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self):
        return self.__comm


    @property
    def mgrid(self):
        return self.__mgrid

    @mgrid.setter
    def mgrid(self):
        return self.__mgrid

    @property
    def deptid(self):
        return self.__deptid

    @deptid.setter
    def deptid(self):
        return self.__deptid





