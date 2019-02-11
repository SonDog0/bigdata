# https://finance.naver.com/
# 환율, 금리, 유가, 금시세, 원자재


import requests
import lxml.html
exchange_name = []
exchange_content = []
interest_name = []
interest_content =[]
oilprice_name = []
oilprice_content = []




url = 'https://finance.naver.com'
res = requests.get(url)
html = res.text
root = lxml.html.fromstring(html)
# 환율 이름
for part_html in root.xpath('//div[@class="section1"]/div[@class="group1"]/table[@class="tbl_home"]/tbody/tr/th/a'):
    exchange_name.append(part_html.text_content())



# //*[@id="content"]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a

# 환율 내용
for part_html in root.xpath('//div[@class="section1"]/div[@class="group1"]/table[@class="tbl_home"]/tbody/tr/td'):
    exchange_content.append(part_html.text_content())

for i in range(0,4):
    print(exchange_name[i])
    print(exchange_content[i])

# 환율//*[@id="content"]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1]
print('\r\n')

#금리

for part_html in root.xpath('//div[@class="section1"]/div[@class="group3"]/table[@class="tbl_home"]/tbody/tr/th/a'):
    interest_name.append(part_html.text_content())
for part_html in root.xpath('//div[@class="section1"]/div[@class="group3"]/table[@class="tbl_home"]/tbody/tr/td'):
    interest_content.append(part_html.text_content())

for i in range(0,4):
    print(interest_name[i])
    print(interest_content[i])
print('\r\n')




#//*[@id="content"]/div[2]/div[1]/div[3]/table/tbody/tr[1]/th/a
# //*[@id="content"]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]

# 유가

for part_html in root.xpath('//div[@class="section2"]/div[@class="group1"]/table[@class="tbl_home"]/tbody/tr/th/a'):
    oilprice_name.append(part_html.text_content())

for part_html in root.xpath('//div[@class="section2"]/div[@class="group1"]/table[@class="tbl_home"]/tbody/tr/td'):
    oilprice_content.append(part_html.text_content())

for i in range(0,4):
    print(oilprice_name[i].strip())
    print(oilprice_content[i])
# //*[@id="content"]/div[2]/div[2]/div[1]/table/tbody/tr[1]/th/a
# //*[@id="content"]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]


