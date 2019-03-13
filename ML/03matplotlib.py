# matplotlib
# 파이썬의 대표적인 시각화 도구
# numpy 기반으로 만들어진 다중 플랫폼 데이터 시각화 라이브러리

# 하지만, 시간이 지남에 따라 인터페이스와 스타일이 고루해짐
# R의 ggplot처럼 세련되고 새로운 도구의 출현을 기대함

# 후추 깔끔하고 현대적인API로 무장한 seaborn 패키지 탄생

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 주피터노트북에서 matplotlib를 이용한 그래프 그리기
# %matplotlib inline 를 설정해 두면
# show 함수 호출 없이 그래프를 그릴 수 있음





# 간단한 선 그래프
#plt.plot([1,4,9,16,25])
#plt.show()
#       => 지정한 자료는 자동으로 y축으로 지정
#       => x축 값이 없으면 자동으로 0,1,2,3 ...으로 설정
# 즉, np.array 객체를 인자로 넘기는 경우,
# y 축만 설정하면 x 축은 자동으로 감지

np.random.seed(181218)
# #y = np.random.standard_normal(20)  # 정규분포 난수
# #print(y)
#
# #x = range(len(y))
#
# # plt.plot(y)
# # plt.show()
# # plt.plot(x,y)
# # plt.show()
#
#
#
# # 암시적 스타일 지정하기 : 색, 모양, 선
# # 색 : r,g,b,c,m,y,k,w
# # 마커 : . o v ^ 1 p * + d D
# # 선 : : -. -- -
#
# plt.plot([1,2,3,4,5],[9,8,7,6,5],'r*:')
# # plt.show()
#
#
# # 명시적 스타일로 지정하기
# # color, linewidth, linestyle, markersize,
# # marker edge color, marker edge width, marker face color
# plt.plot([1,2,3,4,5],[10,20,30,40,50],
#          c='m',lw=3,ls='--',marker='d',
#          ms=20,mec='k',mew=5,mfc='r')
# # plt.show()
#
# # 그래프 축 제어하기
# # matplotlib에서 축, 그래프, 레이블등
# # 모든 객체를 아우르는 하나의 그릇(container)
# fig = plt.figure()     # plot container
# # plt.show()             # 빈화면만 출력
# ax = plt.axes()
x = np.linspace(0,10,1000)   # 지정한 구간을 구간수로 분활
# print('분활된 구간수',x)


# # sin 그래프
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x))
# plt.grid()
# plt.show()
#
# # cos 그래프
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.cos(x))
# plt.grid()
# plt.show()
#
# # tan 그래프
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.tan(x/2))
# plt.grid()
# plt.ylim(100,-100)
# plt.xlim(2,4)
# plt.show()


# sin,cos,tan 함께 그리기 1
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), c='r')
# ax.plot(x, np.cos(x), c='b')
# ax.plot(x, np.tan(x/2), c='g')
# plt.grid()
# plt.ylim(2,-2)
# plt.xlim(10,-10)
# plt.show()

# # sin,cos,tan 함께 그리기 2
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), 'r',
#         x, np.cos(x), 'b--',
#         x, np.tan(x/2),'g-.')
# plt.grid()
# plt.ylim(2,-2)
# plt.xlim(10,-10)
# plt.show()

# # 그래프 색상 지정 방식
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x-0), c='red')  # 색상명
# ax.plot(x, np.sin(x-1), c='b')    # 단축
# ax.plot(x, np.sin(x-2), c='0.45') # 회색조 0검정 ~ 1흰 사이
# ax.plot(x, np.sin(x-3), c='#4c0b5f')    # 16진수표기(RRGGBB)
# ax.plot(x, np.sin(x-4), c=(1.0, 0.2, 0.3))    #RGB tuple(0,1)
# ax.plot(x, np.sin(x-5), c='darkred')     # HTML 색상이름
# plt.grid()
# plt.show()

# 그래프 색 모양 지정 방식
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, x+2, linestyle='solid')  # -
# ax.plot(x, x+2, linestyle='dashed')  # --
# ax.plot(x, x+2, linestyle='dotted')  # .
# ax.plot(x, x+2, linestyle='dashdot')  # -.
# plt.grid()
# plt.show()


# # 그래프 축, 라벨, 타이틀 지정
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), 'r', label='sin(x)')
# ax.plot(x, np.cos(x), 'b', label='cos(x)')
# plt.legend()
# plt.title('sin&cos function curve')
# plt.xlabel('x  value')                # x축 제목
# plt.ylabel('y value')                 # y축 제목
# plt.grid()
# plt.show()


# 타이틀 통합 지정 - axes
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), 'r', label='sin(x)')
# ax.plot(x, np.cos(x), 'b', label='cos(x)')
# ax.set(xlim=(0,10),ylim=(-2,2),
#        xlabel='x  value',ylabel='y value',
#        title='sin&cos function curve')
# ax.legend()
# # ax.set_title() 식으로 다 따로 쓸 수도 있음
# ax.grid()
# plt.show()

# matplotlib 한글 사용
import matplotlib as mpl


# ftpath = 'C:/Windows/Fonts/D2Coding-Ver1.3.2-20180524.ttf'
# fname = mpl.font_manager.FontProperties(fname=ftpath).get_name()
# mpl.rc('font',family=fname)
# mpl.rcParams['axes.unicode_minus'] = False
# mpl.rcParams['font.size'] = 20
#
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), label='사인')
# ax.legend()
# plt.show()


# 시스템에 설치된 폰트정보 알아내기
import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
print(font_list[:10])   # ttf 폰트 목록 상위 10개 출력

for f in fm.fontManager.ttflist:
    print(f.name)        # matplotlib가 관리하는 폰트 목록

for f in fm.fontManager.ttflist:
    if 'YTT' in f.fname:
        print(f.name, f.fname)        # ''가 포함된 폰트이름 출력


mpl.rcParams['font.family'] = 'Yj TEUNTEUN Bold'
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 20
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x), label='사인')
ax.legend()
plt.axhline(y=0, c='b', linewidth=1)
# plt.axvline(y=0, c='b', linewidth=1)
plt.show()