# 공동 주택 단지
# http://k-apt.go.kr
# 2018.08.서울, 강남구, 삼성동, 아이파크삼성동 아파트 주차대수 (지상,지하)



from selenium import webdriver
import re
import time


url ='http://k-apt.go.kr'
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)
time.sleep(3)

# 팝업창 자동으로 닫으려고 시도
# 하지만, 두번째 팝업창이 세번째 팝업창에 가려져서
# 닫기버튼(x)이 보이지 않아 예외발생
# 예외처리후 다시 팝업창 닫음
# for i in range(0,2):
#     for popups in Chrome.find_elements_by_css_selector('div.layerPopupTitle div a'):
#         try:
#             popups.click()
#             time.sleep(2)
#         except:
#             pass

# 팝업창의 닫기버튼에 적용된 자바스크립트 함수를 직접호출해서 닫기

# Chrome.execute_script('closeLyserPopup("popup_20170303")')
# Chrome.execute_script('closeLyserPopup("popup_20171208")')
# Chrome.execute_script('closeLyserPopup("popup_20180912")')
#
# for popups in Chrome.find_elements_by_css_selector('div.layerPopup'):
#     print(popups.get_attribute('id'))


# 팝업창의 닫기버튼에 적용된 자바스크립트 함수를 직접호출해서 닫기 (for문으로 모델링)

for popups in Chrome.find_elements_by_css_selector('div.layerPopup'):
    id = popups.get_attribute('id')
    Chrome.execute_script('closeLyserPopup("'+id+'")')
    time.sleep(1)




Chrome.find_element_by_css_selector('span.navi2').click()
#topMenu2 > a
# Chrome.find_element_by_id('ui-id-8').click()
time.sleep(3)

#xpath로 작성
Chrome.find_element_by_xpath('//*[@class="combo_YYYY"]/option[text()="2018"]').click()
Chrome.find_element_by_xpath('//*[@class="combo_MM"]/option[text()="08"]').click()
Chrome.find_element_by_xpath('//select[@class="combo_SIDO"]/option[text()="서울특별시"]').click()
Chrome.implicitly_wait(3)
Chrome.find_element_by_xpath('//select[@class="combo_SGG"]/option[text()="강남구"]').click()
Chrome.implicitly_wait(3)
Chrome.find_element_by_xpath('//select[@class="combo_EMD"]/option[text()="삼성동"]').click()
Chrome.implicitly_wait(3)
Chrome.find_element_by_xpath('//td[@title="아이파크삼성동"]').click()
time.sleep(5)
select = Chrome.find_element_by_xpath('//img[@alt="관리시설정보"]').click()
# Chrome.find_element_by_id('ui-id-4').click()
time.sleep(2)


# 차 대수 뽑기
print(Chrome.find_element_by_id('parking_cnt').text)


time.sleep(5)


Chrome.quit()
