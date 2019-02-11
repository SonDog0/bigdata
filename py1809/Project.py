# BBQ 페이지다운 크롤링 ( selenium )

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import json
import re
import time

save = []
url = 'http://www.lotteimall.com/display/sellRank100.lotte?tlog=a1001_5#'

Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

cnt = 10
Chrome.get(url)
Chrome.maximize_window()
time.sleep(1)






loginbtn = Chrome.find_element_by_xpath('//*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/a')
mouse = webdriver.ActionChains(Chrome)
mouse.move_to_element(loginbtn).click().perform()
# //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[1]/li[4]/a 패션의류
# //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/a 식품

time.sleep(1)
loginbtn = Chrome.find_element_by_xpath('//*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/ul/li[3]/a')
mouse = webdriver.ActionChains(Chrome)
mouse.move_to_element(loginbtn).click().perform()
# //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[1]/li[4]/ul/li[3]/a 여성트랜드의류
# //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/ul/li[3]/a 즉석/가공식품

# 상품 클릭
# //*[@id="rn2th_container"]/div/div[2]/div[3]/ul/li[1]/div[2]/a/img
time.sleep(3)
for j in range(1,101):
    loginbtn =Chrome.find_element_by_xpath('//*[@id="rn2th_container"]/div/div[2]/div[3]/ul/li['+str(j)+']/div[2]/a/img')
    mouse = webdriver.ActionChains(Chrome)
    mouse.move_to_element(loginbtn).click().perform()

    time.sleep(2)

    # Q&A
    # //*[@id="contents"]/div[2]/div[2]/div[1]/ul/li[4]/a
    loginbtn =Chrome.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/div[1]/ul/li[4]/a')
    mouse = webdriver.ActionChains(Chrome)
    mouse.move_to_element(loginbtn).click().perform()


    # 댓글

    try:
        for k in range(1,11):
            save.append(Chrome.find_element_by_css_selector("li:nth-child("+ str(k)+ ") > div > div > p > span").text)
            print(k,save[k-1])
    except:
        pass

    # //*[@id="rn_header"]/div/div[2]/ul[1]/li[5]/a 베스트
    loginbtn = Chrome.find_element_by_xpath('//*[@id="rn_header"]/div/div[2]/ul[1]/li[5]/a')
    mouse = webdriver.ActionChains(Chrome)
    mouse.move_to_element(loginbtn).click().perform()

    loginbtn = Chrome.find_element_by_xpath('//*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/a')
    mouse = webdriver.ActionChains(Chrome)
    mouse.move_to_element(loginbtn).click().perform()
    # //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[1]/li[4]/a 패션의류
    # //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/a 식품

    time.sleep(1)
    loginbtn = Chrome.find_element_by_xpath('//*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/ul/li[3]/a')
    mouse = webdriver.ActionChains(Chrome)
    mouse.move_to_element(loginbtn).click().perform()
    # //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[1]/li[4]/ul/li[3]/a 여성트랜드의류
    # //*[@id="rn2th_container"]/div/div[2]/div[2]/ul[2]/li[4]/ul/li[3]/a 즉석/가공식품

for i in range(0,len(save)):
    print(save[i])

f = open('./Food.txt','a' , encoding='UTF-8')
for i in range(0,len(save)):
    f.write(save[i])
    f.write('\n')



