# 텍스트 마이닝
# 트위터에서 데이터 수집하기
# pip install twitterscraper
# twitterscraper.nl

from twitterscraper import query_tweets
import datetime as dt
from time import sleep


# twitterscaper 간단 테스트
# if __name__ == '__main__':
#     for tweet in query_tweets('블랙프라이데이',10):
#         print(tweet.timestamp)
#         print(tweet.text)

# twitterscaper 간단 테스트 : 수집결과 파일 저장 , 수집일자 설정

# if __name__ == '__main__':
#
#     fname = r'c:/Java/data/bf' + str(dt.date.today()) + '.txt'
#
#     file = open(fname , 'ab')
#     for tweet in query_tweets('블랙프라이데이' , begindate=dt.date(2018,11,1) , enddate=dt.date(2018,11,28),limit=10):
#
#         file.write(str(tweet.timestamp).encode())
#
#         file.write(tweet.text.encode('utf-8'))
#
#
#
#
#     file.close()



if __name__ == '__main__':
    total = 0 # 수집한 트위터 건수
    fname = r'c:/Java/data/bf' + str(dt.date.today()) + '.txt'

    while True:
        size = 0 # 수집한 트윗 개별 건수
        file = open(fname , 'ab')
        for tweet in query_tweets('블랙프라이데이' , begindate=dt.date(2018,11,1) , enddate=dt.date(2018,11,28),limit=10):
            file.write(str(tweet.timestamp).encode())
            file.write(tweet.text.encode('utf-8'))
            size = size + 1
            # 수집한 트윗을 파일에 저장할때 마다
            # 카운트를 하나씩 증가
        file.close()
        total += size
        print('수집한 트윗 총 갯수', total)

        sleep(5)


