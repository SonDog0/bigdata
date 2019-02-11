# 딕셔너리
# 이름key과 값value으로 구성된 연관 배열의 일종
# 자료형은 {}를 이용하고
# 이름과 값은 : 으로 구분해서 정의
# 리스트나 튜플처럼 순차적으로 자료를 찾지 않고
# 키를 통해 자료를 찾기 때문에 속도가 빠름

person = {'name' : '혜교', 'tel':123456789,
          'email':'abc@xyz.com',
          'birth':[123,456,789]}
print(person)

# 딕셔너리에 새로운 '키':'값' 추가
# 변수명[키] = 값
person['addr'] = '서울시 강남구'
print(person)

# 딕셔너리 기존 값 수정
# 변수명[기존키] = 값
person['tel'] = 987654321
print(person)

# 딕셔너리 기존 값 삭제
# del(변수명[기존키])
del(person['tel'])
print(person)

# 딕셔너리 값 조회 - 키, get함수
print(person['name'])
print(person.get('name'))
print(person.get('birth'))
print(person.get('birth')[1])

# 존재하지 않는 키를 사용하면?
# print(person['gender'])     # 오류 발생
print(person.get('gender'))   # None이라고 뜸

# 딕셔너리의 모든 키 출력
print(person.keys())      # dict_keys 도 출력
print(list(person.keys()))

# 딕셔너리의 모든 값 출력
print(person.values())
print(list(person.values()))

# 딕셔너리 특정 키 존재여부 조회 : in
print('name'in person)

# ex) employees 데이터를 딕셔너리(emp)로 생성
# 1 employees.csv 파일을 읽어오기

# 파일 객체를 이용해서 파일을 읽어옴
empkey = ['empid','fname','lname','email','phone','hdate','jobid','sal','comm','mgrid','deptid']
"""
with open('c:/Java/data/hr/EMPLOYEES.csv') as f:
    for lines in f :
        line = lines.split(',')
        print(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
"""
emps=[]
with open('c:/Java/data/hr/EMPLOYEES.csv') as f:
    for lines in f :
        line = lines.split(',')
        emp={}
        for i in range(len(empkey)):
            emp[empkey[i]]=line[i]
        emps.append(emp)
print(emps)
