import sys
import re

from urllib.request import urlopen
from html import unescape

with open('data/store_full_list.html', 'r', encoding='utf-8') as f:
    html =f.read()



for part_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    # print(part_html)
    title = re.sub(r'<.*?>','', part_html)
    title = re.sub(r'&#41;',')',title)
    title = re.sub(r'&#40;','(',title)
    print(title)


