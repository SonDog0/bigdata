# 공동 주택 단지
# http://k-apt.go.kr
# 2018.08.서울, 강남구, 삼성동, 아이파크삼성동 아파트 주차대수 (지상,지하)

from pymongo import MongoClient
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.support.select import Select
import re
import time

def make_cool(str):
    str = re.sub(r'[\s]', '', str)
    str = re.sub(r'[,]','',str)
    str = re.sub(r'["]','',str)
    return str

keys = ['단지' , '지번', '전용면적', '실거래가', '계약일', '거래금액', '층']


#selenium 실행
url ='http://land.seoul.go.kr/'
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)
time.sleep(3)

# '부동산 실거래가' 버튼 클릭
# 메인페이지의 본문은 프레임안에 처리되고 있음
# 프레임 전환후 클릭 해야함
frm = Chrome.find_element_by_name('mainFrm')
Chrome.switch_to.frame(frm)
landrp = Chrome.find_element_by_css_selector('a[title="부동산실거래가"]')
# -- 프레임 전환 후 클릭
mouse = webdriver.ActionChains(Chrome)
mouse.move_to_element(landrp).click().perform()


time.sleep(3)

# -- 콤보박스 클릭을 위한 프레임 전환

frm = Chrome.find_element_by_id('contentFrame')
Chrome.switch_to.frame(frm)

frm = Chrome.find_element_by_id('contentInfoFrame')
Chrome.switch_to.frame(frm)

sido = Select(Chrome.find_element_by_id('selectSigungu'))
sido.select_by_visible_text('강남구')
time.sleep(2)

dong = Select(Chrome.find_element_by_id('selectBjdong'))
dong.select_by_visible_text('논현동')
time.sleep(2)

year = Select(Chrome.find_element_by_id('selectYear'))
year.select_by_visible_text('2018')
time.sleep(2)

bongi = Select(Chrome.find_element_by_id('selectBoongi'))
bongi.select_by_visible_text('1분기')
time.sleep(2)

findbtn = Chrome.find_element_by_css_selector('a[id="search"]')
mouse = webdriver.ActionChains(Chrome)
mouse.move_to_element(findbtn).click().perform()

time.sleep(2)

# '검색' 버튼 클릭 후 내용 확인
# print(Chrome.page_source)
# bs로 출력

html = BeautifulSoup(Chrome.page_source,'lxml')
# print(html.prettify())

# tech ! 빈 내용이 많은 테이블을 정제하기
# html = re.sub(r'<td .*?>', '"', html)
# html = re.sub(r'</td>', '",', html)
# html = re.sub(r'<.*?>','',html)
# html = re.sub(r'</.*?>','',html)
# print(html)

#
for tblist in html.select('#resultList tr'):
    tblist = re.sub(r'<td .*?>', '"', str(tblist))
    #expected string or bytes-like object 오류 방지를위해 tblist를 str형식으로 변경
    tblist = re.sub(r'</td>', '"|', tblist)
    tblist = re.sub(r'<.*?>', '', tblist)
    tblist = re.sub(r'</.*?>', '', tblist)
    # print(tblist)

    realprices = tblist.split('|')



    for i in range(0, int(len(realprices)/14)):
        apt = {}
        rps = []

        for j in range(0,3):
            apt[keys[j]] = make_cool((realprices[i * 14 + j  ]))


        # 실 거래가 #1 , #2 , #3
        for k in range(0,3):
            rp = {}
            for j in range(4,7):
                rp[keys[j]] = make_cool((realprices[i * 14 + j - 1 + k * 3 ]))
            rps.append(rp)

        # 모든 실거래가 추가
        apt[keys[3]] = rps
        print(apt)





Chrome.quit()
