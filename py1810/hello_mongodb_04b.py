import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient,DESCENDING,ASCENDING
import datetime
from bson.objectid import ObjectId



client = MongoClient('mongodb://13.124.214.229:7185')

db = client.son
coll = db.restaurants
#
# print('전체데이터 조회')
# for rest in coll.find():
#     print(rest)

# 데이터 조회 - 부분키 출력
# 음식점 정보 중 id , borough , cuisine , name 만 출력
# cursor = coll.find({},{'id':1 , 'borough':1,'cuisine':1,'name':1} )
#
# for rest in cursor:
#     print(rest)

# 데이터 조회 - 출력 범위 지정
# cursor = coll.find({},{'id':1 , 'borough':1,'cuisine':1,'name':1} ).limit(5).sort('borough' ,DESCENDING)
#
# for rest in cursor:
#     print(rest)


# 데이터 조회 - 일정 범위만큼 데이터 제외후 출력
# 알파벳 정렬 후 2번째 , 3번째 음식점만 출력
# cursor = coll.find().sort('borough',ASCENDING).skip(1).limit(2)
#
# for rest in cursor:
#     print(rest)


# 집계함수 이용
# 총 음식점 수 출력
param = [ {'$group' : {'_id' : '총음식점수', 'total' : {'$sum' : 1  } }  } ]
value = list(coll.aggregate( param ))

print(value[0]['total'])

client.close()

