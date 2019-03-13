# 데이터과학 분야 핵심 구성요소
# 선형대수학 - 행렬, 벡터
# 통계적 모델링 - 기술적/추론적 통계
# 컴퓨터 프로그래밍 - 자바/파이썬
# 데이터 저장 및 검색기술 - 하둡/스파크, 하이브
# 시각화/ 그래프 분석 - ggplot, tableau
# 비지니스 인테리젼스


# 데이터 과학 처리용 패키지 배포판 - 아나콘다
# continuum.io
# 약 450개 패키지 포함
# numpy, scipy, pandas, (선형대수학)
# matplotlib            (시각화)
# scikit-lean,          (머신러닝)
# tensorflow,keras      (신경망 딥러닝 - nvidia GPU)
# NLTK,                 (자연어 처리)
# juypter               (분석자료 공유)

# 데이터 과학 패키지 선언 방법
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# 머신러닝용 데이터셋 확인
from sklearn import datasets

iris = datasets.load_iris()              # 붓꽃 데이터
boston = datasets.load_boston()          # 보스톤 집값 데이터
wine = datasets.load_wine()              # 와인 품질 데이터
breast = datasets.load_breast_cancer()   # 유방암 검진 데이터

# print('iris', iris.keys())               # 데이터의 셋의 각 항목 확인
# print('boston', boston.keys())               # 데이터의 셋의 각 항목 확인
# print('wine', wine.keys())               # 데이터의 셋의 각 항목 확인
# print('breast', breast.keys())               # 데이터의 셋의 각 항목 확인
#
# # print('붓꽃 데이터', iris.data)
# print('붓꽃 분류값', iris.target)
# print('붓꽃 이름', iris.target_names)
# print('붓꽃 이름', iris.DESCR)

# # 시각화
# data = iris.data
# plt.plot(data[:,0], data[:,1], 'go')
#                             # sepal.length, sepal.width
# plt.plot(data[:,2], data[:,3], 'r*')
#                             # petal.length, petal.width
# plt.show()


# 보스톤 집값
# 소매업(2), 오염도(4), 검정색, 기호:+
print(boston.DESCR)
data = boston.data
plt.plot(data[:,2], data[:,4], 'k+')
plt.show()