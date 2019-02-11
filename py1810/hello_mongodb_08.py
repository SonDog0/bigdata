# python을 이용한 데이터 수정 삭제 예제 (inventory)


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient,DESCENDING,ASCENDING
import datetime
from bson.objectid import ObjectId

# zipcode


client = MongoClient('mongodb://13.124.214.229:7185')

db = client.test
coll = db.inventory

# 1. inventory 컬렉션의 document 총 수는 ?

# cursor = coll.find({})
# print(cursor.count())

# 2. tags 항목이 red, blank인 doc는 ?

# cursor = coll.find({'tags' : ['red','blank']})
# for cur in cursor:
#     print(cur)


# 3. dim_cm 항목이 22보다 크고 , 30보다 작은 doc는 ?
#
# cursor = coll.find({'dim_cm' : {'$gt' : 22 ,'$lt' : 30}})
# for cur in cursor:
#     print(cur)

# 4. tags 항목이 내용 갯수가 3인 doc는 ?

# cursor = coll.find({'tags' : { '$size' : 3 }})
# for cur in cursor:
#     print(cur)

# 5. item이 'paper'인 doc를 찾아서 status를 P로 uom을 in로 수정
# results = coll.update_many({'item' : 'paper'},{'$set' : {'status' : 'P' , 'uom' : 'in'} } )
# print('찾은 항목 수 : ' , results.matched_count)
# print('수정한 항목 수 : ' , results.modified_count)
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)
# 6. qty가 50보다 작은 항목을 찾아서 status를 P로 uom을 in로 수정
# results = coll.update_many({'qty' : {'$lt' : 50 }},{'$set' : {'status' : 'P' , 'uom' : 'in'} } )
# print('찾은 항목 수 : ' , results.matched_count)
# print('수정한 항목 수 : ' , results.modified_count)
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)

# 7. item이 'paper'인 doc를 찾아서 instock 이라는 항목에 배열 형식으로 warehouse는 각각 A , B 로 qty는 각각 60 , 40을 수정

# results = coll.update_many({ 'item' : 'paper' } , {'$set' : { 'instock' : [{'warehose' : 'A' , 'qty' : 60} , {'warehouse' : 'B' , 'qty' : 60 }] } } )
# print('찾은 항목 수 : ' , results.matched_count)
# print('수정한 항목 수 : ' , results.modified_count)
#
# cursor = coll.find({})
# for cur in cursor:
#     print(cur)

# 8. status가 'D'인 항목을 삭제

# results = coll.delete_many( { 'status' : 'D'} )
# print('삭제 된 수  : ' , results.deleted_count)

# 9. status가 'A'이고 item이 notebook인 항목 삭제

# results = coll.delete_many( { 'status' : 'A' , 'item' : 'notebook'} )
# print('삭제 된 수  : ' , results.deleted_count)

# 10. size가 없는 doc를 삭제
results = coll.delete_many({ 'uom' : None } )
print('삭제 된 수  : ' , results.deleted_count)

cursor = coll.find({})
for cur in cursor:
    print(cur)
