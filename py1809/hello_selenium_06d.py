# # 공동 주택 단지
# # http://k-apt.go.kr
# # 2018.08.서울, 강남구, 삼성동소재 모든 아파트
# 선택 한목에 대한 코드값 추출
# 11, 680 , 105 , A1321~~

from selenium import webdriver
import re
import time

from selenium.webdriver.support.select import Select

url ='http://k-apt.go.kr/kaptinfo/openkaptinfo.do'
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)
# time.sleep(2)
# Chrome.maximize_window()

time.sleep(2)

# 2018.08.서울, 강남구, 삼성동 등을 차례로 선택
# Select 태그로 래핑하기 (Select 태그에서 값을 뽑아오거나 할때 , check 박스처럼 value값을 직접 받아올 수 없으니 , 변수화시키는
# 것임 변수화 시킨 year를 LINE48에서처럼 뽑아서 쓸 수 있도록 하는 것 ! )

year = Select(Chrome.find_element_by_class_name('combo_YYYY'))
year.select_by_visible_text('2018')
time.sleep(2)

month = Select(Chrome.find_element_by_class_name('combo_MM'))
month.select_by_visible_text('08')
time.sleep(2)

sido = Select(Chrome.find_element_by_class_name('combo_SIDO'))
sido.select_by_visible_text('서울특별시')
time.sleep(2)

sgg = Select(Chrome.find_element_by_class_name('combo_SGG'))
sgg.select_by_visible_text('강남구')
time.sleep(2)

emd = Select(Chrome.find_element_by_class_name('combo_EMD'))
emd.select_by_visible_text('삼성동')
time.sleep(2)


# 선택한 년, 월, 시, 구, 동에 대한 코드 출력

for option in year.options:
    if option.text == '2018':
        print(option.text,option.get_attribute('value'))

for option in month.options:
    if option.text == '08':
        print(option.text,option.get_attribute('value'))

for option in sido.options:
    if option.text == '서울특별시':
        print(option.text,option.get_attribute('value'))

for option in sgg.options:
    if option.text == '강남구':
        print(option.text,option.get_attribute('value'))

for option in emd.options:
    if option.text == '삼성동':
        print(option.text,option.get_attribute('value'))







