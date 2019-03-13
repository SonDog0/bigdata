# kmeans 분석 시각화
# 실루엣 계수를 이용한 그래프
# 군집 결과 시각화

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pandas._libs.hashtable import na_sentinel
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# 분류/군집용 가상 데이터 생성
# make_classification 분류용 데이터 생성
# make_blobs : 가우시안 분포 기반 군집용 데이터 생성

X ,y = make_blobs(n_samples= 500 , n_features=2, centers=4 , random_state= 10 ,center_box=(-15,15))
# 4개의 군집을 이루는 데이터 생성

# n_sample : 표본 데이터 수 , 기본은 100
# n_features : 독립변수의 수 , 기본은 20
# centers : 생성할 군집 수 , 기본은 3
# cluster_std : 군집의 표준편차, 기본은 1
# center_box : 생성할 군집들의 전체 크기 , 기본은 -10~10
print(X)
range_k = [2,3,4,5,6]
# 생성할 군집의 수를 리스트로 정의

plt.scatter(X[:,0] , X[:,1], marker='o' , c = y , s = 100 , edgecolors= 'k' , linewidths= 2 )
plt.show()

# 생성된 데이터를 기본 산점도로 출력
# k값에 따른 군집의 변화를 확인

for k in range_k:
    fig , (ax) = plt.subplots(1,1)
    # 그래프 작성을 위한 초기화

    # kmean 분석을 이용해서 군집화 시도
    kmeans = KMeans(n_clusters=k , random_state=1)
    predcits = kmeans.fit_predict(X)

    # 실루엣 점수 출력
    ss = silhouette_score(X, predcits)
    print(k , '=>' , ss )

    # 군집을 시각화 하기 위해 색상맵 정의
    # 예측 결과에 따라 적절한 색상을 부여
    colors = cm.nipy_spectral(predcits.astype(float) / k )

    # 부여된 색상을 기본으로 산점도 그림
    ax.scatter(X[:,0] , X[:,1], marker='.' , c = colors , s = 100 , edgecolors= 'k' )

    # 그래프에 소제목 출력
    plt.suptitle(('cluster => %d' % k), fontsize = 14 , fontweight = 'bold'  )

    # 군집의 기준점을 표시
    centers = kmeans.cluster_centers_

    ax.scatter(centers[:,0] , centers[:,1] , marker = 'o' , c = 'white' , s = 200 , edgecolors ='k')
plt.show()