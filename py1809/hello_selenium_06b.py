# 공동 주택 단지
# http://k-apt.go.kr
# 2018.08.서울, 강남구, 삼성동소재 모든 아파트
# 이름 / 주소 / 주차대수 출력


from selenium import webdriver
import re
import time


url ='http://k-apt.go.kr/kaptinfo/openkaptinfo.do'
Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
Chrome.get(url)
time.sleep(2)
Chrome.maximize_window()
time.sleep(2)
end = Chrome.find_elements_by_id('')
for i in range(1,16):
    time.sleep(2)
    Chrome.find_element_by_xpath('//*[@class="combo_YYYY"]/option[text()="2018"]').click()
    Chrome.find_element_by_xpath('//*[@class="combo_MM"]/option[text()="08"]').click()
    Chrome.find_element_by_xpath('//select[@class="combo_SIDO"]/option[text()="서울특별시"]').click()
    time.sleep(2)

    Chrome.find_element_by_xpath('//select[@class="combo_SGG"]/option[text()="강남구"]').click()
    time.sleep(2)

    Chrome.find_element_by_xpath('//select[@class="combo_EMD"]/option[text()="삼성동"]').click()
    time.sleep(2)

    Chrome.find_element_by_xpath('//tr[@id="'+str(i)+'"]').click()
    time.sleep(2)

    Chrome.find_element_by_xpath('//img[@alt="기본정보"]').click()
    # Chrome.find_element_by_id('ui-id-3').click()


    print(Chrome.find_element_by_id('kapt_name').text)
    time.sleep(2)
    print(Chrome.find_element_by_id('kab_addr').text)
    time.sleep(2)

    Chrome.find_element_by_xpath('//img[@alt="관리시설정보"]').click()
    # Chrome.find_element_by_id('ui-id-4').click()
    time.sleep(4)

    # 차 대수 뽑기
    print(Chrome.find_element_by_id('parking_cnt').text)

    time.sleep(2)
    Chrome.find_element_by_id('ui-id-1').click()


Chrome.quit()













