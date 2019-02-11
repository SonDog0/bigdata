# 네이버 로그인 자동화 (lg_local_btn)

# 네이버 메인 페이지에서 naver 로그인 버튼 클릭
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time

Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
url ='https://www.naver.com/'
Chrome.get(url)
time.sleep(5)
logbtn = Chrome.find_element_by_class_name('lg_local_btn')
mouse = webdriver.ActionChains(Chrome)
mouse.move_to_element(logbtn).click().perform()
# time.sleep(5)
# sleep은 단순히 정지 상태로 대기

time.sleep(5)

# 암묵적 시간 만큼 대기
# 특정요소가 실행될때까지 기다리는 효과

# 로그인 페이지로 전환되면
# 아이디 , 비밀번호 입력후 '로그인' 버튼 클릭

Chrome.find_element_by_id('id').send_keys('madok1')
time.sleep(5)
Chrome.find_element_by_id('pw').send_keys('비번')
# 버튼의 유형이 input일 경우 submit() 메소드 사용
loginbtn = Chrome.find_element_by_css_selector('input[title="로그인"]')
loginbtn.submit()
# Chrome.implicitly_wait(3)
time.sleep(5)

Chrome.close()