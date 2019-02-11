# http://www.yes24.com/24/category/bestseller
# data/yes24_best.html
# 도서제목 추출
# 정규 표현식에서 특수기호는 '\기호'로 검색

import  sys
import re
from urllib.request import urlopen
from html import unescape

f = urlopen('http://www.yes24.com/24/category/bestseller')
encode = f.info().get_content_charset()
text = f.read().decode(encode)


with open('data/yes24_best.html', 'w', encoding=encode) as out:
    out.write(text)

with open('data/yes24_best.html', 'r', encoding=encode) as i:
    html = i.read()


for part_html in re.findall(r'<p class="copy"><a.*?</p>', html, re.DOTALL):
    title = re.sub(r'<.*?>', '', part_html)
    print(title)

