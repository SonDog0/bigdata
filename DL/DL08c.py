# 영화리뷰 긍정 / 부정 평가하기
# 사람의 언어를 완벽하게 단어 임베딩으로 매핑해서
# 어떤 자연어 처리작업에도 사용할 수 있을까 ? = > 다소 불가능

# 세상에는 많은 언어가 있고 , 언어는 특정 문화와
# 환경을 반영하기 때문에 서로 유사성 찾기에는 어려움
# 새로운 언어에 대한 임베딩은 새롭게 학습해야 함
# 역전파와 LSTM을 이용하면 어느정도 해결 가능함

from keras.datasets import imdb
from keras import preprocessing

max_features = 10000 # 특성으로 사용할 단어 수
maxlen = 20 # 사용할 텍스트 길이

# 훈련 / 테스트 데이터 불러오기
(xtrain , ytrain ) , (xtest , ytest )  = imdb.load_data(num_words=max_features)
print(xtrain[0]) # 가공 전 데이터 확인

# 데이터를 단어임베딩 처리하기 편하도록
# 2D 정수 텐서로 변환함
# maxlen : 문장길이 제한 , maxlen보다 모자르면 0으로 채움
# 즉 , 제각각인 리뷰내용을 특정길이로 제한함
xtrain = preprocessing.sequence.pad_sequences(xtrain, maxlen = maxlen)
xtest = preprocessing.sequence.pad_sequences(xtest, maxlen = maxlen)

print(xtrain[0]) # 가공 후 데이터 확인

# 신경망 구성
from keras.models import Sequential
from keras.layers import Flatten , Dense , Embedding


# 단어 임베딩을 입력으로 하는 층 생성
# 단어를 기하학적 공간에 매핑할수 있도록 벡터화 함
model = Sequential()
model.add(Embedding(max_features , 8 , input_length=maxlen))

# 3D 임베딩 텐서를 2D 텐서로 펼침
# 3차원 데이터를 xy평면에 나타내기위해 2D변환
model.add(Flatten())

# 최종  결과 출력 (긍정 / 부정을 0~1 사이값으로 표현 )
# 즉 , 0.5 기준으로 긍정/부정이 나뉨
model.add(Dense(1,activation='sigmoid'))

# 하이퍼 매개변수 정의
model.compile(loss = 'binary_crossentropy', optimizer='rmsprop' , metrics=['accuracy'])

# 생성한 신경망 설정 확인
model.summary()

# 신경망 훈련
model.fit(xtrain , ytrain , epochs= 10 , batch_size=32)

# 검증
print(model.evaluate(xtest,ytest)[1])

# 긍정/부정 예측하기
text = 'i really liked the movie and had fun' #0.26
# text = 'this movie was terrible and bad' # 0.22
# text = 'fun happy nice good' # 0.26
# text = 'disgusting movie and hate it fucking go away' # 0.31

from keras.preprocessing.text import Tokenizer
from numpy import array
tokenizer = Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(text)
token = tokenizer.texts_to_sequences(text)
print(token)

# texts_to_sequnces에 의해 토큰화된 텍스트를
# 1D 형태로의 벡터로 변환
tokens = []
for idx in token:
    for j in idx:
        tokens.append(j)
print(tokens)

query = preprocessing.sequence.pad_sequences([tokens],maxlen = maxlen)
y_predict = model.predict(array([query][0]))

print(y_predict)