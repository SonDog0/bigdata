# https://news.naver.com
# data/naver_new.html
# 뉴스제목
# 정규 표현식에서 특수기호는 '\기호'로 검색

import  sys
import re
from urllib.request import urlopen
from html import unescape

f = urlopen('https://news.naver.com')
encode = f.info().get_content_charset()
text = f.read().decode(encode)


with open('data/naver_new.html', 'w', encoding=encode) as out:
    out.write(text)

with open('data/naver_new.html', 'r', encoding=encode) as i:
    html = i.read()



for part_html in re.findall(r'<strong.*?</strong>', html, re.DOTALL):
    # print(part_html)
    title = re.sub(r'<.*?>', '', part_html)
    title = re.sub(r'\".*?\"', '', title)
    title = re.sub(r'&quot', '', title)
    title = re.sub(r'.*?&middot;', '', title)

    print(title)

