# 교보문고 베스트셀러, 도서제목, 가격
# http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79

import requests
from bs4 import BeautifulSoup
import re
import lxml.html
import csv
book_name = []
book_auth = []
book_price = []



url ='http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url,headers=headers)

html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름
html2 = res.text
root = lxml.html.fromstring(html2)


# html2 = res.text
# root = lxml.html.fromstring(html2)
cnt = 0
for a in html.select('div.title a strong'):
    book_name.append(a.text)


# for part_html in root.xpath('//*[@id="main_contents"]/ul/li[3]/div[2]/div[3]/text1]'):
#     print(part_html.text_content()

for a in html.select('div ul li div.detail div.author'):
    # td: nth - of - type(1)
    # main_contents > ul > li:nth-child(7) > div.detail > div.author
    # temp = a.get_text().strip()

    # book_auth.append(a.text.strip()[0] + a.text.strip()[1] + a.text.strip()[2])
    temp = re.sub(r'\s+', '', a.text)
    # temp = re.findall(r'\w+|',a.text)

    book_auth.append(temp)





for a in html.select('div.price strong.book_price'):
    book_price.append(a.text)

length = len(book_name)


#
# for i in range (0,book_name):
#     print(book_auth[i])

out = open('data/kyobobest.csv', 'w', encoding='utf-8',newline='')
mycsv = csv.writer(out)

for i in range(0,length):
    mycsv.writerow([book_name[i],book_auth[i],book_price[i]])

out.close()

