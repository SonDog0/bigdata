import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient,DESCENDING,ASCENDING
import datetime
from bson.objectid import ObjectId

# zipcode


client = MongoClient('mongodb://13.124.214.229:7185')

db = client.son
coll = db.zipcode

# 1 우편번호 데이터 수를 조회
# cursor  = coll.find({})
# print(cursor.count())

# 2 'MA' 주State를 조회
# cursor = coll.find({'state' : 'MA'})
# for cur in cursor:
#     print(cur)

# 3 'NY' 주State, New York 시City를 조회
# cursor = coll.find({'state' : 'NY' , 'city' : 'NEW YORK'})
# for cur in cursor:
#     print(cur)

# 4 'NY' 주State 또는 New York 시City를 조회
# cursor = coll.find({'$or' : [{ 'state' : 'NY' },{'city' : 'NEW YORK'} ]})
# for cur in cursor:
#     print(cur)

# 5 인구 수pop가 100,000이상인 지역을 조회
# cursor = coll.find({'pop' : {'$gte' : 100000}})
# for cur in cursor:
#     print(cur)

# 6 전지역의 총 인구수를 조회
# cursor = coll.aggregate( [{'$group' : { '_id' :'' , '총인구수' : {'$sum' : '$pop' }} }])
# for cur in cursor:
#     print(cur)

# 7 각 지역state별 인구수를 조회(aggregate 이용 - $group, $sum)
#
# cursor = coll.aggregate( [{'$group' : { '_id' :'$state' , '주별인구수' : {'$sum' : '$pop' }} }])
# for cur in cursor:
#     print(cur)

# 8 각 도시city 별 인구수 조회
# cursor = coll.aggregate( [{'$group' : { '_id' :'$city' , '시별인구수' : {'$sum' : '$pop' }} }])
# for cur in cursor:
#     print(cur)

# 9 인구 수가 50,000이상인 도시를 조회(aggregate 이용 - $match)
# cursor = coll.aggregate( [{ '$match' : { 'pop' : {'$gte' : 50000}}}])
# for cur in cursor:
#     print(cur)


# 10 인구수가 천만 이상인 도시를 조회
# cursor = coll.aggregate( [
#     {'$group' : {'_id' : '$state', '주별인구수' : {'$sum' : '$pop' } } },
#     {'$match' : { '주별인구수' : {'$gte' : 10000000}}} ])
# for cur in cursor:
#     print(cur)

# 11 'NY' 지역의 인구수를 조회하세요

# cursor = coll.aggregate([
# {'$group' : {'_id' : '$state', '주별인구수' : {'$sum' : '$pop' } } },
# {'$match' : { '_id' : 'NY'}} ])
# for cur in cursor:
#     print(cur)



db.zipcode.find({'name' : 'son'}, {'$name : 1 '})

