class Department:
    def __init__(self, deptid, dname, mgrid, locid):
        self.__deptid = deptid
        self.__dname = dname
        self.__mgrid = mgrid
        self.__locid = locid

    # setter/getter
    @property
    def deptid(self):
        return self.__deptid
    @deptid.setter
    def deptid(self, value):
        self.__deptid = value

    @property
    def dname(self):
        return self.__dname
    @dname.setter
    def dname(self, value):
        self.__dname = value

    @property
    def mgrid(self):
        return self.__mgrid
    @mgrid.setter
    def mgrid(self, value):
        self.__mgrid = value

    @property
    def locid(self):
        return self.__locid
    @locid.setter
    def locid(self, value):
        self.__locid = value

    # 멤버변수 전체 출력
    def __str__(self):
        msg = '%d %s %d %d' %\
               (self.__deptid,self.__dname,self.__mgrid,self.__locid )
        return msg