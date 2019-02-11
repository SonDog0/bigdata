# http://news.naver.com
# data/naver_news.html
# 뉴스제목 추출

# //ul.newsnow_txarea li div a strong
# //ul[@class="mlist2 no_bg"]/li/a/strong
#  ul > li:nth-child(1) > a > strong

import requests
import lxml.html

url = 'http://news.naver.com'
res = requests.get(url)
html = res.text
root = lxml.html.fromstring(html)

# for part_html in root.cssselect('ul.newsnow_txarea li div a strong'):
#     print(part_html.text_content())
cnt = 1 # 출력 횟수 지정

for part_html in root.xpath('//ul[@class="mlist2 no_bg"]/li/a/strong'):
    print(part_html.text_content())


    if cnt % 5 == 0: print('\r\n')
    cnt = cnt + 1;



# 탑 주요뉴스
# # # 인절미 //*[@id="pan_today_main_news"]/div[1]/div/a/div[2]
# for part_html in root.xpath('//p[@class ="nowsnow_img_mask_p"]'):
#     print(part_html.text_content())

for part_html in root.cssselect('p.newsnow_img_mask_p'):
    print(part_html.text_content().strip())
# 분야별 탑 주요 뉴스

# 최종 시간
for part_html in root.xpath('//span[@class="small"]/em'):
    print('' +part_html.text_content() + '\r\n')
#
# for part_html in root.cssselect('span'):
#     print('' +part_html.text_content() + '\r\n')


# //*[@id="text_today_main_news_801001"]/li[1]/div/a/strong
# # 인절미 //*[@id="pan_today_main_news"]/div[1]/div/a/div[2]
# # - > //div[@class ="nowsnow_imgarea"]/a/div/div
# # 김정은 현장연결 //*[@id="section_politics"]/div[2]/div/ul/li[1]/a/strong
# # - > //ul[@class="mlist2 no_bg"]/li/a/strong
# //*[@id="section_politics"]/div[2]/div/ul/li[1]/a/strong




# 가장 많이 본 뉴스

print('가장 많이 본 뉴스 :')
# for part_html in root.xpath('//ul[@class="section_list_ranking"]/li/a'):
#     print('' +part_html.text_content() + '\r\n')

for part_html in root.cssselect('ul.section_list_ranking li a'):
    print(part_html.text_content())



