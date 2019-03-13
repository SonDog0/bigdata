# LSTM 으로 영화리뷰 분석
# LSTM 개념
# 만일, 영화의 매순간 일어나는 시간을 분류하고 싶다면 ?
# 전통적인 신경망은 이전에 일어난 사건을 바탕으로
# 나중에 일어나는 사건을 알 수 없음

# 반면, RNN(recurrent neural network)는 스스로를
# 반복하면 이전 단계에서 얻은 정보가 지속되도록 함
# RNN을 이용해서 음성인식, 언어모델링, 번역, 이미지 주석생성등
# 다양한 분야에서 굉장한 결과물을 만들어 내고 있음

# 한편 , RNN은 '장기'적으로 정보를 지속시키는 반면
# LSTM은 '단기'적으로 정보를 지속 시킬 필요가 있는 경우에 사용
# LSTM : long short term memory

# 예를 들어 이전 단어를 토대로 다음 단어를 예측하는 경우
# RNN 보다는 LSTM이 더 적절할수 있음
# 예1) 'the clouds are in the ??? ' 에서 마지막에 올 단어는 ?
# 예2) 'i grew up in Korea.. so, i can speak flunet ???' 에서 마지막에 올 단어는 ?

# 따라서 , RNN은 긴 기간의 의존성 문제를 해결할 수 있고
# LSTM은 짧은 기간의 의존성 문제를 해결 할 수 있음

# LSTM 주 구성 요소
# forget gate layer : 입력된 정보의 저장여부를 시그모이드 함수에 의해 판단
# input gate layer : 입력된 정보를 저장하기로 결정했다면 어떤 정보를 저장할지 tanh 함수에 의해 결정
# cell state : 이전에 저장된 정보에 새로운 정보를 갱신함
# output gate layer : 입력된 정보와 이전에 저장된 정보를 적절히 필터링해서 출력으로 내보냄

# 리뷰 데이터 불러오기
from keras import Sequential
from keras.datasets import imdb
from keras.layers import Embedding, LSTM, Dense
from keras_preprocessing import sequence

max_words = 20000
print('데이터불러오는중...')
(xtrain , ytrain) , (xtest, ytest) = imdb.load_data(num_words = max_words)


max_len = 80
print('리뷰 내용 벡터화 진행 중...')
xtrain = sequence.pad_sequences(xtrain , maxlen = max_len)
xtest = sequence.pad_sequences(xtest, maxlen = max_len)

print('LSTM 신경망 구성중 ')
model = Sequential()
model.add(Embedding(input_dim= max_words , output_dim=max_len))
model.add(LSTM(units=100, dropout=0.2 , recurrent_dropout= 0.2 )) # , mask_zero=True

# units : 입력 데이터 수
# dropout : 드롭아웃 시킬 노드의 비율
# recurrent_dropout : 순환층 중 드롭아웃 시킬 비율
# dropout : 입력데이터의 차원이 커서 신경망 모델이
# 복잡하면 기존의 방식처럼 가중치 감소만으로는 과적합을 방지하기 어려움
# 이것을 방지하기 위해 신경망내 노드간의
# 일부 연결을 임의로 삭제하는 것을 의미
# 즉 , 훈련시 임의의 노드를 골라 삭제하여
# 신호가 다른 노드로 전달되지 않게 함


model.add(Dense(units=1 , activation='sigmoid'))

model.compile(loss = 'binary_crossentropy' , optimizer= 'adam' , metrics=['acc'])
print(model.summary())

# 신경망 훈련
print('신경망 훈련 시작 ...')
model.fit(xtrain , ytrain , epochs= 3 , batch_size= 32 )

# 모델 평가
print('모델 평가 시작 ...')
loss_acc = model.evaluate(xtest,ytest , verbose= 0 )
print(loss_acc[0] , loss_acc[1] * 100)

# 모델 저장
print('모델 저장중 ...')
model.save('imdb_LSTM_model.h5')



