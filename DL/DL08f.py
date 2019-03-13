import numpy as np
from keras.models import Sequential
from keras.layers import Embedding

model = Sequential()
model.add(Embedding(5,2,input_length= 5))

data = np.random.randint(5,size = (1,5))
# 정수 난수 5개 생성

model.compile('rmsprop' , 'mse')

print(data)
print(model.predict(data))