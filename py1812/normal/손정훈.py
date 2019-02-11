### 1, 텍스트 마이닝과 형태소 분석 관련 패키지와 사전 설치하세요

from konlpy.tag import Okt
from collections import Counter
twitter = Okt()
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re


### 2. 예제 파일을 읽어 텍스트 데이터를 가져오고 데이터에서 명사 추출하세요

# 텍스트 데이터 가져오기
f = open('c:/Java/data/president.txt' , encoding='utf-8')
docs = f.read()

# 명사추출
nouns = twitter.nouns(docs)

# 금칙어 , 광고문자 제거


### 3. 데이터 전처리를 하세요

# 공백, 문장부호 ,숫자 제거
docs = re.sub("\s+", " " , docs)
docs = re.sub("\W+", " " , docs)
docs = re.sub("\d+", " " , docs)
print(docs)


### 4. 문자길이가 2자 이상인 단어만 추출하고 빈도수를 계산하세요
wdlist = []

# 2자이상 단어 추출
for i in range(0,len(nouns)):
    if len(nouns[i]) >= 2 :
        wdlist.append(nouns[i])

wc = Counter(wdlist) # 빈도수 확인
print(wc)



### 5. 계산된 단어 빈도수를 기반으로 워드클라우드를 작성하세요
# # 워드클라우드로 출력
wcimg = WordCloud(font_path=r'c:/Windows/Fonts/malgun.ttf',background_color='white')\
    .generate_from_frequencies(wc)
plt.imshow(wcimg, interpolation='bilinear')
plt.axis('off')
plt.show()
#
