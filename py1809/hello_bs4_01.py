#beatifulsoup4로 스크래핑 하기
import requests
from bs4 import BeautifulSoup





url ='http://www.hanbit.co.kr/store/store_submain.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url,headers=headers)
# html = BeautifulSoup(res.text,'html.parser')
html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

# print(html) # 들여쓰기가 안되어 불편
# print(html.prettify()) # 들여쓰기 적용 - 보기좋게 출력

# 스크래핑한 문서에서 title 요소의 텍스트만 출력
print(html.title)
print(html.title.string)

# 스크래핑한 문서에서 p요소 추출
print(html.p)
print(html.p['class'])
# 스크래핑한 문서에서 a요소 추출
print(html.a)

#스크래핑한 문서에서 모든 p, a 요소 추출
print(html.find_all('p'))
print(html.find_all('a'))

#도서 제목 가져오기
for a in html.select('p.book_tit a'):
    print(a.text,a.get('href'))


