import  sys
import re   # 정규표현식 처리용 패키지
# 내장 패키지

from urllib.request import urlopen
from html import unescape


# 웹 페이지 크롤링을 위해 필요한 패키지 초기화


# 온라인 도서 쇼핑몰의 도서 정보를 크롤링함
# http://www.hanbit.co.kr/store/store_submain.html
# 도서 정보가 있는 사이트의 URL을 알아냄

# 문서에서 필요한 정보를 얻어오려면 정보가 있는 위치 (태그,CSS등등)를 알아내야 함
# 일반적으로 html 소스에서 필요한 정보를 크롤링 함

## 크롤링을 위한 크롤러 ?

f = urlopen('http://www.hanbit.co.kr/store/store_submain.html')
# 크롤링할 url을 urlopen 함수의 매개변수로 입력
# f변수에는 open한 URL의 html 소스가 저장됨


encode = f.info().get_content_charset()
print(encode)
# http 헤더를 기반으로 크롤링한 문서의 인코딩 방식을 알아냄 / 내용 출력 (utf-8)

text = f.read().decode(encode)
print(text)
#알아낸 인코딩 방식을 이용해서 크롤링한 문서를 디코딩함
# 디코딩된 문서를 콘솔에 출력

# text = f.read()
# print(text)
# 인코딩 하지 않으면 .. 한글 깨짐

with open('data/store_main.html', 'w', encoding=encode) as out:
    out.write(text)
# 크롤링한 문서를 특정 위치에 파일로 저장함


