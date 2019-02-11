# 다음 증권, 코스피(상승, 하락, 순매수, 거래량, 시가총액)
# http://finance.daum.net/index.daum?nil_profile=stockgnb&nil_menu=stock_top

import requests
from bs4 import BeautifulSoup
import re

stock_name=[]
stock_price=[]
stock_perc=[]
stock_title=['상승률','하락률','외국인순매수','기관순매수','거래량','시가총액']

url ='http://finance.daum.net/index.daum?nil_profile=stockgnb&nil_menu=stock_top'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url,headers=headers)
# html = BeautifulSoup(res.text,'html.parser')
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

for a in html.select('div.section_features div div.info_kospi ol li span.tit_rank a'):
    print(a.text)
    stock_name.append(a.text)

for a in html.select('div.section_features div div.info_kospi ol li span.cont_result a span.num_features'):
    price = re.sub(r'주가','',a.text)
    print(price)
    stock_price.append(price)

for a in html.select('div.section_features div div.info_kospi ol li span.cont_result span.num_cont'):
    print(a.text)
    stock_perc.append(a.text)

print('----------------------------------결 과 ----------------------------------')
j = 0
for i in range(0,len(stock_title)):
    if(i%3 == 0):
        print(stock_title[j])
        j = j +1
    print(stock_name[i],stock_price[i],stock_perc[i])




        







# for a in html.select('div.price strong.book_price'):
#     book_price.append(a.text)
#
# for i in range(0,20):
#     print(book_name[i], book_price[i])
#

#main_contents > ul > li:nth-child(7) > div.detail > div.title > a > strong
# #cEtc > div.section_features > div:nth-child(2) > div.info_kospi > ol > li:nth-child(1) > span.cont_result > a > span
#cEtc > div.section_features > div:nth-child(2) > div.info_kospi > ol > li:nth-child(1) > span.cont_result > span