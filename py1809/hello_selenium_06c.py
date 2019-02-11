# 공동 주택 단지
# http://k-apt.go.kr
# 2018.08.서울, 강남구, 삼성동소재 모든 아파트
# 이름 / 주소 / 주차대수 출력
# 아파트 명칭에 대한 id값은 자동추출



from selenium import webdriver
import re
import time


url ='http://k-apt.go.kr/kaptinfo/openkaptinfo.do'
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)
# time.sleep(2)
# Chrome.maximize_window()

time.sleep(2)
Chrome.find_element_by_xpath('//*[@class="combo_YYYY"]/option[text()="2018"]').click()
Chrome.find_element_by_xpath('//*[@class="combo_MM"]/option[text()="08"]').click()
Chrome.find_element_by_xpath('//select[@class="combo_SIDO"]/option[text()="서울특별시"]').click()
time.sleep(2)

Chrome.find_element_by_xpath('//select[@class="combo_SGG"]/option[text()="강남구"]').click()
time.sleep(2)

Chrome.find_element_by_xpath('//select[@class="combo_EMD"]/option[text()="삼성동"]').click()
time.sleep(2)

# 아파트 목록에서 마지막 id값을 추출

# tr요소중 마지막 요소 하나를 추출해서 id값 저장
apt_id = Chrome.find_elements_by_xpath('//table[@id="aptInfoList"]/tbody/tr')[-1].get_attribute('id')

# apt_id = Chrome.find_elements_by_css_selector('table[id="aptInfoList"] tbody tr')[-1].get_attribute('id')
print(apt_id)


#
# # 첫번재 td 태그는 아파트 코드
# for trs in Chrome.find_elements_by_xpath('//table[@id="aptInfoList"]/tbody/tr/td'):
#
#     #2개의 td태그 중 숨김으로 처리되었던 td를 보임으로 설정
#     Chrome.execute_script("arguments[0].style.display ='block';",trs)
#
#     # 2개의 td 태그중 0번째 요소의 부모태그를 리턴함
#     parent =Chrome.execute_script("return arguments[0].parentNode;",trs)
#
#     print(parent.get_attribute('id'),trs.text)




