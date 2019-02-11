import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient,DESCENDING,ASCENDING
import datetime
from bson.objectid import ObjectId



client = MongoClient('mongodb://13.124.214.229:7185')

db = client.son
coll = db.restaurants


# 1. 모든 음식점을 조회하라
# cursor = coll.find()
# for cur in cursor:
#     print(cur)
# 2. 맨하튼Manhattan 자치구borough에 있는 모든 음식점을 조회하라
#
# cursor = coll.find({'borough' : 'Manhattan'})
# for cur in cursor:
#     print(cur)

# 3.우편번호가 10075인 음식점을 조회하고, 그 갯수도 출력하라
#
# cursor = coll.find({'address.zipcode' : '10075'})
# for cur in cursor:
#     print(cur)

# 4.

# cursor = coll.find({'grades.grade' : 'B'})
# for cur in cursor:
#     print(cur)

# 4-1 : 첫번째 등급이 C인 음식점 조회
# cursor = coll.find({'grades.0.grade' : 'C'})
# for cur in cursor:
#     print(cur)

# 5. 음식점 평점이 30보다 큰 음식점을 조회하고, 그 갯수도 출력하라

# cursor = coll.find({'grades.score' : {'$gt' : 30} })
# for cur in cursor:
#     print(cur)

# 6.  음식점 평점이 10보다 낮은 음식점을 조회하고, 그 갯수도 출력하라
#
# cursor = coll.find({'grades.score' : {'$lt' : 10} })
# for cur in cursor:
#     print(cur)


# 7.우편번호가 10075인 이탈리안Italian 요리cuisine 음식점을 조회하고, 그 갯수도 출력하라

# cursor = coll.find({'address.zipcode' : '10075' , 'cuisine' : 'Italian'})
# for cur in cursor:
#     print(cur)


# 8.우편번호가 10075이거나, 이탈리안Italian 요리cuisine 음식점을 조회하고, 그 갯수도 출력하 라

# cursor = coll.find({'$or' : [ {'address.zipcode' : '10075'} , {'cuusine' : 'Italian'} ] } )
# for cur in cursor:
#     print(cur)

# 9 이름이 ‘Juni’인 음식점을 찾아서 요리cuisine를 ‘American (New)’으로 변경하라

# cursor = coll.update({'name' : 'Juni'}, {'$set'} )
# for cur in cursor:
#     print(cur)

# 10
# 11
# 12
# 13  자치구borough별 음식점 개수를 조회하라 ( 파이프라인 / 리스트 / [] 사용]
# cursor = coll.aggregate( [ { '$group' : {'_id' : '$borough' , '자치구별음식점수' : {'$sum' : 1 }} } ])
# for cur in cursor:
#     print(cur)
#
# values = list(cursor)
# # 다른방법
# for i in range( 0 ,len(values)):
#     print(values[i]['_id'])
#     print(values[i]['자치구별음식점수'])

# 14  Queens 자치구 내 Brazilian 요리 음식점이 구역별zipcode로 얼마나 존재하는지 조회하라
# cursor = coll.aggregate( [
#     {'$match' : {'borough' : 'Queens' , 'cuisine' : 'Brazilian'}},
#     {'$group' : {'_id' : '$address.zipcode' , '우편번호별음식점수' : {'$sum' : 1 }} }
#                            ] )
# for cur in cursor:
#     print(cur)

client.close()