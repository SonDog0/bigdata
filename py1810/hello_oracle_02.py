# 한빛미디어 - store - 전체도서목록 정보를 스크래핑해서
# data/allbooks.csv 파일에 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html

import cx_Oracle
import os
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

os.putenv('NLS_LANG', '.UTF8')

conn = cx_Oracle.connect('son','931027','13.209.88.188/xe')
curs = conn.cursor()

drop_sql = 'drop table AllBooks'
create_sql = 'create table AllBooks(pub varchar2(50),bname varchar2(200), auth varchar2(50), pday varchar2(20), bprice varchar2(20))'
curs.execute(drop_sql)
curs.execute(create_sql)
insert_sql = 'insert into AllBooks values(:pub,:bname,:auth,:pday, :bprice )'

bookcnt = len(html.select('table tbody tr'))
print(bookcnt)

for i in range(0,bookcnt):
    curs.execute(insert_sql, pub=book_name[i*5], bname=book_name[i*5+1], auth=book_name[i*5+2],pday=book_name[i*5+3],bprice=book_name[i*5+4])

conn.commit()

conn.close()