# 인스타그램 에서 해시태그 수집

# http://www.instagram.com/randyolson
# SPA - singgle page application 단일페이지로 웹 어플리케이션 생성
# SPA 특성상 서버로부터 데이터를 일겅와서
# script 태그를 이용해서 _shareData 변수를 만들고
# 이 변수에 데이터를 저장해 둠
# 이미지 클릭시 자바스크립트를 이용해서 UI를 생성후 출력

# request + beatifulsoup
import pprint

from bs4 import BeautifulSoup
import requests

import json
import re

url = 'http://www.instagram.com/randyolson'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers= ua)
html =BeautifulSoup(res.text,'lxml')

# 본문에서 script 태그에 정의된 _sharedData 변수를 찾아냄
body = html.find('body')
print(body)
print('\r\n')
script = body.find('script')
print(script)
print('\r\n')


# script 태그내 문자열만 추출함
raw_json_data = script.text.strip() # 문자열추출, 공백제거
raw_json_data = raw_json_data.replace('window._sharedData = ','').replace(';','')
print(raw_json_data)
print('\r\n')
print('----------------------------------------------------------------------------')

# 전처리된 json 데이터 확인 - 예쁘게 출력
# pprint.pprint(raw_json_data, indent=2)
# print('\r\n')


# json 형식으로 데이터를 메모리에 불러온 후
# 필요한 데이터 추출

#화면에 출력된 게시물 관련 데이터는 총 12개
json_data = json.loads(raw_json_data)

# for i in range(0,12):
#     post_list = json_data['entry_data']['ProfilePage'][0]
#     post_list = post_list['graphql']['user']
#     post_list = post_list['edge_owner_to_timeline_media']
#     post_list = post_list['edges'][i]['node']
#     post_list = post_list['edge_media_to_caption']['edges']
#     tag_list = post_list[0]['node']['text']
#
# # pprint.pprint(tag_list, indent=1)
#
# # 게시물 본문을 #으로 구분지어서 분리한 뒤 리스트에 저장
# tags = tag_list.split('#')
#
# for j in range(1,len(tags)):
#     print(tags[j])

# 정규 표현식으로 해쉬 태그 찾기
# #으로 시작하는 단어를 모두 찾아서 리스트에 저장
tags = re.findall(r'#\w+',raw_json_data)
print(len(tags))

# 리스트에 저장된 해쉬태그를 반복문으로 출력
for i in range(0,len(tags)):
    print(tags[i])



# requests는 브라우저 스크롤 기능이 없음
# 인스타그램 첫페이지에 대해 해쉬태그 추출하고
# 두번째 페이지 부터는 수집불가 - selenium 이용




