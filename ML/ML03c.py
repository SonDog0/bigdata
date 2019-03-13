import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mglearn


sms = pd.read_csv('c:/java/data/SMSSpam' , sep = '\t' , header= None)

# 정상메일(ham)과 스팸메일spam 수량 확인

print('정상수' , sms[sms[0] == 'ham'][0].count())
print('스팸수' , sms[sms[0] == 'spam'][0].count())
print(sms.head())

sns.countplot(sms[0])

# 텍스트 전처리 작업 실시

# 문자로 구성된 sms데이터를 로지스틱 회귀가 가능하도록
# 적절한 전처리 작업 실시 - BOW 사용

# BOW : bag of words => 문자/문서를 숫자 벡터로 변환
# 먼저 , 전체 문자/문서에 대한 단어장 생성
# 그런다음, 문서 내 단어의 출현빈도를 측정해서
# 개별 단어장에 저장

# BOW 문자 전처리 종료
# 머신러닝으로 분석하는 사례 중 텍스트를 이용하는 경우가 있음
# 이런경우 문자를 벡터값으로 인코딩 해서 처리해야함

# DictVectorizer : 각 단어를 세어 사전 생성
# CountVexctoprizer "; 단어 토큰을 만들고 단어수를 세어 사전생성
# tfidVectorizer : 각 단어에 가중치 두어 사전 생성

# CountVectorizer 예제
from sklearn.feature_extraction.text import CountVectorizer
sentence = ['UNC played Duke in baseball, Duke lost the basketball game']

vectors = CountVectorizer()
print('변환된 벡터값' , vectors.fit_transform(sentence).todense())

# UNC played Duke in baseball, Duke lost the basketball game' 문장을 알파벳순으로 정렬한 후 순번 부여
# {UNC:8 , played :6 ,duke:2 , in:4, baseball:0 , lost:5 , the :7  , basketball : 1 , game : 3 }
# =>{ baseball, basketball, game, in, lost, played, the, UNC}

# 각 문서의 내용을 토큰 리스트로 생성
# 각 문서에서 토큰의 출현순서를 셈
# 각 문서를 BOW 벡터값으로 변환

print('추출한 어휘' , vectors.vocabulary_)
print('추출한 패턴' , vectors.fit_transform(sentence)[0])

# 새로운 문장을 추가하면 :?

sentence.append('Is this last document')
vectors.fit_transform(sentence).todense()
print('추출한 어휘' , vectors.vocabulary_)

# TfidVectorizer 예제
# term frequency (전체 문서 대비 특정 단어 빈도수 )
# inverse document frequency (특정 문서 대비 특정 단어가 문서에 출현하는 빈도 )

# Tfidf : 텍스트 마이닝에서 이용하는 가중치 부여 방식으로
# 여러 문서로 이루어진 문서군에서 어떤 단어가 특정 문서상에서
# 얼마나 중요한 것인지를 의미하는 통계적 수치
# Tf가 크면 (여러문서에 단어가 출현) -> 자주등장 -> 중요
# Tf의 역수인 idf가 크면 (특정 문서에 단어 출현) -> 중요함 -> 가중치 부여

# 예 ) 신문과 방송에서 '독감' 언급 : Tf가 높음
# 예 ) 특정 언론에서 '테블릿' 언급 : idf 가 높음

from sklearn.feature_extraction.text import TfidfVectorizer

sentence = ['UNC played Duke in baseball' , 'Duke lost the basketball game']

vectors = TfidfVectorizer()

print('변환된 벡터 값' , vectors.fit_transform(sentence).todense())
print('추출한 패턴' , vectors.vocabulary_)

sentence.append('Is this last document')


print('변환된 벡터 값' , vectors.fit_transform(sentence).todense())
print('추출한 패턴' , vectors.vocabulary_)

###

# smsspam 데이터를 TfidfVectorizer로 전처리 함
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import re

# idx 1 = 내용 , 0 = 스팸/햄 여부
data = sms[1].values
target =sms[0].values
# 문자 전처리 관련 패키지
# pip install nltk
import nltk
nltk.downloader('stopwords') # 불용어 사전 다운로드
from nltk.corpus import stopwords
stopwords = stopwords.words('english')


X_train , X_test , y_train, y_test = train_test_split(data, target , random_state= 0)

# 문자 데이터 tfidf 벡터화 실시
vectors = TfidfVectorizer()
vX_train = vectors.fit_transform(X_train) # [[],[],[]]
vX_test = vectors.transform(X_test) # [,,,]

print(X_train)
print(X_test)
print('######')
print(vX_train)
print('@@@@@@')
print(vX_test)

# logr = LogisticRegression(solver='liblinear')
#
# logr.fit(vX_train , y_train)
#
# print('훈련 정확도' , logr.score(vX_train , y_train))
# print('검증 정확도' , logr.score(vX_test , y_test))
#
# # 실제 값을 넣어서 예측하기
#
# pred = logr.predict(vX_test)
# for i in range(0,10):
#     print(pred[i] , vX_test[i], X_test[i])
#

