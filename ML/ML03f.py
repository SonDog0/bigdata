# rottentomato 염화 감상자료를 이용한
# 다항 로지스틱 회귀분석
# 감상평은 0(부정) ~ 2(중립) ~ 4(긍정)으로 분류됨

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

movies = pd.read_csv('c:/java/data/RottenTomato.tsv' , sep='\t')
print(movies)

sns.countplot(movies['Sentiment'])
# plt.show()

# 전처리 : 소문자 변환 , 숫자 , 기호 제거
import re

data = movies['Phrase'].str.lower()

pd.set_option('display.max_columns', 500)
print(data)

tmp = []
for line in data:
    line = re.sub('[^a-z]' ,' ' ,line) # 숫자 / 기호 제거
    line = re.sub('[\s]+', ' ' , line) # 공백 하나로 합침
    tmp.append(''.join(line.strip()))
data = tmp
# print('\n#######\n' )
print(data)
# print(data[:10])
#
target = movies['Sentiment']

# 훈련/검증 데이터로 분리

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

X_train, X_test , y_train, y_test =train_test_split(data,target,random_state=0)

# 문자 데이터를 숫자 데이터로 변환
vectors = TfidfVectorizer()
tr_X_train = vectors.fit_transform(X_train)
tr_X_test = vectors.transform(X_test)
# fit_transform() : 단어사전 생성하고 단어 빈도 조사
# transform() : 만들어진 단어사전을 토대로 단어 빈도 조사

# 다항 로지스틱 회귀 분석
logr =LogisticRegression(solver='saga' , multi_class= 'multinomial')
logr.fit(tr_X_train, y_train)

print('훈련 정확도' , logr.score(tr_X_train , y_train))
print('검증 정확도' , logr.score(tr_X_test , y_test))


# 오차행렬 출력
predict = logr.predict(tr_X_test)
print('' , confusion_matrix(y_test,predict))


