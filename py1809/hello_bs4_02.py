# 교보문고 베스트셀러, 도서제목, 가격
# http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79

import requests
from bs4 import BeautifulSoup
book_name = []
book_price = []



url ='http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url,headers=headers)
# html = BeautifulSoup(res.text,'html.parser')
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

for a in html.select('div.title a strong'):
    book_name.append(a.text)


for a in html.select('div.price strong.book_price'):
    book_price.append(a.text)

for i in range(0,20):
    print(book_name[i], book_price[i])

# book_name.append(html.select('div.title a strong').text)
#
# print(book_name[0])
# #
# print(soup.select("li:nth-of-type(" + "1" + ")a.body._goPost div.pTxt").text)
# print(soup.select("li:nth-of-type(" + "2" + ")a.body._goPost div.pTxt").text)


#main_contents > ul > li:nth-child(7) > div.detail > div.title > a > strong
##main_contents > ul > li:nth-child(7) > div.detail > div.price > strong