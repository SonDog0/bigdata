"""
# 반복문
어떤 문장 or 코드를
지정한 횟수나 조건에 맞게 실행

for i in range(1,3):
    print('프린트듕')

"""

for i in range(1,3):  # 2번출력
    print('프린트듕', i)

# for i in [0, 1, 2]:  # 2번출력
for i in range(0,3):  # 3번출력
    print('프린트듕', i)

"""
# 반복처리 : for
for 변수 in range(시작, 끝-1, 증가/감소):
    반복할 문장/코드
변수사용하지 않을 경우!
for _ in range( 시작, 끝-1, 증가/감소)
"""
"""
# ex) 1~ 10  출력
for i in range(1,11) :
    print(i, end=', ')
# ex) 1~50 짝수
for i in range (1,51) :
    if i % 2 == 0 :
        print(i, end=', ')

# ex ) 1~50 홀수
for i in range (1,51) :
    if i % 2 != 0 :
        print(i, end=', ')
"""
# 1~ 100까지 합
a=0
for i in range (1,101) :
    a += i
print(a)

b=0
for i in range (1,101) :
    if i%2 == 0 :
        b += i
print(b)

c=0
for i in range (1, 101) :
    if i%2 != 0 :
        c += i
print(c)

d=0
for i in range (1, 101) :
    if i%2 != 0 :
        d += i
print(d)

"""
while
반복, 변수증가,
특정조건을 확실히 알 수 없을 때 사용


"""

i = 1
while (i<=3):
    print('선생님~ 미워요!')
    i = i+1

i = 1
while (i <= 50) :
    if i % 2 == 0 :
        print(i, end=' ')
    i = i +1

print()

i = 1
a = 0
while ( i <= 100) :
    a += i
    i = i + 1
print(a)

"""
# 구구단
for i in range(1,10) :
    for j in range (1,10) :
        print(i,' x ',j,' = ', i*j)
        j = j + 1
    i = i + 1

i=1;j=1;
while (i <= 9) :
    while ( j <= 9) :
        print(i,' x ',j,' = ', i*j)
        j = j + 1
    j=1
    i = i + 1
"""

"""
# 무한 반복
while문의 조건식에 True라고 기입하면
반복을 무한대로 실행하는 반복문 생성

while True : 
    print('선생님~ 미워요!')


# 반복문 탈출 : break 
"""

# ex) 1부터 무한 합. 단, 총합이 20181128이 넘으면 자동 중단

i=1
a = 0
while True :
   i += 1
   a += i
   if a >= 20181128 :
       break;
print(a)

#
from random import *
a = input('3자리 숫자 입력')
# b = str(randint(100,999))
b = str(100)
c = [a[0],a[1],a[2]]
d = [b[0],b[1],b[2]]

print(c)

msg = '꽝'
if c in d :
    msg = '상금 1백만 지급'
elif (c[0],c[1]) or (c[0],c[2]) or (c[1],c[2]) in d :
    msg = '상금 1만지급'
elif c[0] or c[1] or c[2] in d :
    msg = '상금 1천 지급'
print(msg)
