# yes24 '빅데이터'로 검색 , 'IT 모바일', '신상품' 순으로 정렬해서 3페이지
# 한글문자 => URL 질의 문자열로 변환 dencode.com
# yes24는 EUC-KR로 되어있어서 질의문을 UTF-8로 맞게 변환 해줘야함


import requests
from bs4 import BeautifulSoup
import re

# 검색어를 미리 EUC-KR 인코딩해서 질의문자열에 포함
# url = 'http://www.yes24.com/searchcorner/Search?query=%BA%F2%B5%A5%C0%CC%C5%CD'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
# sort_gb ='RECENT_DATE'
# scode='009_003'
# disp_no ='001001003'
# domain ='book'
#
# for i in range(1,4):
#     PageNumber = i
#     params = {'PageNumber': i , 'sort_gb': sort_gb, 'scode': scode, 'disp_no' : disp_no, 'domain' : domain}
#     res = requests.get(url, headers=headers,params=params)
#     html = BeautifulSoup(res.text, 'lxml')  # 가볍고 처리가 빠름
#     for a in html.select('td.goods_infogrp p.goods_name a strong'):
#         print(a.text)
#     print('\r\n')

#검색어를 인코딩
url = 'http://www.yes24.com/searchcorner/Search?'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
key = '빅데이터'
keyWord =key.encode('euc-kr')
sort_gb ='RECENT_DATE'
scode='009_003'
disp_no ='001001003'
domain ='book'

for i in range(1,4):
    PageNumber = i
    params = {'PageNumber': i , 'sort_gb': sort_gb, 'scode': scode, 'disp_no' : disp_no, 'domain' : domain, 'query' : keyWord}
    res = requests.get(url, headers=headers,params=params)
    html = BeautifulSoup(res.text, 'lxml')  # 가볍고 처리가 빠름
    for a in html.select('td.goods_infogrp p.goods_name a strong'):
        print(a.text)
    print('\r\n')



 # schMid_wrap > div:nth-child(4) > div.goodsList.goodsList_list > table > tbody > tr:nth-child(1) > td.goods_infogrp > p.goods_name.goods_icon > a > strong
 # #schMid_wrap > div:nth-child(4) > div.goodsList.goodsList_list > table > tbody > tr:nth-child(1) > td.goods_infogrp > p.goods_name.goods_icon > a > strong