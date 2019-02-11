# python dictionary 구조를 이용해서
# json 형식으로 mongodb에 저장하기
# 데이터 저장시 날짜정보 포함
from pymongo import MongoClient
import datetime


client = MongoClient('mongodb://13.124.214.229:7185')

db = client.hellomongo
coll = db.students


# 문서document 생성 - JSON 형식
stud = {'name' : '써니' , 'kor' : '99' , 'eng' : '90', 'mat' : '95'}

stud_id = coll.insert_one(stud).inserted_id
print(stud_id)

# 한꺼번에 입력하기 - 배열 형식 이용
stud_ary = [{'name' : '경아' , 'kor' : '40' , 'eng' : '90', 'mat' : '10'},{'name' : '준모' , 'kor' : '99' , 'eng' : '90', 'mat' : '95'},{'name' : '정훈' , 'kor' : '100' , 'eng' : '100', 'mat' : '100'}]
# for i in range (0,3):
#     coll.insert_one(stud_ary[i]).inserted_id

coll.insert_many(stud_ary)


# # 데이터 시간 까지 넣기
# blogs = db.blogs
#
# new_posts = [{"author": "Mike",
# "text": "Another post!",
# "tags": ["bulk", "insert"],
# "date": datetime.datetime(2018, 11, 12, 11, 14)},
# {"author": "Eliot",
# "title": "MongoDB is fun",
# "text": "and pretty easy too!",
# "date": datetime.datetime.utcnow()}]
#
# blogs.insert_many(new_posts)

client.close()

