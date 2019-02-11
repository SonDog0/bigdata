# 한빛미디어 - store - 전체도서목록 정보를 스크래핑해서
# AllBooks 테이블에 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html

import pymysql

import requests
import soup as soup
from bs4 import BeautifulSoup
import re
import time
import csv
book_name = []

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}


res = requests.get(url,headers=headers)
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름


for pub in html.select('tbody tr td'):
    book_name.append(pub.text)


conn = pymysql.connect(host='13.209.88.188', user= 'son', password= '931027',db='SON_MARIADB', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

# sql 질의문 실행
# 테이블 생성
create_sql = 'create table AllBooks(pub varchar(50),bname varchar(70), auth varchar(50), pday date, bprice varchar(20))'
drop_sql = 'drop table AllBooks'

curs.execute(drop_sql)
curs.execute(create_sql)

# Insert
sql = 'insert into AllBooks values(%s,%s,%s,%s,%s)'

# 페이지 당 도서 정보 행수 확인
bookcnt = len(html.select('table tbody tr'))
print(bookcnt)


for i in range (0,bookcnt):

    curs.execute(sql, (book_name[i*5], book_name[i*5+1],book_name[i*5+2],book_name[i*5+3],book_name[i*5+4]))

#변경사항 서버에 적용하기
conn.commit()




#mysql connection 닫기
conn.close()

# 도서 정보를 스크래핑하는 또 다른 방법
brand = []

title = []
pub = []
pdate = []
price = []

for books in html.select('table tbody tr'):
    for brand in books.select('td:nth-of-type(1)'):
        print(brand.text)
    for title in books.select('td:nth-of-type(2)'):
        print(title.text)
    for pub in books.select('td:nth-of-type(3)'):
        print(pub.text)
    for pdate in books.select('td:nth-of-type(4)'):
        print(pdate.text)
    for price in books.select('td:nth-of-type(5)'):
        print(price.text)