# https://media.daum.net/cp/310
# data/daum_jtbc.html
# 뉴스제목, 뉴스요약 , 많이본 뉴스 추츨

import requests
import lxml.html

url = 'https://media.daum.net/cp/310'
res = requests.get(url)
html = res.text
root = lxml.html.fromstring(html)

news_title=[]
news_desc=[]


# 뉴스 제목
print('뉴스제목 \r\n')

# for part_html in root.xpath('//strong[@class="tit_thumb"]/a'):
#     print(part_html.text_content())

# for part_html in root.cssselect('ul.list_news2 li div strong a'):
#    print(part_html.text_content().strip())

#뉴스 요약
print('뉴스요약 \r\n')
# for part_html in root.xpath('//div[@class="desc_thumb"]/span'):
#     print(part_html.text_content().strip())

# for part_html in root.cssselect('div.desc_thumb span'):
#    print(part_html.text_content().strip())


# 위 제목 , 요약 따로 따로 놀음 => list로 제목 요약 1:1로 만들기
print('제목 + 요약 \r\n')
for part_html in root.cssselect('ul.list_news2 li div strong a'):
   news_title.append(part_html.text_content())

for part_html in root.xpath('//div[@class="desc_thumb"]/span'):
   news_desc.append(part_html.text_content());

for i in range(0,15):
    print(news_title[i])
    print(news_desc[i])
    print('\r\n')

# 많이 본 뉴스
print('많이 본 뉴스 !! \r\n');
for part_html in root.xpath('//div[@class="aside_g aside_ranking"]/ul/li/div/ol/li/strong/a'):
    print(part_html.text_content().strip())


# //*[@id="mAside"]/div[4]/ul/li[1]/div/ol[1]/li[1]/strong/a
# //*[@id="mArticle"]/div[2]/ul/li[1]/div/div/span
# //*[@id="mAside"]/div[4]/ul/li[1]/div/ol[1]/li[1]/strong/a