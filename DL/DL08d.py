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
maxlen = 1500 # 사용할 텍스트 길이

# 훈련 / 테스트 데이터 불러오기
(xtrain , ytrain ) , (xtest , ytest )  = imdb.load_data(num_words=max_features)
print(xtrain[0]) # 가공 전 데이터 확인

# 데이터를 단어임베딩 처리하기 편하도록
# 2D 정수 텐서로 변환함
# 제각각인 리뷰내용을 특정길이로 제한함
xtrain = preprocessing.sequence.pad_sequences(xtrain, maxlen = maxlen)
xtest = preprocessing.sequence.pad_sequences(xtest, maxlen = maxlen)

print(xtrain[0]) # 가공 후 데이터 확인

# 신경망 구성
from keras.models import Sequential
from keras.layers import Flatten , Dense , Embedding


# 단어 임베딩을 입력으로 하는 층 생성
# 단어 임베딩 차원을 8->16
model = Sequential()
model.add(Embedding(max_features , 16 , input_length=maxlen))

# 단어 임베딩 작동 원리
# 1. 훈련시킬 문장 정의
# hope to see you soon
# nice to see you again

# 2. 각 단어에 고유 정수값을 할당한 후 인코딩함 ( 단어벡터화 )
# [0, 1, 2, 3, 4]
# [5, 1, 2, 3, 6]
# 총 단어수가 7개인 단어사전을 사용함

# 3. 단어임베딩 층 정의
# Embedding(7, 2, input_length = 5)
# param1 : 훈련시 사용 할 단어 사전의 크기
# param2 : 임베딩시 사용할 좌표계 크기
# param3 : input_length; 입력단어수 (시퀀스)

# 4. 훈련시 각 단어에 대한 임베딩 결과
# 0 : [1.2 , 3.1] => hope
# 0 : [0.1 , 4.2] => to
# 0 : [1.0 , 3.1] => see
# 0 : [1.2 , 1.1] => you
# 0 : [2.2 , 3.1] => soon
# 0 : [1.2 , 3.1] => nice
# 0 : [1.2 , 3.1] => again

# 5. 임베딩 결과에 의해 각 문장을 벡터화
# [[1.2,3.1] , [0.1,4.2] , [ 1.0,3.1] , [1.2 ,1.1] , [2.2 , 3.1] ] => hope to see you soon
# 자세한 내용은 DL08f.py



# 3D 임베딩 텐서를 2D 텐서로 펼침
model.add(Flatten())

# 최종  결과 출력 (긍정 / 부정을 0~1 사이값으로 표현 )
model.add(Dense(1,activation='sigmoid'))

# 하이퍼 매개변수 정의
# rmsprop -> adam
model.compile(loss = 'binary_crossentropy', optimizer='adam' , metrics=['accuracy'])

# 생성한 신경망 설정 확인
model.summary()

# 신경망 훈련
# 3-way 방식으로 훈련(train , vali , test )
# validatio_split : 훈련/검증 비율
model.fit(xtrain , ytrain , epochs= 10 , batch_size=32 , validation_split=0.2 , verbose= 0)

# 검증
print(model.evaluate(xtest,ytest)[1])

# 긍정/부정 예측하기
text = 'i really liked the movie and had fun' #0.87
# text = 'this movie was terrible and bad' # 0.22
# text = 'fun happy nice good' # 0.26


from keras.preprocessing.text import Tokenizer
import numpy as np


tokens = []
word_idx = imdb.get_word_index() # 단어 : 인덱스 형식의 dict
for word in text.split(" "):
    tokens.append(word_idx[word])

query = preprocessing.sequence.pad_sequences([tokens],maxlen = maxlen)

y_predict = model.predict(np.array([query][0]))

print(y_predict)
print(tokens)