# matplotlib
# 파이썬의 대표적인 시각화 도구
# numpy 기반으로 만들어진 다중 플랫폼 데이터 시각화 라이브러리

# 하지만, 시간이 지남에 따라 인터페이스와 스타일이 고루해짐
# R의 ggplot 처럼 새로운 도구 출현 기대

# 추후에 API로 seaborn 패키지 탄생

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 간단한 서 그래프

# plt.plot([1,4,9,16,25])
# plt.show()

# 지정한 자료는 자동적으로 y축으로 지정
# x축 값이 없으면 0,1,2,3,...로 설정
# 즉, np.array 객체를 인자로 넘기는 경우
# y축만 설정하면 x축은 자동적으로 감지

np.random.seed(181218)
y = np.random.standard_normal(20) # 정규분포 난수 20개
x= range(1,21)
# plt.plot(y) #자동감지 사용
# plt.plot(x,y)

# 주피터 노트북에서 matplotlib를 이용한 그래프 그리기
# %matplotlib inline를 설정해두면
# show 함수 호출없이 그래프를 그릴 수 있음


# 스타일 지정하기 : 색 , 모양 , 선
# 색 : rgb
# 마커 : . / o / v / ^ / 1 / p / * / d / D
# 선 | , - , --

plt.plot([1,2,3,4,5] , [9,8,7,6,5] , 'r^')
# plt.show()

# 명시적 스타일로 지정하기
# color, linewidth , linestyle, markersize
# marker edge color, marker edge width, marker face color

# plt.plot([1,2,3,4,5] , [10,20,30,40,50] , c ='m' , lw='3' , ls='--', marker ='d' , ms = '20' , mec = 'k' , mew = '5' , mfc = 'r')
#
# plt.show()


# 그래프 축 제어하기
# figure : matplotlib에서 축, 그래프, 레이블등
# 모든 객체를 아우르는 하나의 그릇 (container)


x = np.linspace(0,10,1000)# 지정한 구간을 구간수로 분살 0 ~ 10 1000구간
print('분할된 구간수 :', x)
print('sin 함수 값 ' , np.sin(x))

fig = plt.figure()
ax = plt.axes()
ax.plot(x,np.sin(x))
plt.grid()  # 모눈 표시








# 그래프 한글 출력하기
import matplotlib as mpl
plt.style.use('classic')
mpl.rcParams['font.family'] = 'BM YEONSUNG'
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 10


# 그래픽 스타일 지정하기
x = np.linspace(0,10,1000)# 지정한 구간을 구간수로 분산 0 ~ 10 1000구간

fig = plt.figure()
ax = plt.axes()
ax.plot(x,np.sin(x) , label = 'zhtkdls')
plt.grid()  # 모눈 표시

plt.show()


