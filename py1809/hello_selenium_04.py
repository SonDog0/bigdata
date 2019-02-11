from selenium import webdriver
import re
import time

Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
url ='https://www.daum.net/'
Chrome.get(url)

# 먼저, 다음 메인페이지에서
# 아이디id, 비밀번호inputPwd 입력후 '로그인'버튼 클릭

time.sleep(2)

# 겉으로 보기에 하나의 웹 페이지로 보이지만
# 실제로는 여러페이지가 합쳐져서 보여지는 구조
# iframe 태그로 다른 웹 페이즈를 호출하여
# 현재 문서에 포함시켜 출력함
# 로그인 박스, 쇼핑박스, 인기기획전 등이 iframe으로 호출

# iframe을 통해 호출되는 페이지로 제어를 옮겨야 함
iframe = Chrome.find_element_by_css_selector('iframe[id="loginForm"]')
Chrome.switch_to.frame(iframe)
time.sleep(2)



userid = Chrome.find_element_by_id('id')
userid.send_keys('gnslekek')
time.sleep(2)

passwd = Chrome.find_element_by_id('inputPwd')
passwd.send_keys('비번')
time.sleep(2)

loginbtn = Chrome.find_element_by_id('loginSubmit')
loginbtn.submit()


time.sleep(3)
# 로그인 후 메일 수 확인
mailnum = Chrome.find_element_by_css_selector('a.link_num')
print(mailnum.text)
time.sleep((3))

# 로그아웃 처리
logoutbtn = Chrome.find_element_by_css_selector('button.btn_logout')
logoutbtn.submit()
time.sleep(3)

Chrome.quit()

