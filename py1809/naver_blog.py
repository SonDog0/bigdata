# BBQ 페이지다운 크롤링 ( selenium )

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import json
import re
import time

save = []
url = 'https://search.shopping.naver.com/search/all.nhn?query=%EC%97%AC%EC%84%B1%EC%9D%98%EB%A5%98&cat_id=&frm=NVSHATC'

Chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')


Chrome.get(url)
body = Chrome.find_element_by_tag_name("body")
html = BeautifulSoup(Chrome.page_source,'lxml')
Chrome.maximize_window()

# 댓글
for a in html.select("sp_blog_1 > dl > dt > a"):
    save.append(a.text)

# #_search_list > div.search_list.basis > ul > li:nth-child(1) > div.info > span.depth > a.cat_id_50000815
# #_search_list > div.search_list.basis > ul > li:nth-child(2) > div.info > span.depth > a.cat_id_50000808
print(len(save))



# save.append(Chrome.find_element_by_css_selector("sp_blog_1 > dl > dt > a").text)

# save.append(Chrome.find_element_by_css_selector("sp_blog_"+ str(k) +" > dl > dt > a").text)


# #sp_blog_1 > dl > dt > a
# #sp_blog_2 > dl > dt > a
# f = open('./BBQ.txt','a' , encoding='UTF-8')
# for i in range(0,len(save)):
#     f.write(save[i])
#     f.write('\n')
#


