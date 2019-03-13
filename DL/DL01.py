# Deep Learning
# 딥러닝 개요

# 인공지능 - 보통의 사람이 수행하는 지능적인 작업을 자동화하기 위한 연구 활동
# 체스프로그램 - 하드코딩된 규칙만 작성 => 잘 논리된 논리적인 문제만 잘 품
# => 이미지분류, 음성인식, 언어번역 등 복잡하고 불투명한 문제는 잘못 품

# 머신러닝 - AI 선구자 앨런 튜링은 그의 기념비적 논문
# 'computing machinary and intelligence' 에서
# 범용 컴퓨터가 학습과 창의력을 가질수 있다고 결론을 내림

# => 우리가 무언가를 지시하면 그 지시내용 이상을 컴퓨터가 처리할 수 있을까 ?
# => 프로그래머가 만든 처리 규칙대신 데이터를 보고 자동으로 규칙을 학습할 수 있을까 ?

# 머신러닝 프로그램은 명시적으로 프로그램하는것이 아니라
# 작업과 관련된 샘플(데이터)을 제공하면
# 통계적 구조를 찾아 그 작업을 자동화하기 위한 규칙을 생성

# 머신러닝을 통해 입력데이터를 기반으로
# 기대출력에 가깝게 만드는 유용한 표현을 학습함
# => 분류작업 용이


# 딥러닝 - 머신러닝의 한 분야, 연속된 층 layer에서 점진적으로 의미있는 표현을 학습하는 새로운 방식
# 즉, 데이터로 부터 모델을 만드는데 얼마나 많은 층을 사용했는지가 관건 - 층 기반 학습, 계층적 학습
# 층을 겹겹히 쌓아 올려 구성한 신경망이라는 모델을 사용
# 비유) 필터(층)가 여러개 있는 여과기

# 이미지 분류, 음성인식, 필기인식, 기계번역, 자율주행
# 광고타겟팅, 웹검색결과, 자연어 대화, 뛰어난 바둑실력

# 딥러닝의 장래
# 단기간의 성과로 장미빛 전망 => 이어진 실망 => 투자 감소
# 과거 두차례의 AI 빙하기 상기 => 1960년 심블릭 AI , 1980년 전문가 시스템

# 인공지능의 단기간의 기대는 비현실적임
# => 아직 폭넓게 다양한 분야에 뿌리 내리지 못함
# => 반면, 장기적인 전망은 매우 밝은 편

# 딥러닝의 사례
# 2012년 ImageNet에서 제공하는 1000개의 카테고리로
# 분류된 100만개의 이미지를 인식하여 정확성을 겨루는
# ILSVRC라는 이미지 인식대회에서 84.7%라는 인식률을 달성
# 그전에는 75%대 - 현재는 97%에 육박함


# 딥러닝 개발 환경
# 파이썬 3.5 이상 or 아나콘다 4.4
# IDE : pycharm(venv환경)
# 머신러닝, 딥러닝 패키지 설치
# numpy , scipy , matplotlib, pandas, scikit-learn
# spyder(과학계산) seaborn(시각화) h5py(hdf5) pillow(이미지)
# tensorflow(tensorflow-gpu) keras

# 텐서플로 GPU 지원사이트
# 시스템에 nvidia GPU가 없다 => CPU만 사용하는 텐서플로 패키지
# 시스템에 nvidia GPU가 있다 => GPU를 지원하는 텐서플로 패키지
# 이럴경우 nvidia에서 제공하는 딥러닝 관련 S/W를 설치해야 함

# 자신의 GPU가 텐서플로를 지원하는지 확인
# developer.nvidia.com/cuda-gpus
# GTX 1050 - CUDA 6.1

# 텐서플로 설치방법
# tensorflow.org/install/install_windows
# tensorflow.org/install/gpu
# NVIDIA® GPU drivers —CUDA 9.0 requires 384.x or higher.
# CUDA® Toolkit —TensorFlow supports CUDA 9.0.
# CUPTI ships with the CUDA Toolkit.
# cuDNN SDK (>= 7.2)

# CUDA 툴킷 다운로드
# developer.nvidia.com/cuda-zone

# CUDA 툴킷 설치
# Experience는 제외
# 설치경로를 path로 설정 (프로그램파일\엔비디아 GPU\~~\bin)

# cuDNN(v7.3) 압축 해제(bin / include / lib / txt) 후 설치경로(C\~엔비디아GPU\~\CUDA\v9.0) 안에 덮어씌우기

