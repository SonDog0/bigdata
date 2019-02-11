# https://www.google.co.kr/search?q=검색어
# 검색 사이트에서 검색어를 입력한 결과에서 데이터 추출
# 즉, 질의문자열 querystring을 이용해서 검색하고
# 그 결과에서 필요한 데이터를 추출


import requests
import lxml.html


url = 'https://www.google.co.kr/search'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
params = {'q' : 'html5'}
res = requests.get(url,headers=headers, params=params)
html = res.text
root = lxml.html.fromstring(html)

for part_html in root.cssselect('h3.r a'):
    print(part_html.text_content(),part_html.get('href'))



#main_contents > ul > li:nth-child(21) > div.detail > div.author > span.popup_load.uxOpenList