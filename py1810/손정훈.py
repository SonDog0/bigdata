### 2018-10-19 평가 / 손정훈


from pymongo import MongoClient,DESCENDING,ASCENDING
import datetime




client = MongoClient('mongodb://13.124.214.229:7185')
##### 1번. HR 데이터베이스 생성 및 접속  #####
db = client.HR

##### 2번. 콜렉션 생성 및 연결 , 100~105 사원번호 콜렉션에 저장  #####
coll = db.EMPLOYEES
# emps = [
#     {'EMPLOYEE_ID' : '100' , 'FIRST_NAME' : 'Steven' , 'LAST_NAME' : 'King', 'EMAIL' : 'SKING' , 'PHONE_NUMBER' : '515.123.4567' , 'HIRE_DATE' : '2003-06-17', 'JOB_ID' : 'AD_PRES' , 'SALARY' : 24000 , 'COMMISSION_PCT' : None , 'MANAGER_ID' : None , 'DEPARTMENT_ID' : '90'  },
# {'EMPLOYEE_ID' : '101' , 'FIRST_NAME' : 'Neena' , 'LAST_NAME' : 'Kochhar', 'EMAIL' : 'NKOCHHAR' , 'PHONE_NUMBER' : '515.123.4568' , 'HIRE_DATE' : '2005-09-21', 'JOB_ID' : 'AD_VP' , 'SALARY' : 17000 , 'COMMISSION_PCT' : None , 'MANAGER_ID' : '100' , 'DEPARTMENT_ID' : '90'  },
# {'EMPLOYEE_ID' : '102' , 'FIRST_NAME' : 'Lex' , 'LAST_NAME' : 'De Haan', 'EMAIL' : 'LDEHAAN' , 'PHONE_NUMBER' : '515.123.4569' , 'HIRE_DATE' : '2001-01-13', 'JOB_ID' : 'AD_VP' , 'SALARY' : 17000 , 'COMMISSION_PCT' : None , 'MANAGER_ID' : '100' , 'DEPARTMENT_ID' : '90'  },
# {'EMPLOYEE_ID' : '103' , 'FIRST_NAME' : 'Alexander' , 'LAST_NAME' : 'Hunold', 'EMAIL' : 'AHUNOLD' , 'PHONE_NUMBER' : '590.423.4567' , 'HIRE_DATE' : '2006-01-03', 'JOB_ID' : 'IT_PROG' , 'SALARY' : 9000 , 'COMMISSION_PCT' : None , 'MANAGER_ID' : '102' , 'DEPARTMENT_ID' : '60'  },
# {'EMPLOYEE_ID' : '104' , 'FIRST_NAME' : 'Bruce' , 'LAST_NAME' : 'Ernst', 'EMAIL' : 'BERNST' , 'PHONE_NUMBER' : '590.423.4568' , 'HIRE_DATE' : '2007-05-21', 'JOB_ID' : 'IT_PROG' , 'SALARY' : 6000 , 'COMMISSION_PCT' : None , 'MANAGER_ID' : '103' , 'DEPARTMENT_ID' : '60'  },
# {'EMPLOYEE_ID' : '105' , 'FIRST_NAME' : 'David' , 'LAST_NAME' : 'Austin', 'EMAIL' : 'DAUSTIN' , 'PHONE_NUMBER' : '590.423.4569' , 'HIRE_DATE' : '2005-06-25', 'JOB_ID' : 'IT_PROG' , 'SALARY' : 4800 , 'COMMISSION_PCT' : None , 'MANAGER_ID' : '103' , 'DEPARTMENT_ID' : '60'  }
# ]
# coll.insert_many(emps)

########################################################################


# 전체 출력
# cursor = coll.find({})

##### 3번. 급여 15000 이상 사원들의 사번 , 성 , 급여 출력 #####
# cursor = coll.find({'SALARY' : {'$gte' : 15000} } ,{'EMPLOYEE_ID' : 1 , 'LAST_NAME' : 1 , 'SALARY' : 1 })

##### 4번. 입사일이 2005-01-01 부터 2005-05-31 까지인 사원들을 조회하세요 #####
# cursor = coll.find({'HIRE_DATE' : {'$gte' : '2005-01-01' , '$lte' : '2005-05-31' }})


##### 5번. 직급별 사원들의 급여 총액이 30,000 ~ 60,000인 직급을 내림차순으로 조회하세요  #####
cursor = coll.aggregate( [
    {'$group' : { '_id' : '$JOB_ID', '급여총액' : { '$sum' : '$SALARY' }} },
    {'$match' : {'급여총액' : {'$gte' : 30000 , '$lte' : 60000} }},
    {'$sort' : { '급여총액' : 1  } }
])



############### 공통 출력 부분 ####################

for cur in cursor:
    print(cur)

##################################################



# 접속 해제
client.close()

