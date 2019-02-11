# 한빛미디어 -store - 전체 도서 목록을
# json 형식(allbooks.json)으로 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html
# brand , title , publish , pdate , price

import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

brand = []
title = []
pub = []
pdate = []
price = []

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}


res = requests.get(url,headers=headers)
html = BeautifulSoup(res.text,'lxml')



for books in html.select('table tbody tr'):
    for data in books.select('td:nth-of-type(1)'):
                brand.append(data.text)
    for data in books.select('td:nth-of-type(2)'):
                title.append(data.text)
    for data in books.select('td:nth-of-type(3)'):
                pub.append(data.text)
    for data in books.select('td:nth-of-type(4)'):
                pdate.append(data.text)
    for data in books.select('td:nth-of-type(5)'):
                price.append(data.text)



allbooks = OrderedDict()
books = []
for i in range(0,10):
    book = OrderedDict()
    book['brand']= brand[i]
    book['title']= title[i]
    book['pub']= pub[i]
    book['pdate'] = pdate[i]
    book['price'] = price[i]
    allbooks[i]=book

# for i in range(0,10):
#     print(books[i])
print(json.dumps(allbooks,ensure_ascii=False,indent=2))

with open('data/allbooks.json','w',encoding='utf-8') as out:
    json.dump(allbooks,out,ensure_ascii=False,indent=2)


