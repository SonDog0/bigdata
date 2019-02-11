# http://www.hanbit.co.kr/store/books/full_book_list.html
# 크롤링한 결과 : data/store_full_list.html

import  sys
import re
from urllib.request import urlopen
from html import unescape

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
encode = f.info().get_content_charset()
print(encode)


text = f.read().decode(encode)
print(text)


with open('data/store_full_list.html', 'w', encoding=encode) as out:
    out.write(text)