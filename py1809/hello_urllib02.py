import sys
import re

from urllib.request import urlopen
from html import unescape

with open('data/store_main.html', 'r', encoding='utf-8') as f:
    html =f.read()

# data 폴더의 store_main.html 파일을 'read'모드로 열어서 utf-8로 인코딩하여 f에 저장
# html 변수에 f의 내용을 저장

# print(html)

# 도서 제목을 추출하기 위해 정규표현식을 이용함
# python 정규표현식 패키지는 re
# re.findall(r'찾을내용', 대상, 찾을범위)
# re.sub(r'찾을내용', 바꿀문자, 대상)


for part_html in re.findall(r'<p class="book_tit"><a.*?</p>', html, re.DOTALL):
    print(part_html)
    # title = re.sub(r'<.*?>','', part_html)
    # print(title)









