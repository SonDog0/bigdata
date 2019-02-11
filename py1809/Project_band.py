# 네이버 로그인 자동화 (lg_local_btn)

# 네이버 메인 페이지에서 naver 로그인 버튼 클릭
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import time

save = []
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
# url ='https://www.naver.com/'
# Chrome.get(url)
# time.sleep(5)
#
#
# logbtn = Chrome.find_element_by_class_name('lg_local_btn')
# mouse = webdriver.ActionChains(Chrome)
# mouse.move_to_element(logbtn).click().perform()
# # time.sleep(5)
# # sleep은 단순히 정지 상태로 대기
#
# time.sleep(5)
#
# # 암묵적 시간 만큼 대기
# # 특정요소가 실행될때까지 기다리는 효과
#
# # 로그인 페이지로 전환되면
# # 아이디 , 비밀번호 입력후 '로그인' 버튼 클릭
#
# Chrome.find_element_by_id('id').send_keys('sjh10271')
# time.sleep(5)
# Chrome.find_element_by_id('pw').send_keys('10276320s')
# # 버튼의 유형이 input일 경우 submit() 메소드 사용
# loginbtn = Chrome.find_element_by_css_selector('input[title="로그인"]')
# loginbtn.submit()
# # Chrome.implicitly_wait(3)
time.sleep(150)

# Chrome.get('https://band.us/discover/search/%EB%A1%AF%EB%8D%B0%ED%99%88%EC%87%BC%ED%95%91')
Chrome.get('https://band.us/discover/post/%EB%A1%AF%EB%8D%B0%ED%99%88%EC%87%BC%ED%95%91')
time.sleep(10)

html = Chrome.page_source
soup = BeautifulSoup(html, 'html.parser')
# for a in soup.select('div div h1'):
#     print(a.text)
for a in soup.select('div.pTxt'):
    print(a.text)

# num_of_page = 50
body = Chrome.find_element_by_tag_name("body")

for i in range(0, 20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

print('-------------------------------------------------------------')
# 배열저장

for i in range(1,10):
    for a in soup.select("li:nth-of-type(" + str(i) + ")a.body._goPost div.pTxt"):
       save.append(a.text)



# 파일저장

f = open('./BAND.txt', 'a', encoding='UTF-8')
for i in range(0, len(save)):
    f.write(save[i])
    f.write('\n')
# for a in soup.select('a.body._goPost div.pTxt'):
#     print(a.text)

# content > div > div > section > ul > li:nth-child(1) > a.body._goPost
# content > div > div > section > ul > li:nth-child(1) > a.body._goPost > div.pTxt


# content > div > div.wide.-w840 > section > div > div > h1

#
# res = requests.get(url,headers=headers)
# # html = BeautifulSoup(res.text,'html.parser')
# html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름
#
# #도서 제목 가져오기
# for a in html.select('p.book_tit a'):
#     print(a.text,a.get('href'))
#
#
# for n in notices:
#     print(n.text.strip())
#
#

# content > div > div > section > ul > li:nth-child(1) > a.body._goPost > div.pTxt

# content > div > div > section > ul > li:nth-child(2) > a.body._goPost > div.pTxt