# 파이참 재시작 


# cudnn 설치
#


# 텐서플로 간단예제 #1
import tensorflow as tf

# hello = tf.constant('Hello , Tensorflow!!!')
#
# sess = tf.Session() # 코드를 실행하기 위해 세션 생성
# print(sess.run(hello))

# 텐서플로 간단예제 #2
from keras.datasets import mnist
from keras import models
from keras import layers

# 케라스의 MNIST 데이터 셋 다운로드 하기
# 이미지는 numpy 배열형으로 저장
# 0~9까지 숫자이미지 저장
(Xtrain,ytrain), (Xtest,ytest) = mnist.load_data()

print(Xtrain.shape , len(Xtrain))
print(ytrain.shape, len(ytrain))

print(Xtest.shape, len(Xtest))
print(ytest.shape, len(ytest))

# 신경망 생성
# 층 layer : 데이터 처리 필터
# 데이터들이 입력되면 다음 단계에서 처리하기 용이하도록
# 유용한 형태로 변환
# 주어딘 입력데이터들에서 더 의미있는 표현을 추출해 냄
# 데이터 정재 필터가 여러 개 있는 여과기와 같음
network = models.Sequential()
network.add(layers.Dense(512, activation='relu' , input_shape=(28*28,))) # 입력층 784->512
network.add(layers.Dense(10, activation='softmax' )) # 출력층 512->10

# 신경망 분석시 중요요소 3가지
# 손실함수 : 신경망의 성능을 측정하는 지표
# 옵티마이저 : 손실함수를 기반으로 신경망 개선 , 오차역전파
# 측정 지표 : 훈련과 검증 과정을 통해 정확도 측정
network.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
# 이미지 데이터 -> categorical_crossentropy

# 전처리 #1 : 단일 색상으로 변환 (255로 나누기)
Xtrain = Xtrain.reshape((60000, 28*28))
Xtrain = Xtrain.astype('float32') / 255

Xtest = Xtest.reshape((10000, 28*28))
Xtest = Xtest.astype('float32') / 255


# 전처리 #2 : 범주형으로 변환 - 원핫인코딩
# 원핫 인코딩
# 0 1 2 3 4 5 6 7 8 9
#[0 0 0 0 0 0 0 0 0 1] 9일떄

from keras.utils import to_categorical
ytrain = to_categorical(ytrain)
ytest = to_categorical(ytest)


# 신경망에 입력데이터 훈련
# epochs : 데이터 전체를 이용해서 훈련시킬 횟수
# batch_size : 한번에 처리하는 데이터 수
network.fit(Xtrain,ytrain, epochs=5 , batch_size=128)

# 검증데이터로 테스트
test_loss , test_acc = network.evaluate(Xtest, ytest)

# 정확도 손실 확인
print('정확도' , test_acc)
print('손실(오차)정도', test_loss)


# # 텐서플로 간단 예제 # 3
# import tensorflow as tp
# from keras.datasets import mnist
# from keras import models
# from keras import layers
# import numpy as np
#
# # 수술 데이터 불러옴
# # 폐암 수술환자 데이터(0:16 , 17:수술결과)
# data = np.loadtxt('c:/Java/data/surgery.csv', delimiter= ',')
# X = data[:,0:17] # 환경변수
# y = data[:,17] # 수술결과
#
#
# # 신경망 생성
# network = models.Sequential()
# network.add(layers.Dense(30, activation='relu' , input_dim=17)) # 입력층 17->30 # 왜 증가시켜? 조합의 수를 생각 ? 공부 더 해봐야할듯 ..
# network.add(layers.Dense(1, activation='sigmoid' )) # 출력층 30->1 # 결과값이 하나니까 sigmoid를 써서 출력 하나로 함 ( 수술결과 Y/N)
#
#
# # 신경망 분석시 중요요소 3가지
# network.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
# # mean_squared_error -> 선형데이터
# # 측정지수 (mtrix => 정확도)
#
#
# # 신경망에 입력데이터 훈련
# network.fit(X,y, epochs=30 , batch_size=10)
# # 47번씩 10개 30번반복 => 47 x 10 x 30
#
# # 검증데이터로 테스트
# test_loss , test_acc = network.evaluate(X, y)
#
# # 정확도 손실 확인
# print('정확도' , test_acc)
# print('손실(오차)정도', test_loss)
#
#
# #