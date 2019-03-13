# 과적합 문제 해결
# 1998년 존스홉킨스 대학 세즈노프스키 교수가
# 힌튼 교수가 발표한 역전파 알고리즘에 관심을 가짐
# 즉 , 은닉층과 역전파의 효과가 얼마나 큰지 궁금

# 따라서, 광석과 일반돌에 음파를 쏘아 측정치 조사
# 과연 이 돌을 잘 분류 할 수 있을지 실험 (sonar.csv)

# 논문결과 : 은닉층의 수가 올라갈수록
# 데이터 예측 정확도도 같이 상승
# 학습/검증 데이터로 분리해서 진행하면
# 학습 예측 정확도는 여전히 증가하지만
# 증가속도가 다소 지연됨

# 과적합 방지 방법 - 데이터를 train / test로 분리해서 훈련 실시 ( + 교차검증 )

from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import tensorflow as tf

# 측정치 데이터 불러오기
sonar = pd.read_csv('c:/java/data/sonar.csv',header=None)

x = sonar.iloc[:,0:60]
y = sonar.iloc[:,60]

print(x)
print(y)

# 전처리 수행
# target 값 : R/M 을 0 /1 로 바꿔주기

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(y)
y = le.transform(y)

print(y)

# 난수 지정
seed = 190121
np.random.seed(seed)
tf.set_random_seed(seed)

# 신경망 구성
# 입력층(25) + 은닉층 + 출력층
# 출력층 활성화 함수 : sigmoid
model = Sequential()

model.add(Dense(25,input_dim=60, activation='relu'))

# model.add(Dense(16,activation='relu'))
# model.add(Dense(8,activation='relu'))

model.add(Dense(1,activation='sigmoid'))


# 손실함수 , 최적화 함수 정의
# mean_squared_error : 회귀
# binary_crossentropy : 이항분류
# categorical_crossentropy : 다항분류

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy']) #정확도,오차

# 훈련
# model.fit(x,y,epochs=100)
#
# # 정확도 확인
# print('%.4f'% model.evaluate(x,y)[1])

# 과적합을 방지하기 위해
# 데이터셋에서 train/test 데이터로 분리
from sklearn.model_selection import train_test_split
xtrain , xtest , ytrain , ytest = train_test_split(x , y , test_size=0.3 , random_state=seed)

model.fit(xtrain,ytrain,epochs=300)

# 평가
print(model.evaluate(xtest,ytest))

model.save('models/sonar.h5')

