# 네이버 쇼핑
# 랭킹
import requests
from bs4 import BeautifulSoup
shopping_rank = []



url ='https://search.shopping.naver.com/search/all.nhn?origQuery=%EC%97%AC%EC%84%B1%EC%9D%98%EB%A5%98&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EC%97%AC%EC%84%B1%EC%9D%98%EB%A5%98'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
for i in range(1,10):
    params = {'pagingIndex': i}
    res = requests.get(url,headers=headers,params=params)
    # html = BeautifulSoup(res.text,'html.parser')
    html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

    for a in html.select('span.depth a'):
        shopping_rank.append(a.text)



for i in range(len(shopping_rank)):
    print(shopping_rank[i])

f = open('./shopping_ranking.txt', 'a', encoding='UTF-8')
for i in range(0, len(shopping_rank)):
    f.write(shopping_rank[i])
    f.write('\n')
