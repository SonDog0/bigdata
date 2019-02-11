import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

temp = []

for i in range (1,65):
    url = 'http://www.ppomppu.co.kr/search_bbs.php?search_type=sub_memo&page_no='+str(i)+'&keyword=%B7%D4%B5%A5%C8%A8%BC%EE%C7%CE&page_size=20&bbs_id=&order_type=date&bbs_cate=1'
    # 롯데홈쇼핑 키워드 검색

    # url = 'http://www.ppomppu.co.kr/search_bbs.php?search_type=sub_memo&page_no='+str(i)+'&keyword=Lpoint&page_size=20&bbs_id=&order_type=date&bbs_cate=1'
    # # Lpoint 키워드 검색


    res = requests.get(url, headers=headers)
    html = BeautifulSoup(res.text, 'lxml')

    # 게시글 제목 추출 및 저장
    for a in html.select('form div div span a'):
        temp.append(a.text)

# 확인코드
for i in range(0,len(temp)):
    print(temp[i])


# 파일저장

f = open('./lotteHS2_ppomppu.txt','a' , encoding='UTF-8')
for i in range(0,len(temp)):
    f.write(temp[i])
    f.write('\n')

#
# f = open('./lpoint_ppomppu.txt','a' , encoding='UTF-8')
# for i in range(0,len(temp)):
#     f.write(temp[i])
#     f.write('\n')


