# 텍스트 마이닝 -형태소 분석
# 파이썬 형태소 사전 : KoNLPY 및 필요 모둘 설치
# konlpy.org
# pip install konlpy
# visualstudio.microsoft.com/downloads

# JPype1-0.6.3-cp36-cp36m-win_amd64.whl
# pycharm의 터미널창을 띄우고 다음 명령 실행
# python -m pip install c:/java/JPype1-0.6.3-cp36-cp36m-win_amd64.whl

# pip install konlpy


# pip install Twitter
# pip install KKma
# pip install Hannanum


from konlpy.tag import Twitter
from konlpy.tag import Okt
twitter = Okt()
# 트위터 형태소 사전
#
# txt1 = '아버지가 방에 들어가신다'
# txt2 = '나는 보리밥을 먹었다;'
# txt3 = '롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.'
#
# # print(twitter.nouns(txt1))
# #
# # print(twitter.pos(txt1)) # 중요 품사 기반 추출2
# # print(twitter.morphs(txt1)) # 상세 품사기반 추출
# #
#
# # 연설문 wordcount
#
# f = open('c:/Java/data/toji_2.txt','r',encoding='UTF-8')
#
# docs = f.read()
# # print(docs)
# from collections import Counter
# nouns = twitter.nouns(docs)
# print(nouns)
# wc = Counter(nouns)
# print(wc)
# # 빈도수 최상위 20개 출력
# wclist = wc.most_common(20)
# print(wclist)
# print(wclist[0][0],wclist[0][1])
#
# # 단어수가 2자 이상만 추출
# df_word=[]
# df_freq=[]
#
# for i in range(0,len(wclist)):
#     if len(wclist[i][0]) >= 2 :
#         df_word.append(wclist[i][0])
#         df_freq.append(wclist[i][1])
#
# print(df_word,df_freq)


# 워드 클라우드 패키지 설치
# github.com/amueller/word_cloud
# pip install WordCloud
# pip install matplotlib


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 월드컵 워드클라우드
from collections import Counter
f = open('c:/Java/data/Band.txt' , encoding='utf-8')
docs = f.read()
nouns = twitter.nouns(docs)

# 금칙어 , 광고문자 제거
import re

# wdlist = []
# stopword = '비아그라|시알리스'
#
# for i in range(0,len(nouns)):
#     nouns[i] = re.sub(stopword,'',nouns[i])
#     if len(nouns[i]) >= 2 :
#         wdlist.append(nouns[i])
#
# wc = Counter(wdlist) # 빈도수 확인
# print(wc)


# 워드클라우드로 출력
# wcimg = WordCloud(font_path=r'C:Windows/Fonts/Malgun.ttf',background_color='white', width=800,height=600).generate_from_frequencies(wc)
# plt.imshow(wcimg,interpolation='bilinear')
# plt.axis('off')
# plt.show()



# 마스크를 이용한 워드 클라우드
# pip install PIL

# import numpy as np
# from PIL import Image
# mask_path = 'c:/Java/data/bh.png'
# mask = np.array(Image.open(mask_path))
#
# wcimg = WordCloud(font_path=r'C:Windows/Fonts/Malgun.ttf',background_color='white', mask=mask).generate_from_frequencies(df)
#
# plt.imshow(wcimg,interpolation='bilinear')
# plt.axis('off')
# plt.show()
#
#
#
#
