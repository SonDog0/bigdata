# python을 이용한 mongodb 접속 테스트
# AWS에 설치한 mongodb에 접속
# hellomongo 데이터베이스에 있는 컬렉션 조회


from pymongo import MongoClient

#mongodb 연결 객체 만들기

# client = MongoCilent('','') # 접속 주소 , 포트

client = MongoClient('mongodb://13.124.214.229:7185')

# DB 객체 가져오기
# db = client['hellomongo']
db = client.hellomongo

# Collection 객체 가져오기
# collection = db['students']
coll = db.students

# 전체 조회

for stud in coll.find():
    print(stud)

#접속 해제

client.close()




#문서 생성하기
#몽고디비 안애 데이터는 JSON으로 저장






