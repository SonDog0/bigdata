import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient,DESCENDING,ASCENDING
import datetime
from bson.objectid import ObjectId


client = MongoClient('mongodb://13.124.214.229:7185')

db = client.hellomongo
# coll = db.students
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)

# 데이터 수정 - 수지 학생의 성적 변경
# results = coll.update_one( {'name' : '수지' }, { '$set' : { 'kor' : 85 }})
# coll.update_one( {'name' : ' 동건' }, { '$set' : { 'name' : '동건'}})
# coll.update_one( {'name' : ' 동건' }, { '$set' : { 'name' : '동건'}})
# coll.update_one( {'name' : '동건' }, { '$set' : { 'kor' : 30 }})

# print('찾은 항목 수 : ' , results.matched_count)
# print('수정한 항목 수 : ' , results.modified_count)



# 데이터 수정 - 국어점수가 70점 이하 학생들 성적 변경 (0점으로)
# results = coll.update_many ( {'kor' : {'$lte' : 70
#                                        } } , {'$set' : { 'kor' : 0}} )

# print('찾은 항목 수 : ' , results.matched_count)
# print('수정한 항목 수 : ' , results.modified_count)



# 블로그 본문과 제목 수정 -  날짜도 수정
# coll = db.blogs
# results = coll.update_one ( {'author' : 'Eliot' } , {'$set' : {'text' : '...' , 'title' : '...' ,'date' : datetime.datetime.utcnow()}  } )
#
# print('찾은 항목 수 : ' , results.matched_count)
# print('수정한 항목 수 : ' , results.modified_count)
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)
#

# 데이터 삭제 - 지현 학생의 성적 삭제

# coll = db.students
#
# results= coll.delete_one({'name' : '써니'})
#
#
# print('수정한 항목 수 : ' , results.deleted_count)
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)


# 데이터 삭제 - 국어점수가 0인 학생들 성적 삭제

# coll = db.students

# results= coll.delete_many({'kor' : 0})

# print('삭제된 항목 수 : ' , results.deleted_count)
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)




# 모두 삭제 - 블로그 데이터 삭제
coll = db.blogs
#
results = coll.delete_many({})
print('삭제된 항목 수 : ' , results.deleted_count)

cursor = coll.find({})
for cur in cursor:
    print(cur)


client.close()