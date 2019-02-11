# 인스타그램 에서 해시태그 수집

# http://www.instagram.com/randyolson
# SPA - singgle page application 단일페이지로 웹 어플리케이션 생성
# SPA 특성상 서버로부터 데이터를 일겅와서
# script 태그를 이용해서 _shareData 변수를 만들고
# 이 변수에 데이터를 저장해 둠
# 이미지 클릭시 자바스크립트를 이용해서 UI를 생성후 출력



import pprint

from selenium import webdriver
from bs4 import BeautifulSoup
import json
import re
import time


url = 'http://www.instagram.com/randyolson'

Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)

html = BeautifulSoup(Chrome.page_source,'lxml')
Chrome.maximize_window()
# 스크래핑한 내용중 해쉬태그가 있는 본문 추출
body = html.find('body')
script = body.find('script')

# 메소드 체인 방식 사용
raw_json = script.text.strip().replace('window.sharedData =','').replace(';','')

# 정규 표현식 사용
tags = re.findall(r'#\w+',raw_json)
for i in range(0,len(tags)):
    print(tags[i])

print('\r\n')
# 두번째 페이지 부터는 스크롤해서 데이터를 가져와야함
# 하지만, 데이터는 JSON 형태로 전달되지 않고
# img 태그의 alt 속성에 저장됨

opage = 0 # 스크롤 이동 초기값
while True:
    Chrome.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

    #스크롤후 바뀐 소스내용 불러오기
    html = BeautifulSoup(Chrome.page_source,'lxml')
    time.sleep(2)

    #img 태그에 있는 alt 요소의 텍스트 가져오기
    for img in html.select('img[alt]'):
    #img 변수에 select(요소)한걸 집어넣음
        tags=re.findall(r'#\w+',img.get('alt'))

    for i in range(0,len(tags)):
        print(tags[i])


    cpage =Chrome.execute_script('return window.pageYOffset')
        # 스크롤 이동거리를 알아내서 cpage 변수에 저장

    print(opage, cpage)


    if (opage == cpage):
        print('스크롤불가')
        break
    elif (opage < cpage):
        opage = cpage
        pass





    # 스크롤 가능 여부 체크
    # 스크롤이 더이상 가능하지 않으면 반복문 중지
    # 자바스크립트 BOM중에서 window 객체에는
    # 스크롤이동거리에 관련된 정보를 제공하는 속성 존재
    # window.pageYOffset






Chrome.quit()