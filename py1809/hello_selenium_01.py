# selenium 으로 스크래핑 하기
# requests, bs4로 스크래핑할 수 없는 동적 데이터를 원격조작이 가능한 브라우저를 이용해서 처리

# selenium : 브러우저를 이용한 작업들을 자동화할 수 있도록
# 특수하게 제작된 브라우저
# seleniumhq.org - download - third party driver
# Mozilla geckoDriver (geckodriver-v0.22.0-win64.zip)
#  또는 Google Chrome Driver (chromedriver_win32.zip) 다운로드

# 다운로드 받은 파일을 압축 해제한 후
# 'geckodriver.exe'를 C:\program Files\Mozilla Firefox에 복사
# 'chromedriver.exe'를 C:\program Files(x86)\Application 에 복사

from bs4 import BeautifulSoup
from selenium import webdriver


# geckodriver 브라우저 실행하기
firefox = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

# 지정한 URL로 접속하기
url = 'http://www.hanbit.co.kr/store/store_submain.html'
firefox.get(url)

#응답으로 받은 결과를 화면에 출력
# print(firefox.page_source)
res = firefox.page_source

# bs4를 이용해서 원하는 데이터 추출하기
html = BeautifulSoup(res,'lxml')

for title in html.select('p.book_tit a'):
    print(title.text)

# 작업 종료시 브라우저 닫음
firefox.close()
#
#
# # chromedriver 브라우저 실행하기
# Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#
# # 지정한 URL로 접속하기
# url = 'http://www.hanbit.co.kr/store/store_submain.html'
# Chrome.get(url)
#
# #응답으로 받은 결과를 화면에 출력
# print(Chrome.page_source)
#
# # 작업 종료시 브라우저 닫음
# Chrome.close()
#
#
