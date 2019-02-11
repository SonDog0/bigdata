# 파이썬으로 JSON 형식 다루기
# javascript object notation
# 자바스크립트에서 객체를 표현하는 방식을 이용해서
# 각종 프로그래밍 언어에서 데이터를 표현함
# 예전에는 csv, xml로 데이터를 표현했다면
# 지금은 json으로 거의 대부분 사용

# json은 파이썬 사전식dictionary 자료형과 비슷
# [ { 키 : 값 } , { ... } ]
# { 'userid' : 'zzyzzy' , 'passwd' : '123456' , 'age' : 15 }
# 따옴표 붙이면 문자인식

import json
# 파이썬에서 json을 다룰려면 json 내장객체 호출
from collections import OrderedDict
# JSON 파일을 생성하기 위한 사전형 객체 호출

myjson = { 'userid' : 'zzyzzy' , 'passwd' : '123456' , 'age' : 15 }
# json 객체를 만들려면 python의 dict 객체처럼 정의

#print(myjson)

json_obj = json.dumps(myjson, indent=2)
# json 객체는 dump 함수를 이용
# indent 속성을 이용하면 json 문자열을 보기좋게 들여쓰기 적용

print(json_obj)

# 이름 , 이메일, 전화번호를 json 객체로 생성
personal = {'name':'홍길동' , 'eamil':'bac@xyz.com', 'phone':'123-456-7890'}

ps_json =json.dumps(personal,indent=2)
# 한글 객체를 json으로 변환할 경우 인코딩이 변해서 저장
# ex ) '홍길동 ' =>  "\ud64d\uae38\ub3d9"
print(ps_json)

print(json.loads(ps_json))
# json 객체를 다시 원래의 dict 객체로 변환해서 출력 (한글 안 깨짐)

ps_jsonk = json.dumps(personal,ensure_ascii=False)
# ensure_ascii 속성을 False로 지정하면
# ASCII로의 강제 인코딩을 중지할 수 있음 - 한글 깨짐 방지
print(ps_jsonk)


# OrderedDict 객체를 이용해서 json 객체 정의
persons = OrderedDict()
persons['name']='홍길동'
persons['email']='abc@na.com'
persons['phone']='123-456-17'
persons['friends'] = ['지현', '혜교', '수지']


#객체 안에 다시 객체 정의 (persons 안에 schools)
schools =OrderedDict()
schools['고등학교']='서울고';
schools['대학교']='서울대';
schools['대학원']='서울대학원';

persons['schools'] =schools

print(persons)
print('\r\n')
print(json.dumps(persons, ensure_ascii=False,indent=2))

print('\r\n')
# personal 객체를 JSON파일로 저장
with open('data/personal.json','w',encoding='utf-8') as jsonout:
    json.dump(persons, jsonout, ensure_ascii=False,indent=2)

# JSON 파일로 저장된 personal 객체 출력하기
with open('data/personal.json','r',encoding='utf-8') as jsonin:
    person_data = json.load(jsonin)

print(person_data)
