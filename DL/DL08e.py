# 로이터 뉴스 데이터 분류
# x : 기사
# y : 카테고리 ( 46개 주제 )

from keras.datasets import reuters

(xtrain , ytrain ) , (xtest , ytest ) = reuters.load_data(num_words=15000)

print(xtrain[2])

# 3-way 데이터 분할
# 총 데이터 11,228건
# 훈련/시험 : 8982건 / 2246건
# 훈련/검증/시험 : 7000/1982/2246

# 검증을 위한 데이터 생성
x_val = xtrain[7000:]
y_val = ytrain[7000:]

xtrain = xtrain[:7000]
ytrain = ytrain[:7000]

print('검증값 길이 =>',len(x_val))
print('훈련값 길이 =>',len(xtrain))

# 입력 데이터의 길이가 다르므로 ( 어떤사람을 기사를 길게쓰고 , 짧게쓰고 , 길이가 각각 다름 )
# pad_sequence함수로 동일한 길이를 가지도록 데이터 조정 (이 코드에선 120개로 제한)
# 신경망 주입시 같은 행렬크기
# 모자르면 앞 0으로 채우고
# 넘으면 빈도수에 따라 채움

from keras.preprocessing import sequence
maxlen = 120
xtrain = sequence.pad_sequences(xtrain , maxlen = maxlen)
x_val = sequence.pad_sequences(x_val,maxlen=maxlen)
xtest = sequence.pad_sequences(xtest , maxlen= maxlen)
print(xtrain[2])


# 뉴스의 주제가 46개 => 다항
# 따라서 , 주제 결과값을 담고 있는 레이블을
# 원핫인코딩으로 변경해야함
# 다항분류에서는 y값을 원핫인코딩으로 바꿔줘야함 !!!!

from keras.utils import np_utils

ytrain = np_utils.to_categorical(ytrain)
ytest = np_utils.to_categorical(ytest)
y_val =  np_utils.to_categorical(y_val)

print('원핫인코딩 변경 = > \n',ytrain)


# 신경망 구성(MLP)
from keras.models import Sequential
from keras.layers import Dense , Flatten , Embedding


# 입력층
# 입력된 단어들을 차원에 매핑  15000 x 128 x maxlen 만큼의 차원으로 공간생성
model = Sequential()
model.add(Embedding(15000 , 128 ,input_length= maxlen))

#3D -> 2D
model.add(Flatten())

# 2D->1D
# model.add(Dense(256,activation='relu'))

# 출력층
model.add(Dense(46 , activation='softmax'))

# 하이퍼 매개변수
model.compile(loss = 'categorical_crossentropy', optimizer='adam' , metrics=['acc'])

# 모델 훈련 - > 3-way
model.fit(xtrain,ytrain , epochs=10, batch_size=64 , validation_data= (x_val , y_val))

# 모델 시험
print(model.evaluate(xtest, ytest)[1])

#
# # 모델 예측
# y_predict = model.predict()


