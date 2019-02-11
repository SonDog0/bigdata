# 텍스트 마이닝
# 트위터에서 데이터 수집하기
# pip install twitterscraper  # file setting에서 직접 설치
# twitterscraper.nl

from twitterscraper import query_tweets
import datetime as dt
from time import sleep

"""
if __name__=='__main__':
   for tweet in query_tweets('블랙프라이데이',10):
       print(tweet.timestamp)    # 작성시간
       print(tweet.text)         # 트윗내용
#               => 10개의 카테고리? 에서 디폴트값인 20개씩 긁어옴
"""

"""
# twitterscraper 테스트 : 수집일자 파일저장, 수입일자 설정
if __name__=='__main__':
    # 수집한 트윗을 저장할 파일이름/경로 지정
    fname = r'c:/Java/data/bf' + str(dt.date.today()) + '.txt'

    file = open(fname, 'ab') # 지정한 파일 객체 생성 ab를 안쓸경우 누적이 되지 않음
    for tweet in query_tweets('블랙프라이데이',
                              begindate=dt.date(2018,11,1),
                              enddate=dt.date(2018,11,28),
                              limit=10):
        file.write(str(tweet.timestamp).encode())
        file.write(tweet.text.encode('utf-8'))

    file.close()
"""

# twitterscraper 최종 : 수집일자 파일저장, 수입일자, 수집건수, 수집 지연

if __name__=='__main__':
    # 수집한 트윗을 저장할 파일이름/경로 지정
    total = 0      # 수집한 트윗 건수
    fname = r'c:/Java/data/bf' + str(dt.date.today()) + '.txt'

    while True :
        size = 0   # 수집한 트윗 개별 건수
        file = open(fname, 'ab') # 지정한 파일 객체 생성 ab를 안쓸경우 누적이 되지 않음
        for tweet in query_tweets('블랙프라이데이',
                                  begindate=dt.date(2018,11,1),
                                  enddate=dt.date(2018,11,28),
                                  limit=10):
            file.write(str(tweet.timestamp).encode())
            file.write(tweet.text.encode('utf-8'))
            size += 1  # 수집한 트윗을 파일에 저장 할 때마다 카운트를 하나씩 증가 시킴

        file.close()
        total += size
        print('수집한 트윗 총 갯수', total)

        sleep(5)
