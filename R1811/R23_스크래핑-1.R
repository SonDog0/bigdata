

install.packages('rvest')

#httr 패키지
#http 헤더 취급 post,get api 지원
#read_html(url) 를 간단하게 GET/POST 함수로 처리가능
#부수적으로 http header 를 추가해서 서버에 요청 
#웹문서를 가져올때는 content 함수를 이용
install.packages('httr')
library(httr)

url <- 'http://www.hanbit.co.kr/store/books/full_book_list.html'
html <- GET(url,add_headers(
  .headers =c('User-Agent'='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')))
content(html)
content(html,'text')

title<-html_nodes(content(html),'td.left')
price<-html_nodes(content(html),'td.right')
html_text(title)
html_text(price)

install.packages('devtools')
devtools::install_github('ropensci/RSelenium')
library(RSelenium)
library(rvest)


chrome <- remoteDriver('localhost',9563,'chrome')
chrome$open()
