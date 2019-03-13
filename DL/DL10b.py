import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer

# 파일 읽어보기
from sklearn.model_selection import train_test_split

ratings = pd.read_csv('c:/java/data/ratings.txt',sep = '\t')
review = ratings.iloc[:5 ,1]
target = ratings.iloc[:5, 2]

# 형태소 분석 후 벡터화 ( 추천 @@ )
twitter = Okt()
words = []

# 형태소 분리
for doc in review:
    malist = twitter.pos(doc)
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

# 데이터, 레이블 train / test로 분리
max_feature = len(kword_idx)
maxlen = 5 # 문장길이 5로 제한

# 7:3으로 나누기
Xtrain ,Xtest , ytrain , ytest = train_test_split(data, target , test_size = 0.3 , random_state = 0 )


# 한줄로 만들기
from keras_preprocessing import sequence
Xtrain = sequence.pad_sequences(Xtrain , maxlen = maxlen)
Xtest = sequence.pad_sequences(Xtest , maxlen = maxlen)


from keras.models import Sequential
from keras.layers import Flatten , Dense , Embedding


# 단어 임베딩을 입력으로 하는 층 생성
model = Sequential()
model.add(Embedding(max_feature , 8 , input_length=maxlen))

# 3D 임베딩 텐서를 2D 텐서로 펼침
model.add(Flatten())

# 최종  결과 출력 (긍정 / 부정을 0~1 사이값으로 표현 )
model.add(Dense(1,activation='sigmoid'))

# 하이퍼 매개변수 정의
model.compile(loss = 'binary_crossentropy', optimizer='adam' , metrics=['accuracy'])

# 생성한 신경망 설정 확인
model.summary()

# 신경망 훈련
model.fit(Xtrain , ytrain , epochs= 100 , batch_size=32 ,  verbose= 0)

# 검증
print(model.evaluate(Xtest,ytest)[1])



