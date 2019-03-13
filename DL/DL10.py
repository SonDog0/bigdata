# 네이버 영화 리뷰 분석 - MLP 사용
# 문자를 벡터로 바꾸기 - Bag of Words
# BOW는 단어별로 정수 인덱스를 부여해서
# 문장(문서)의 단어 갯수를 벡터로 변환하는 것

import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer

# 파일 읽어보기
ratings = pd.read_csv('c:/java/data/ratings.txt',sep = '\t')
review = ratings.iloc[:5 ,1]
target = ratings.iloc[:5, 2]

print(review)
print(target)

# 형태소 분석 없이 벡터화
# 텍스트 벡터화
vect =TfidfVectorizer()
vect.fit_transform(review)

kword_idx = vect.vocabulary_

print(kword_idx)


# 형태소 분석 후 벡터화 ( 추천 @@ )
twitter = Okt()
words = []

# 형태소 분리
for doc in review:
    # malist = twitter.pos(doc, norm=True , stem= True)
    # 어딜때 보고 -> 어리다 때 보다
    malist = twitter.pos(doc)
    # 어릴때 보고 -> 어릴 때 보고
    token = []
    for word in malist:
        if not word[1] in ['Josa','Eomi','Punctuation']:
            token.append(word[0])
    rl = ' '.join(token).strip()
    words.append(rl)

print(words)

# 텍스트 백터화
vect =TfidfVectorizer()
vect.fit_transform(words)
kword_idx = vect.vocabulary_
print(kword_idx)
print(len(kword_idx)) # 전체 어휘 59개

# 단어 빈도 확인
# 단어 목록을 이용해서 리뷰내용을 정수 벡터화
print('=================================================')
data = []
for i in range(0,len(words)):
    word2num =[]

    for doc in words[i].split(' '):
        if doc not in kword_idx:
            # word2num.append(0)  # 단어사전에 없는 단어이면 0 넣기
            pass # 혹은 그냥 패스
        else:
            word2num.append(kword_idx[doc])
    data.append(word2num)
print(data)

word_dic = {}
for nums in data:
    for num in nums:

        if not num in word_dic:
            word_dic[num] = 0
        word_dic[num] += 1


keys = sorted(word_dic.items(), key = lambda x:x[1] , reverse = True)

for word , count in keys[:50]:
    print('{0}({1})'.format(word, count))



