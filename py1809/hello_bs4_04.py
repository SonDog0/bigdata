# daum 뉴스 사이트에서 jtbc 뉴스 스크래핑하기
# http://media.daum.net/cp/310


import requests
from bs4 import BeautifulSoup
import re



url = 'https://media.daum.net/cp/310?'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
# 뉴스 일자와 페이지 번호를 질의문자열 매개변수로 정의

page = 1
regDate = '20180917'
params = {'page': page, 'regDate':regDate}
res = requests.get(url,headers=headers,params=params)
# html = BeautifulSoup(res.text,'html.parser')
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

for a in html.select('div.box_etc ul li div.cont_thumb strong.tit_thumb a'):
    print(a.text)



#mArticle > div.box_etc > ul > li:nth-child(1) > div > strong > a

# 뉴스 목록 총 페이지 파악
res = requests.get(url,headers=headers)
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름
lastpage = html.select('span.inner_paging a')[-1]
print(lastpage.text)
end = int(lastpage.text)
print(end)


# 특정일자 뉴스 제목, 요약을 모두 스크래핑 하기
# 각 일자별 뉴스 총 페이지를 파악

for i in range(1,end):
    page = i
    regDate = '20180917'
    params = {'page': i, 'regDate':regDate}
    res = requests.get(url,headers=headers,params=params)
    # html = BeautifulSoup(res.text,'html.parser')
    html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

    for a in html.select('div.box_etc ul li div.cont_thumb strong.tit_thumb a'):
        print(a.text)

    print('\r\n')




#mArticle > div.box_etc > div > span > em


# #mArticle > div.box_etc > div > span > em
