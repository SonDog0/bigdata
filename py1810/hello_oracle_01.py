# 파이썬으로 오라클 다루기
# 파이썬용 오라클 라이브러리 cx_Oracle 설치
# oracle instant client : Oracle Client Library
# https://www.oracle.com/technetwork/topics/winx64soft-089540.html
# Basic Package / SQL*Plus 다운로드
# instatn client Library 설치 경로를 윈도우 환경변수 PATH로 설정
# pycharm 재시작

# cx_Oracle에서 한글처리를 하려면 반드시 NLS 환경변수 지정

import cx_Oracle
import os

# 한글 처리를 위해 NLS 환경변수 설정
os.putenv('NLS_LANG', '.UTF8')
# os.putenv('NLS_LANG', '.KO16KSC5601')

# #oracle connection 생성
# conn = cx_Oracle.connect('son','931027','13.209.88.188/xe')
#
#
#
#
# # 오라클 설치 버전 확인
# # print(conn.version)
# # print(cx_Oracle.clientversion())
#
# # connection 으로 부터 cursor 생성
# curs = conn.cursor()
#
# # sql 질의문 실행
# sql = 'select * from books'
# curs.execute(sql)
#
# # 결과집합 처리
#
# for rs in curs.fetchall():
#     print(rs)
#
# #oracle connection 닫기
# conn.close()


conn = cx_Oracle.connect('son','931027','13.209.88.188/xe')
curs = conn.cursor()

# sql 질의문 실행

drop_sql = 'drop table numbers'
create_sql = 'create table numbers(idx number, no2 number, no3 number ,no5 number)'
curs.execute(drop_sql)
curs.execute(create_sql)

for i in range(1,101):
    insert_sql = 'insert into numbers values(:idx,:no2,:no3,:no5)'
    curs.execute(insert_sql,idx=i,no2=i*2,no3=i*3,no5=i*5)
# insert_sql = 'insert into numbers values(%s,%s,%s,%s)'
# curs.execute(insert_sql,1,2,3,4)
conn.commit()
# 결과집합 처리
# for rs in curs.fetchall():
#     print(rs)

#oracle connection 닫기
conn.close()
