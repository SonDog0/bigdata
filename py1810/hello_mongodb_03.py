# 한빛미디어 -store - 새로나온책
# http://www.hanbit.co.kr/store/books/new_book_list.html
# 제목, 저자 가격 , 생성일 추출해서 new_books 컬렉션에 저장

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime



book_name = []
author = []
price = []
book_json = []


url = 'http://www.hanbit.co.kr/store/books/new_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url,headers=headers)
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

for a in html.select('p.book_tit a'):
    book_name.append(a.text)

for a in html.select('p.book_writer'):
    author.append(a.text)

for a in html.select('span.price'):
    price.append(a.text)





for i in range(0,len(book_name)):
    book_json.append({ "bookname" : book_name[i] , 'author' :  author[i],  'price' : price[i] , 'date' : datetime.datetime.utcnow() })

client = MongoClient('mongodb://13.124.214.229:7185')

db = client.hellomongo
coll = db.new_books
coll.drop()
coll.insert_many(book_json)

#container > div.new_book_list_wrap > div.sub_book_list_area > li:nth-child(1) > div > div > p.book_writer
#container > div.new_book_list_wrap > div.sub_book_list_area > li:nth-child(1) > div > div > p.book_tit > a
#container > div.new_book_list_wrap > div.sub_book_list_area > li:nth-child(1) > div > span > span > span.price