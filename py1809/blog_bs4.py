# 네이버 블로그
# 페이지 이동 파라미터로
import requests
from bs4 import BeautifulSoup
blog_title = []




url ='https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=Lpoint&sm=tab_pge&srchby=all&st=sim&where=post'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
for i in range(1,500,10):
    params = {'start': i}
    res = requests.get(url,headers=headers,params=params)
    # html = BeautifulSoup(res.text,'html.parser')
    html = BeautifulSoup(res.text,'lxml') # 가볍고 처리가 빠름

    for a in html.select('li.sh_blog_top'):
        blog_title.append(a.text)




    for i in range(len(blog_title)):
        print(blog_title[i])

f = open('./lpoint_blog.txt', 'a', encoding='UTF-8')
for i in range(0, len(blog_title)):
    f.write(blog_title[i])
    f.write('\n')
