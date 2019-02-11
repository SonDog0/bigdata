# https://www.naver.co.kr/search
# 검색 사이트에서 검색어를 입력한 결과에서 데이터 추출
# 즉, 질의문자열 querystring을 이용해서 검색하고
# 그 결과에서 필요한 데이터를 추출


import requests
import lxml.html


url = 'https://search.naver.com/search.naver'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
params = {'query' : 'html5'}
res = requests.get(url,headers=headers, params=params)
html = res.text
root = lxml.html.fromstring(html)
# 블로그
for part_html in root.cssselect('div.blog ul li dl dt a'):
    print(part_html.text_content(),part_html.get('href'))
print('\r\n')
for part_html in root.cssselect('div.cafe ul li dl dt a'):
    print(part_html.text_content(),part_html.get('href'))
print('\r\n')
for part_html in root.cssselect('div.sp_website ul li dl dt a'):
    print(part_html.text_content(),part_html.get('href'))



# for part_html in root.xpath('//div[@class="section1"]/div[@class="group1"]/table[@class="tbl_home"]/tbody/tr/th/a'):
#sp_blog_1 > dl > dt > a
#main_pack > div.sp_post.section > ul > li:nth-child(1) > dl > dt > a
# //*[@id="sp_blog_1"]/dl/dt/a