# 딥러닝의 가장 말단 분석 기법
# => 단순/다중 선형회귀, 로지스틱 회귀, 분류

# 회귀에서 가장 중요한 작업 -> 예측선 긋기

# 공부시간과 성적에 대한 상관/회귀 분석
X = [2,4,6,8]
y = [81,90,94,97]

# 그래프를 이용한 탐색적 분석
import matplotlib.pyplot as plt

plt.scatter(X,y)
plt.axis([1,9,75,100]) # x축은 1~9 y축은 85 ~100
# plt.show()


# 각 점들을 가로지르는 직선을 그어보자
# y = ax + b  ( a: 기울기 , b : y절편)
# 기울기와 절편은 최소제곱법을 이용하면 쉽게 구해짐
# 기울기 공식 : ( x - x평균 )( y - y평균 )의 합 / ( x - x평균 )의 제곱합
# 절편 공식 : y평균 - (x평균 * a )

#  x , y 평균값
import numpy as np
# 벡터 연산 => 넘파이
mX = np.mean(X)
my = np.mean(y)
print(mX,my)

# 기울기 공식의 분자 : ( x - x평균 )( y - y평균 )의 합
print(len(X)) # 4

def top(x,mx,y,my):
    d = 0
    for i in range (len(x)):
        d += (x[i] - mx ) * (y[i] - my)
    return d
diver = top(X,mX,y,my)
print(diver)

# 기울기 공식의 분모 : (x - x평균) 의 제곱합
divsor = [ sum((i-mX)**2 for i in X)]
# for comprehension 찾아보기

# 기울기와 절편 구하기
a = diver / divsor
b = my - (mX*a)

# 결과출력
print('기울기' ,a)
print('절편' , b)

# 예측값을 넣어 회귀선을 그려봄
z = []

for xx in X:
    z.append(a*xx + b)
    print('예측값' , z )


plt.plot(X,z,'ro-')
plt.show()