# 한빛미디어 - store - 전체도서목록 정보를 스크래핑해서
# # data/allbooks.csv 파일에 저장
# # http://www.hanbit.co.kr/store/books/full_book_list.html

# 한빛 도서 - 새로나온도서 '웹'으로 검색 , 모든 페이지

import requests
from bs4 import BeautifulSoup
import re
import time
import csv
book_name = []


url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}


res = requests.get(url,headers=headers)
html = BeautifulSoup(res.text,'lxml')


for pub in html.select('tbody tr td'):
    book_name.append(pub.text)



# 페이지 당 도서 정보 행수 확인
bookcnt = len(html.select('table tbody tr'))
print(bookcnt)

# for i in range(0,100):
#     print(book_name[i])

out = open('data/allbooks.csv', 'w', encoding='utf-8',newline='')
mycsv = csv.writer(out)
for i in range(0,bookcnt):
    mycsv.writerow([book_name[i*5], book_name[i*5+1], book_name[i*5+2], book_name[i*5+3] , book_name[i*5+4]])


out.close()

