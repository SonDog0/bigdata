# 파이썬으로 MySQL, MariaDB 다루기
# python에서 MySQL 데이터베이스를 지원하려면
# python DB API 규약에 맞게 작성된 mySQL DB 모듈 필요
# 일반적으로 pyMySQL 모듈을 많이 사용

import pymysql

# # mysql connection 생성
# conn = pymysql.connect(host='13.209.88.188', user= 'son', password= '931027',db='SON_MARIADB', charset='utf8')
#
# curs = conn.cursor()
#
# curs.execute('DROP TABLE items')
# curs.execute('''create table items( item_id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, price INTEGER)''' )
# # sql 질의문 실행
# sql = 'select * from books'
# curs.execute(sql)
#
# # 결과 집합 처리
# for rs in curs.fetchall():
#     print(rs[0], rs[1], rs[2], rs[3])  #배열 기반 커서
#
#
#
#
# #mysql connection 닫기
# conn.close()



# # mysql connection 생성
# conn = pymysql.connect(host='13.209.88.188', user= 'son', password= '931027',db='SON_MARIADB', charset='utf8')
# # connection 으로부터 dict cursor 생성
# curs = conn.cursor(pymysql.cursors.DictCursor)
#
# # sql 질의문 실행
# sql = 'select * from books'
# curs.execute(sql)
#
# # 결과 집합 처리
# for rs in curs.fetchall():
#     print(rs['bno'], rs['bname'], rs['bpub'], rs['bprice'])  #사전기반 커서
#
# #mysql connection 닫기
# conn.close()


# 1~100 까지 2배수, 3배수, 5배수 저장
# 테이블 이름은 numbers
# 필드는 no, no2, no3, no5


# mysql connection 생성
conn = pymysql.connect(host='13.209.88.188', user= 'son', password= '931027',db='SON_MARIADB', charset='utf8')
# connection 으로부터 cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

# sql 질의문 실행
create_sql = 'create table numbers( no2 int, no3 int, no5 int )'
drop_sql = 'drop table numbers'
sql = 'insert into numbers values(%s,%s,%s)'

# sql = 'select * from books'
curs.execute(drop_sql)
curs.execute(create_sql)


# 1~ 100까지 2배수, 3배수, 5배수
num1 = 0
num2 = 0
num3 = 0

for i in range (1,101):
    if i % 2 == 0:
        num1 = i
    else:
        num1 = 0

    if i % 3 == 0:
        num2 = i
    else:
        num2 = 0

    if i % 5 == 0:
        num3 = i
    else:
        num3 = 0

    curs.execute(sql, (num1, num2, num3))

#변경사항 서버에 적용하기
conn.commit()


# 결과 집합 처리
select_sql = 'select * from numbers'
curs.execute(select_sql)


for rs in curs.fetchall():
    print(rs['no2'], rs['no3'], rs['no5'])  #사전기반 커서

#mysql connection 닫기
conn.close()




