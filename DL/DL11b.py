# LSTM으로 리뷰 분석

from keras.models import load_model
import numpy as np
from keras.preprocessing import sequence
from keras.datasets import imdb
max_len = 80


# 모델불러오기
print('모델불러오는중 ...')
model = load_model('imdb_LSTM_model.h5')
print(model.summary())

# 모델예측
text = 'the movie was a great waste of my life'
text = 'i really liked the movie and had fun'
# text = 'this movie was terrible and bad'
# text = 'happy nice fun great'
# text = 'this movie is a bomb'
# text = 'this move is the bomb'
#
print('결과 예측중입니다')
word_idx = imdb.get_word_index()
token = []
for word in text.split(' '):
    token.append(word_idx[word] + 3 )

query = sequence.pad_sequences([token] , maxlen = max_len)

y_pred = model.predict(query)
print(text , y_pred)



