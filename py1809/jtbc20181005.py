# daum 뉴스 사이트에서 jtbc 뉴스 스크래핑하기
# http://media.daum.net/cp/310


import requests
from bs4 import BeautifulSoup
import re
import csv

title = []
sub = []


url = 'https://media.daum.net/cp/310?'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
# 뉴스 일자와 페이지 번호를 질의문자열 매개변수로 정의

page = 1
regDate = '20181005'
params = {'page': page, 'regDate':regDate}
res = requests.get(url,headers=headers,params=params)
# html = BeautifulSoup(res.text,'html.parser')
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

for a in html.select('div.box_etc ul li div.cont_thumb strong.tit_thumb a'):
    title.append(a.text)
for a in html.select('div.box_etc ul li div div span'):
    sub.append(a.text.strip())
length = len(sub)

for i in range(0,length):
    print(title[i])
    print(sub[i])
    print('\n')

out = open('data/jtbc20181005.csv', 'w', encoding='utf-8',newline='')
mycsv = csv.writer(out)

for i in range(0,length):
    mycsv.writerow([title[i],sub[i]])

out.close()