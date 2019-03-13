# 영화 리뷰 데이터를 바탕으로
# 긍정 / 부정 분류 분석 실시

# 인터넷 영화 디비에서 양극단으로 나뉜 5만건의 IMDB 데이터셋 이용
# 50% 비율로 훈련 / 테스트 , 긍정 / 부정으로 나뉨

from keras.datasets import imdb

(xtrain , ytrain) , (xtest , ytest) = imdb.load_data(num_words=10000)

# 훈련 데이터에서 출현빈도가 높은 10000개의 단어 추출
# 드물게 나오는 단어는 무시 - 단어수 10000개짜리 사전

# print(xtrain[0], ytrain[0])

# num_word 확인
# for i in range(0,5):
#     print([max(idx) for idx in xtrain])
#     # 각 문장의 단어에 대해 가장 큰 index 조사
#
# print(max([max(idx) for idx in xtrain]))
# # 문장들의 각 단어에 대해 가장 큰 index 조사

# 벡터화된 단어를 원래 단어로 변환
word_idx = imdb.get_word_index() # 단어사전 다운로드
# print(word_idx)
# word_idx는 단어와 idx로 구성된 dict형 자료
# 단어 입력 -> idx 출력
# 따라서 , idx 입력 -> 단어 출력 되어야 하므로 구조 변경

# print(word_idx.items()) # ex ) ('dayan' , 84842) dict 구조 출력

# print([(val , key) for (key, val) in word_idx.items()]) # key , val 형태를 key ,val 형태로 변환 출력
# ('dayan' , 84842) -> (84842, 'dayan')

new_word_idx = dict([(val , key) for (key, val) in word_idx.items()])
# key , val 형태를 key ,val 형태로 변환 후 dict 자료형에 저장
# for i in range(0,5):
#     print(new_word_idx.get(i))
# 생성된 단어사전을 이용해서 원래 문장으로 출력
# print ( [new_word_idx.get(idx-3 , '') for idx in xtrain[0]] )
# ''은 None 없애기


review_txt = ' '.join( [new_word_idx.get(idx-3 , '') for idx in xtrain[0]] )
print(review_txt)

# 전처리 작업 - 벡터화
# 문자데이터에 대해 원핫인코딩 작업 적용
# 희소행렬(대부분이 0으로 채워진 행렬)로 단어 벡터화 진행
import numpy as np

def vectorize_sequence(data , dim= 10000) :
    v = np.zeros((len(data), dim ))
    # 크기가 data x dim 인벡터에 data 만큼 0을 생성
    for i , idx in enumerate(data):
        v[i,idx] = 1. # v[i]에서 특정 위치의 값을 1로 설정
    return v

xtrain = vectorize_sequence(xtrain)
xtest = vectorize_sequence(xtest)

print([idx for idx in xtrain[0]])
# 첫번째 문장에 대해 벡터화된 결과 출력

# 나머지 벡터(ytrain , ytest)를 실수형 텐서로 변환
ytrain = np.asarray(ytrain).astype('float32')
ytest = np.asarray(ytest).astype('float32')

# 신경망 구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(16 , activation='relu' , input_dim=10000))
model.add(Dense(8, activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer=  'rmsprop' , metrics= ['accuracy'])



# 3-way 검증 방식 사용
# 훈련데이터 중 1만건을 검증데이터로 분할
xval = xtrain[:10000]
yval = ytrain[:10000]

# 1.5만건을 훈련데이터로 분할
pxtrain = xtrain[10000:]
pytrain = ytrain[10000:]

# # 훈련
# model.fit(pxtrain , pytrain , epochs=25 , batch_size=512 ,validation_data= (xval , yval))
#
# # 검증
# model.evaluate(xtest , ytest)
# print(model.evaluate(xtest , ytest)[1])
#


# 그래프로 나타내기

history = model.fit(pxtrain , pytrain , epochs=25 , batch_size=512 ,validation_data= (xval , yval), verbose=0)

hist = history.history
print(hist.keys())
# dict_keys(['val_loss', 'val_acc', 'loss', 'acc'])

import matplotlib.pyplot as plt

loss = hist['loss']
val_loss = hist['val_loss']
acc = hist['acc']
val_acc = hist['val_acc']

epochs = range(1,len(loss) + 1 )
print(epochs)

plt.plot(epochs , loss ,'ro', label = 'train loss ')
plt.plot(epochs , val_loss , 'b-' ,  label = 'vali_train loss ')
plt.legend()
plt.show()

plt.clf() # 그래프를 초기화함

plt.plot(epochs , acc ,'ro', label = 'train acc ')
plt.plot(epochs , val_acc , 'b-' ,  label = 'vali_train acc ')
plt.legend()
plt.show()

### 그래프를 그림으로써 과적합이 되지 않는 epoch를 찾아내어 model 훈련시 적절한 epoch를 쓸수있게함 ###
### 디버깅 용도로 적합한거같음 ###

