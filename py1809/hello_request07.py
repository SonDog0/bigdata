# https://kr.investing.com/currencies/streaming-forex-rates-majors
# 주요 통화간 환율
# 주의! 무분별한 스크래핑은 접속차단의 위험 !
# 특정 사이트는 스크래핑이나 크롤링을 막기 위한 방편으로 사이트에 접속하는 사용자의 user-agent를 확인함
# UA없이 사이트 접속을 시도하면 접속 권한 거부의 의미로
# 403 응답코드와 함께 거부신호를 보냄


import requests
import lxml.html
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

url = 'https://kr.investing.com/currencies/streaming-forex-rates-majors'
res = requests.get(url,headers=headers)
html = res.text
root = lxml.html.fromstring(html)

currency =[]


for part_html in root.cssselect('table.closedTbl tbody tr td'):
    # print(part_html.text_content().strip())
    currency.append(part_html.text_content().strip())

# 통화종목 한글, 통화종목 영어, 매도, 매수, 변동%, 시간

for i in range(0,41):
    print(currency[i*10+1],currency[i*10+2],currency[i*10+3],currency[i*10+4],currency[i*10+8],currency[i*10+9] )


