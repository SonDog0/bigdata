# https://movie.daum.net/main/new#slide-1-0 홈
# https://movie.daum.net/premovie/released 현재상영/ 개봉예정
# http://ticket2.movie.daum.net/Movie/MovieRankList.aspx 예매순위
# 영화제목, 순위, 개봉일

import requests
import lxml.html

url = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
res = requests.get(url)
html = res.text
root = lxml.html.fromstring(html)

# 영화제목
# 소스상에서는 영화 제목이 변수로 되어있음
# 브라우저에 의해 동적처리된 후에야 제목을 볼 수 있음

# for part_html in root.xpath('//span[@class="inf_poster"]/cont_poster/strong/a'):
#     print('' +part_html.text_content() + '\r\n')

for part_html in root.cssselect('strong.tit_join a'):
    print('' +part_html.text_content().strip() + '\r\n')

for part_html in root.cssselect('span.num_rank'):
    print('' + part_html.text_content().strip() + '\r\n')


for part_html in root.cssselect('dl.list_state dd:nth-child(2)'):
    print('' + part_html.text_content().strip() + '\r\n')




# #mArticle > div > div.movie_detail > div.main_detail > div > ul > li:nth-child(1) > div > strong > a
# #mArticle > div > div.movie_detail > div.main_detail > div > ul > li:nth-child(1) > a > span.num_rank.rank_1
#  #mArticle > div > div.movie_detail > div.main_detail > div > ul > li:nth-child(1) > div > dl > dd:nth-child(2)