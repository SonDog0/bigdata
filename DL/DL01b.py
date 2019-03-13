# TensorBoard
# Tensorflow에 기록된 로그를 그래프로 시각화 시켜주는 도구
# 딥러닝 성능이나 실행상황을 그래프로 출력

# TensorBoard 서버 실행
# cmd 실행후 tensorboard --logdir=c:/Java/data/logs

# Web UI 확인
# http://127.0.0.1:6006

# acc : 훈련 정확도
# loss : 훈련 손실 (오차)
# val_acc : 검증정확도
# val_loss : 검증 손실(오차)


import tensorflow as tf
import keras

from keras.datasets import mnist
from keras import models
from keras import layers

(Xtrain,ytrain), (Xtest,ytest) = mnist.load_data()

model = models.Sequential()
model.add(layers.Dense(512, activation='relu' , input_shape=(28*28,))) # 입력층 784->512
model.add(layers.Dense(10, activation='softmax' )) # 출력층 512->10
model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])


Xtrain = Xtrain.reshape((60000, 28*28))
Xtrain = Xtrain.astype('float32') / 255

Xtest = Xtest.reshape((10000, 28*28))
Xtest = Xtest.astype('float32') / 255

from keras.utils import to_categorical
ytrain = to_categorical(ytrain)
ytest = to_categorical(ytest)

# 딥러닝 진행상황을 로그에 기록하는 callback 정의
callbacks  = [
    keras.callbacks.TensorBoard(
        log_dir = 'c:/Java/data/logs' , histogram_freq = 1,
    )
]

# 딥러닝시 로그를 남기기 위해 callback을 사용
model.fit(Xtrain,ytrain, epochs=5 )

# 검증데이터로 테스트
test_loss , test_acc = model.evaluate(Xtest, ytest)

# 정확도 손실 확인
print('정확도' , test_acc)
print('손실(오차)정도', test_loss)

