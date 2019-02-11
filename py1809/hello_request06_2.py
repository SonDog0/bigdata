
# https://finance.naver.com/
# 환율, 금리, 유가, 금시세, 원자재

import requests
import lxml.html

url = 'https://finance.naver.com/'
res = requests.get(url)
html = res.text
root = lxml.html.fromstring(html)
title = []
updown = []


#환율

for part_html in root.cssselect('div.group1 table tbody tr th'):
    # print('' + part_html.text_content().strip() + '\r\n')
    title.append(part_html.text_content().strip())

for part_html in root.cssselect('div.group1 table tbody tr td'):
    # print('' + part_html.text_content().strip() + '\r\n')
    updown.append(part_html.text_content().strip())

# for i in range(0,4):
#     print(title[i],updown[i*2] , updown[i*2 + 1])
# print('\r\n')
#
# for i in range(4,8):
#     print(title[i],updown[i*2] , updown[i*2 + 1])

for part_html in root.cssselect('div.group2 table tbody tr th a'):
    title.append(part_html.text_content().strip())

for part_html in root.cssselect('div.group2 table tbody tr td'):
    # print('' + part_html.text_content().strip() + '\r\n')
    updown.append(part_html.text_content().strip())

for i in range(8,14):
    print(title[i],updown[i*2] , updown[i*2 + 1])
print('\r\n')


# 금리 원자재 SKIP !!




# content > div.article2 > div.section1 > div.group1 > table > tbody > tr.down.bold > th
# #content > div.article2 > div.section1 > div.group2 > table > tbody > tr:nth-child(1) > th > a
# #content > div.article2 > div.section1 > div.group2 > table > tbody > tr:nth-child(1) > td:nth-child(2)