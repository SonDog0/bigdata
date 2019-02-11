# 공동주택관리정보시스템 k-apt.go.kr 에서 단지정보를 이용해서 단지별 주차장 수 추출(2018.08, 서울, 강남구, 아이파크삼성동)
# 크롬, 개발자도구, 네트워크 탭에서 요청 header 조사
# 서울 특별시 :  bjd_code : 11
# 강남구 : 680
# 삼성동 : 105
# 아이파크삼성동: KAPT_CODE = A13509009

# 시간, 지역에 따른 아파트 목록 조회
# http://k-apt.go.kr/kaptinfo/getKaptListl.do
# ?bjd_code=11680105&search_date=201808

# 지도에 아파트 좌표 표시
# http://k-apt.go.kr/kaptinfo/getKaptInfo_poi.do
# ?bjd_code=11680105&search_date=201808

# 선택한 아파트 상세 정보
# http://k-apt.go.kr/kaptinfo/getKaptInfo_detail.do
# ?kapt_code=A13509009

# http://k-apt.go.kr/kaptinfo/openkaptinfo.do
# ?bjd_code=11680105&search_date=201808
# ?kapt_code=A13509009
# http://k-apt.go.kr/kaptinfo/openkaptinfo.do?bjd_code=11680105&search_date=201808?kapt_code=A13509009



import requests
from bs4 import BeautifulSoup
import time


url = 'http://k-apt.go.kr/kaptinfo/openkaptinfo.do?bjd_code=11680105&search_date=201808?kapt_code=A13509009'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36','Referer' : 'http://k-apt.go.kr/kaptinfo/openkaptinfo.do?bjd_code=11680105&search_date=201808?kapt_code=A13509009'}

res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')  # 가볍고 처리가 빠름
print(html)

# 주차대수 항목을 검색해보면 값이 없음
# 동적으로 페이지를 생성하기 때문에
# bs4로는 데이터 추출이 어려움 - selenium 사용




