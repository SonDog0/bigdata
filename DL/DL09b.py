

# 소설 '토지'를 word2vec으로 단어임베딩한 후
# 단어간 유사성 알아보기
# 각 문장을 품사로 분리한 후
# 조사 , 어미, 문장부호는 제외하고
# 단어사전에 저장함

# from konlpy.tag import Okt
#
# with open('c:/Java/data/lands.txt' , 'r') as f:
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
# with open('lands_pos.txt' , 'w' , encoding='utf-8') as f :
#     f.write('\n'.join(words))

# 형태소 분석시 실행하는 전처리 작업들
# 정규화 nomalization :  올바른 단어로 변환
# ex) 입니탁 => 입니다
# 어간화 stemming : 변형된 단어를 원래의 단어로 변환
# 한국어를 , 처리하는,  => 한국어, 처리 , 하다

# word2vec 모델 생성
from gensim.models import word2vec
# data = word2vec.LineSentence('lands_pos.txt')
# # 줄단위로 파일을 읽어옴
# model = word2vec.Word2Vec(data,size =100, window=7, min_count=1 ,negative=3)
# model.save('lands.model')
#
# 단어 유사성 테스트
model = word2vec.Word2Vec.load('lands.model')

print(model.most_similar(positive=['땅']))
print(model.most_similar('주인'))