# http://www.yes24.com/24/category/bestseller
# data/yes24_best.html
# 도서제목 추출 : //*[@id="bestList"]/ol/li[1]/p[1]/a #bestList > ol > li.num1 > p.copy > a

import requests
import lxml.html

url = 'http://www.yes24.com/24/category/bestseller'
res = requests.get(url)
html = res.text
root = lxml.html.fromstring(html)

for part_html in root.xpath('//ol/li/p[3]/a'):
    print(part_html.text_content())

# for part_html in root.cssselect('ol li p:nth-child(3) a')

