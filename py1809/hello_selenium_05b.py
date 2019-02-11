from selenium import webdriver
import re
import time
from selenium.webdriver.common.alert import Alert

url ='http://www.letskorail.com'
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)
# 출발역, 도착역, 시간, 인원 지정후 승처권 예매 버튼 클릭
#
Chrome.find_element_by_id('txtGoStart').clear()
Chrome.find_element_by_id('txtGoStart').send_keys('목포')
Chrome.find_element_by_id('txtGoEnd').clear()
Chrome.find_element_by_id('txtGoEnd').send_keys('서울')
Chrome.find_element_by_xpath('//*[@id="time"]/option[text()="20 (오후08)"]').click()
Chrome.find_element_by_xpath('//*[@id="people_num"]/option[text()="어른 4명"]').click()

reservbtn = Chrome.find_element_by_css_selector('img[alt="승차권예매"]').click()

# 열차 유형을 KTX/KTX-산천/SRT로 변경후 조회하기

choice = Chrome.find_element_by_xpath('//input[@title="KTX"]').click()

select = Chrome.find_element_by_xpath('//img[@alt="조회하기"]').click()
time.sleep(3)


# 브라우저 크기 변경 : maximize_windows()
Chrome.maximize_window()


# 자동 스크롤 - 자바스크립트 BOM 객체 사용 :execute_script
# 조회결과 화면이 잘 보이도록 브라우저 화면을 스크롤함
Chrome.execute_script('window.scrollTo(0,550)')

# 브라우저를 스크롤하는 자바스크립트 BOM 객체 사용



time.sleep(5)
Chrome.quit()
