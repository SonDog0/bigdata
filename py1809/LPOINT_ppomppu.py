from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from datetime import datetime
from konlpy.tag import Twitter



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

temp = []

for i in range (1,372):
    url = 'http://www.ppomppu.co.kr/search_bbs.php?search_type=sub_memo&page_no='+str(i)+'&keyword=%B7%D4%B5%A5%C8%A8%BC%EE%C7%CE&page_size=20&bbs_id=&order_type=date&bbs_cate=1'

    res = requests.get(url, headers=headers)
    html = BeautifulSoup(res.text, 'lxml')

    #result-tab1 > form > div:nth-child(1) > div > span > a


    for a in html.select('form div div span a'):
        temp.append(a.text)

    sleep(5)

for i in range(0,len(temp)):
    print(temp[i])


f = open('./ppomppu3.txt','a' , encoding='UTF-8')
for i in range(0,len(temp)):
    f.write(temp[i])
    f.write('\n')