# http://movie.daum.net/main/new#slide-1-0
# daum.net 영화 사이트에서 영화순위, 제목, 개봉일 추출
# selenium과 bs4를 이용

from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time

name =[]
rank = []
orderperc = []

# geckodriver 브라우저 실행하기
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 지정한 URL로 접속하기
url ='http://movie.daum.net/main/new#slide-1-0'
Chrome.get(url)
# Chrome.refresh()
#
#
# #응답으로 받은 결과를 화면에 출력
# # print(firefox.page_source)
# res = Chrome.page_source

# # bs4를 이용해서 원하는 데이터 추출하기
# html = BeautifulSoup(res,'lxml')
#
# for title in html.select('span.cont_poster strong a'):
#     # print(title.text)
#     name.append(title.text)
#
#
#
# for title in html.select('div div span em'):
#     # print(title.text)
#     rank.append((title.text))
#
#
# for title in html.select('div div span.cont_state span'):
#
#     temp = re.sub(r'예매율','',title.text).strip()
#     orderperc.append(temp)
#     # print(temp)
#
# for i in range(0,len(name)):
#     print(name[i],rank[i],orderperc[i])


# 반복처리
# for i in range(0,4):
#     url = 'http://movie.daum.net/main/new#slide-1-'+str(i)
#     Chrome.get(url)
#     Chrome.refresh()
#
#     # 응답으로 받은 결과를 화면에 출력
#     # print(firefox.page_source)
#     res = Chrome.page_source
#
#     # bs4를 이용해서 원하는 데이터 추출하기
#     html = BeautifulSoup(res, 'lxml')
#
#     for title in html.select('span.cont_poster strong a'):
#         # print(title.text)
#         name.append(title.text)
#
#     for title in html.select('div div span em'):
#         # print(title.text)
#         rank.append((title.text))
#
#     for title in html.select('div div span.cont_state span'):
#         temp = re.sub(r'예매율', '', title.text).strip()
#         orderperc.append(temp)
#         # print(temp)
#
#     for j in range(0, len(name)):
#         print(name[j], rank[j], orderperc[j])
#     time.sleep(3)

# 슬라이드 다음 버튼 클릭 후 영화제목 (mainSlideNextBtn)
# 슬라이드 다음 버튼은 이미지에 a 태그형태로 작성됨
for i in range(1,4):

    time.sleep(3)
    slidebtn = Chrome.find_element_by_id('mainSlideNextBtn')
    mouse =webdriver.ActionChains(Chrome)
    mouse.move_to_element(slidebtn).click().perform()








# 작업 종료시 브라우저 닫음
Chrome.close()



# #slide-1 > div:nth-child(6) > div > span > span.cont_poster > strong > a
# slide-1 > div:nth-child(6) > div > span > em
#slide-1 > div:nth-child(6) > div > span > span.cont_state > span