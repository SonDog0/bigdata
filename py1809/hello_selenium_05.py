from selenium import webdriver
import re
import time
from selenium.webdriver.common.alert import Alert


Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')


url ='http://www.letskorail.com'


Chrome.get(url)
time.sleep(2)

# 코레일 메인페이지에서 로그인버튼 클릭
loginbtn =Chrome.find_element_by_css_selector('a[onclick="return m_login_link()"]')
mouse = webdriver.ActionChains(Chrome)
mouse.move_to_element(loginbtn).click().perform()

#content > div.restaurant-detail.row.ng-scope > div.col-sm-8 > ul > li:nth-child(2) > a
#header > div.h_cont > div > ul > li:nth-child(2) > a > img

# 로그엔 페이징에서
# 아이디 txtMember 비밀번호 txtPwd 입력후
userid = Chrome.find_element_by_id('txtMember')
userid.send_keys('1874865137')
time.sleep(3)
passwd = Chrome.find_element_by_id('txtPwd')
passwd.send_keys('비번')
time.sleep(3)

# 로그인 버튼은 a태그로 구성되어있지만 id 속성이없음
# a태그 아래에 있는 img 태그의 alt 속성으로 대신함
loginb =Chrome.find_element_by_css_selector('img[alt="확인"]')
mouse =webdriver.ActionChains(Chrome)
mouse.move_to_element(loginb).click().perform()

time.sleep(3)

# 로그아웃 버튼 클릭 시 자바스크립트로 구현된 경고창이 표시 이러한 경고창을 자동으로 닫으려면 accept() 사용
# from selenium.webdriver.common.alert import Alert


logout =Chrome.find_element_by_css_selector('img[alt="로그아웃"]')
mouse =webdriver.ActionChains(Chrome)
mouse.move_to_element(logout).click().perform()

Alert(Chrome).accept()

time.sleep(3)
Chrome.close()


