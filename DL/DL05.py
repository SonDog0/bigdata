# 퍼셉트론perceptron
# 신경망(딥러닝)의 기원이 되는 알고리즘

# 1943년 메컬러, 핏츠가 생물의 신경세포를 모방한
# 형식적인 신경모형에 대한 논문에서 최초 제안

# 1957년 프랑크 로젠블라트가 고안한 알고리즘 발표
# 전자부품을 이용해서 물리적 회로망 구성

# 입력값과 가중치의 곱을 모두 더한 후
# 활성화 함수를 적용해서 그 값이 보다 크면 1
# 작으면 -1을 출력하는 분류기를 만듦

# 1969년 민스키가 퍼셉트론의 한계를 수학적으로 증명
# 즉 , 단순한 선형분류기 이므로 간단한 XOR 분류는 수행 할 수 없음
# 이로써 인공신경망 연구는 투자 감소 - AI 암흑기

# 1986년 럼멜하트, 힌튼이 은닉층을 이용한 다층 퍼셉트론MLP와
# 역전파backpropagetion 알고리즘을 이용해서 XOR 문제를 해결함

# 1989년 러쿤은 합성곱Convolutional Neural Networks 알고리즘을 적용해서
# 필기숫자 인식 문제를 해결하는 논문 발표

# 한편, 이러한 알고리즘은 학습시간이 많이 걸리고
# 사람만이 가능한 일을 기계가 하도록 프로그래밍 하는것은
# 어려움 또한, 성능이 좋은 하드웨어를 필요로함

# MLP보다 성능이 좋은 Random Forest와
# 커널기반의 SVM이 주목받음 - 두번째 AI 암흑기

# 2006년 힌튼이 신경망  학습시 가중치의 초기값을적절히
# 조절하면 학습효과가 좋아진다고 논문발표
# 사전훈련의 중요성 설파

# 2007년 벤지오 팀이 자기부호화autoencorder를 통한
# 사전학습 방법을 제안

# 2012년 힌튼 교수의 제자 알렉스가 딥러닝 기반 알고리즘으로
# IMAGENET 이미지 분류대회에서 84.7% 정확도 달성
# 성능이 좋은 GPU의 도움을 받아 성능이 한층 개선

# 성능이 좋은 하드웨어의 출현과 인터넷의 도움으로
# 막대한 크기의 데이터를 수집해서 분석에 활용할 기회가 제공
# => 딥러닝의 성능이 한층 개선

# 퍼셉트론의 동작원리

# 가중치 weight
# 전기전자의 개념을 비유하자면
# 전류의 흐름을 억제하는 매개변수(저항)와 유사
# 오차를 발생하게 하는 외부요인 ( = 기울기 )

# 편항bias ( = 절편 )
# x1w1 + x2w2 + b < 0 이면
# y = 0
# x1w1 + x2w2 + b > 0 이면
# y = 1

# 퍼셉트론 구현하기
# 입력값 x1, x2와 가중치w1, w2들의 곱을 모두 더한 후
# 활성화함수 sigmoid를 적용해서 그 값이 0보다 크면 1
# 작으면 0을 출력하는 분류기
# 임계치theta를 넘어서면 1로 출력하기도 함

import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5]) # 가중치
    b = -0.6 # 편향
    val = 0 # 출력값
    sum = np.sum(x*w) + b # x1w1 + x2w2 + b , 행렬을 쓰면 식이 간단


    if sum > 0 : val = 1
    return val


# AND

print(AND(1,0))


def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5]) # 가중치
    b = -0.4 # 편향
    val = 0 # 출력값
    sum = np.sum(x*w) + b # x1w1 + x2w2 + b , 행렬을 쓰면 식이 간단

    if sum > 0 : val = 1
    return val

# OR

print(OR(1,0))


def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5]) # NAND는 가중치 음수로
    b = 0.6 # 편향은 최대 가중치 보다 큰 양수로
    val = 0 # 출력값
    sum = np.sum(x*w) + b # x1w1 + x2w2 + b , 행렬을 쓰면 식이 간단
    if sum > 0 : val = 1
    return val

# NAND
print('NAND 0 0 =' , NAND(0,0))
print('NAND 0 1 =' ,NAND(0,1))
print('NAND 1 0 =' ,NAND(1,0))
print('NAND 1 1 =' ,NAND(1,1))



# 단층 퍼셉트론으로는 XOR를 구현할 수 없음
# 편향값으로 XOR를 출력할 수 없음
# 베타적 논리합 XOR : 하나이상의 퍼셉트론을 이용 MLP
#  즉 , AND, OR , NAND 퍼셉트론을 조합해서 구현

def XOR(x1,x2):
    p1 = NAND(x1,x2)
    p2 = OR(x1,x2)
    val = AND(p1,p2)
    print('p1 = ', p1)
    print('p2 = ', p2)
    print('val = ', val)
    # 1 1
    # p1 : 0
    # p2 : 1
    # val : 0

    # 1 0
    # p1 : 0
    # p2 : 1
    # val : 0

    return val

print(XOR(1,0))