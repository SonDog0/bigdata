# 위키피디아를 덤프해서 word2vec 으로 워드임베딩한 후
# 단어간 유사성 알아보기
# dumps.wikimedia.org/kowiki=> lastest => kowiki-latest-pages-articles.xml.bz2 다운로드

# xml파일 -> text 추출하기
# => wikiextractor.py 를 이용

# WikiExtractor.py -b 51200k -o c:\Java\data\extract_wiki c:\Java\data\kowiki-latest-pages-articles.xml.bz2

# 분할된 파일 하나로 합치기
#  cd /java/data/extract_wiki/AA
# type wiki_00
# type * > wiki.txt
# 대용량 파일은 EmEditor로 열어야 함

from konlpy.tag import Okt

import re
# with open('c:/java/data/extract_wiki/AA/wiki.txt' ,encoding='utf-8') as f:
#     docs = f.readlines()
#
# print(docs[:5])
#
# # 태그 제거
# wiki = []
#
# for doc in docs:
#     if len(doc) > 3 :
#         wiki.append(re.sub(r'<.*>','',doc)) # >로 시작하고 <로 끝나는 모든 문자 제거
#
# # 제거된 내용을 파일에 저장
# with open('c:/java/data/extract_wiki/AA/wiki2.txt' ,'w' , encoding='utf-8') as f:
#     for i in range (0,len(wiki)):
#         f.write(wiki[i])
#     # for line in wiki:
#     #   f.write(line) 과 동일 ..!




# 형태소 분석 후 품사 추출
# with open('c:java/data/extract_wiki/AA/wiki2.txt','r' ,encoding='utf-8') as f:
#     docs = f.readlines()
#
# twitter = Okt()
# words = []
#
# for doc in docs:
#     word_list = twitter.pos(doc, norm= True , stem= True)
#     r = []
#     for word in word_list:
#         if not word[1] in ['Josa' , 'Eomi' , 'Punctuation']:
#             # 조사, 어미 , 문장부호가 아니라면
#             r.append(word[0])
#     rl = ' '.join(r).strip()
#     if len(rl) > 2 :
#         words.append(rl)
#
# # 품사 추출한 결과물을 파일로 저장
# with open('c:/java/wiki_pos.txt' , 'w' , encoding='utf-8') as f :
#     f.write('\n'.join(words))
#
#

# word2vec 모델 생성
from gensim.models import word2vec
# data = word2vec.LineSentence('c:/java/wiki_pos.txt')
# # 줄단위로 파일을 읽어옴
# model = word2vec.Word2Vec(data,size =100, window=7, min_count=1 ,negative=3)
# model.save('c:/java/data/wiki.model')
#


# 단어 유사성 테스트
model = word2vec.Word2Vec.load('c:/java/data/wiki.model')

print(model.most_similar(positive=['Python']))
print(model.most_similar('주인'))
print(model.most_similar('아빠'))
print(model.most_similar(positive=['왕자' , '여성']))
print(model.most_similar('파이썬'))
print(model.most_similar('PHP'))
print(model.most_similar('경주'))