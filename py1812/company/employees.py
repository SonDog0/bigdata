class Staff:
    def __init__(self,empid,name,deptname,gender,tech,age):
        self.__empid = empid
        self.__name = name
        self.__deptname = deptname
        self.__gender = gender
        self.__tech = tech
        self.__age = age

    def __str__(self):
        msg = '%d %s %s %s %s %s' % (self.__empid,self.__name,self.__deptname,self.__gender,self.__tech,self.__age)
        return msg

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self):
        return self.__empid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self):
        return self.__name


    @property
    def deptname(self):
        return self.__deptname

    @deptname.setter
    def deptname(self):
        return self.__deptname

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self):
        return self.__gender

    @property
    def tech(self):
        return self.__tech

    @tech.setter
    def tech(self):
        return self.__tech

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self):
        return self.__age


    def printbio(self):
        if self.gender == 'M':
            self.__gender = '남자'
        elif self.gender == 'F':
            self.__gender = '여자'
        else:
            self.__gender = '오입력'

        print(self.name +' 직원은 나이가 ' + self.age +'이고 성별은 ' + self.gender +  '입니다' )

# 실행시

from company.employees import Staff

stf = Staff(3,'Ernie','Sales','M','UNIX,Perl','23')

stf.printbio()
