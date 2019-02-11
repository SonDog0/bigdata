# 한빛 도서 - 새로나온도서 '웹'으로 검색 , 모든 페이지

import requests
from bs4 import BeautifulSoup
import re
import time


url = 'http://www.hanbit.co.kr/store/books/new_book_list.html?'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

# 뉴스 목록 총 페이지 파악
page = 1
keyWord = '웹'
searchKey = 'all'
params = {'page': page, 'keyWord':keyWord ,'searchKey': searchKey}
res = requests.get(url,headers=headers, params=params)
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름
lastpage = html.select('div.new_book_list_wrap div.paginate a')[-1]
end =int(lastpage.text)
print(end)

# 총 페이지 만큼 출력

for i in range(1,end+1):
    page = i
    keyWord = '웹'
    searchKey = 'all'
    params = {'page': i, 'keyWord': keyWord, 'searchKey': searchKey}

    res = requests.get(url, headers=headers, params=params)
    html = BeautifulSoup(res.text, 'lxml')  # 가볍고 처리가 빠름
    for a in html.select('p.book_tit a'):
        print(a.text)
    print('\r\n')
    time.sleep(1)



# container > div.new_book_list_wrap > div.sub_book_list_area > li:nth-child(1) > div > div > p.book_tit > a
#container > div.new_book_list_wrap > div.paginate > a:nth-child(3)


