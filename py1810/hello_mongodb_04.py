# 한빛미디어 -store - 새로나온책
# http://www.hanbit.co.kr/store/books/new_book_list.html
# 제목, 저자 가격 , 생성일 추출해서 new_books 컬렉션에 저장

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId



client = MongoClient('mongodb://13.124.214.229:7185')

db = client.hellomongo
coll = db.students

print(coll.find_one({}))
print('\r\n')
# 국어점수가 60점 이상인 학생 조회(1명)
print(coll.find_one({'kor' : {'$gte' : 60 }}))

# 모든 doc 조회 - 모든 doc 출력 - cursor 이용
# find() 의 실행결과는 커서형식의 값으로 return
# 향상된 for문으로 처리하거나, cursor 형식을 이용한 반복문으로 처리

print('\r\n')
# print(coll.find()) # 데이터가 있는 주소만 출력
print('\r\n')
print('전체데이터 조회')
for stud in coll.find():
    print(stud)

print('\r\n')

print('국어 점수가 60점 이상인 학생 조회')
# ex) 국어 점수가 60점 이상인 학생 조회
cursor = coll.find({ 'kor' : { '$gte' : 60  }})
for stud in cursor:
    print(stud)

#
# print('\r\n')
# # cursor 형식으로 처리
print('\r\n')
print('cursor형식으로 처리 ')
cursor = coll.find({ 'kor' : { '$gte' : 60 }})
print(cursor.next())
print(cursor.next())
print(cursor.count())

# cnt = cursor.count()
#
# while ( cnt > 0 ) :
#     print(cursor.next())
#     cnt = cnt - 1


# id가 5bc6ab4f7c796c17481c7560 인 학생의 정보 출력
print('id가 5bc6ab4f7c796c17481c7560 인 학생의 정보 출력')
stud_id = ObjectId('5bc6ab4f7c796c17481c7560')
stud = coll.find_one({ '_id' : stud_id })
print(stud)
print('\r\n')



client.close()
