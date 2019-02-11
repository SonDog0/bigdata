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
# 복권
# 파이썬에서 문자열은 문자의 리스트 집합
# 따라서 문자열의 각 문자는 리스트

from random import *
lucky = str(input('3자리 숫자 입력'))
lotto = str(randint(100,999))
match = 0
msg = '꽝'

# if (lucky[0] == lotto[0] or
#     lucky[0] == lotto[1] or
#     lucky[0] == lotto[2] ):
#     match += 1
# if (lucky[1] == lotto[0] or
#     lucky[1] == lotto[1] or
#     lucky[1] == lotto[2] ):
#     match += 1
# if (lucky[2] == lotto[0] or
#     lucky[2] == lotto[1] or
#     lucky[2] == lotto[2] ):
#     match += 1

for i in range(0,2) :
    for j in range(0,2) :
        if (lucky[i] == lotto[j]) :
            match += 1

print(lotto, lucky, match)

if match == 1 :
    msg = '천원 당첨'
if match == 2 :
    msg = '만원 당첨'
if match == 3 :
    msg = '100만원 당첨'
print(msg)
"""


# 숫자만 입력받아 구구단 출력
# 문자입력시 ASCII 코드 출력 : ord()
# 아스키 코드 입렷기 문자 출력 : chr()
# print(ord(0),ord(9),chr(48),chr(57))
"""
# 숫자 맞추기 게임
magic = randint(1,100)
while True:
    lucky = int(input('1~100사이 숫자 입력'))

    if (lucky == magic):
        msg = '정답'
        print(msg)
        break
    elif ( lucky > magic):
        msg ='정답보다 큼'
        print(msg)
    elif(lucky < magic):
        msg='정답보다 작음'
        print(msg)
"""
# 구구단 테이블
for i in range(1,10):
    print('%d|%2d' %(i,i), end='')
    for j in range(2, 10):
        print('  %2d' % (i*j), end='')
    print()


# 주민번호 유효성검사
# 주민번호 각 자리를 2,3,4,5,6,7,8,9,2,3,4,5 의 가중치를 곱함
# 곱한결과를 각각 모두 더함
# 더한값을 11로 나눠 나머지를 구함
# 나머지와 맨 마지막 자리와 일치여부 검사

jumin = '9105161262011'
jumin = '1111111111118'
sum = 0
"""
# 2,3,4,5,6,7,8,9,2,3,4,5
sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[6]) * 8
sum += int(jumin[7]) * 9
sum += int(jumin[8]) * 2
sum += int(jumin[9]) * 3
sum += int(jumin[10]) * 4
sum += int(jumin[11]) * 5

# a모두 더한 값을 11로 나눈 나머지 계산
mod = sum % 11
checker = 11-mod

# 나머지가 2자리인지 여부 검사
if checker > 9 :
    if (int(str(checker)[1])) == int(jumin[12]) :
        print('유효한 주민번호')
    else:
        print('유효하지 않은 주민번호')

elif (checker == int(jumin[12])) :
    print('유효한 주민번호')
else :
    print('유효하지 않은 주민번호')
"""
"""
for i,j in zip(range(0,12), range(2,10)):  # 이런식으로 사용 가능!
"""

jumin = '1111111111118'
sum = 0
w = [2,3,4,5,6,7,8,9,2,3,4,5]

for i in range(len(w)):
    sum += int(jumin[i])*w[i]
    print( )
checker = (11 -sum%11) % 10
if (checker == int(jumin[12])) :
    print('유효한 주민번호')
else :
    print('유효하지 않은 주민번호')


# 35번 잔돈계산 프로그램
# 10 50 100 500 1000 5000 10000 50000 단위로 수량 계산
# 지불해야 하는 금액 : 12340원
# 지불금액 : 100000
# 잔돈


cost = 12340
money = 100000
charge = money - cost

"""
print('잔돈 :',charge)

c50000 = charge//50000    # // : 몫을 구하는 연산자
charge = charge % 50000    # % : 나머지 연산자
c10000 = charge//10000
charge = charge % 10000
c5000 = charge//5000
charge = charge % 5000
c1000 = charge//1000
charge = charge % 1000
c500 = charge//500
charge = charge % 500
c100 = charge//100
charge = charge % 100
c50 = charge//50
charge = charge % 50
c10 = charge//10
charge = charge % 10

print('50000 :',c50000)
print('10000 :',c10000)
print('5000 :',c5000)
print('1000 :',c1000)
print('500 :',c500)
print('100 :',c100)
print('50 :',c50)
print('10 :',c10)
"""
coins =[50000,10000,5000,1000,500,100,50,10]
ctitle = ['5만원','1만원','5천원','1천원','5백원','1백원','50원','10원']
cqty = [0,0,0,0,0,0,0,0]

print(charge )

for i in range(len(coins)) :
    cqty[i] = charge//coins[i]
    charge = charge % coins[i]
    print(ctitle[i],cqty[i])

# 특정년도의 1월 달력
# ((년도 -1)*365 + ((년도-1)/4 - (년도-1)/100 + (년도-1)/400))%7
# => (년도-1)의 12월 마지막 날의 요일 출력
# 따라서, 수식결과에 +1를 해주면 해당년도 1월1일의 요일 출력

# 먼저, 0001-01-01의 요일 확인
import datetime
wday = ['월','화','수','목','금','토','일']   # 이건 파이썬 버젼
# print(datetime.date(1,1,1).weekday())   # 파이썬의 요일은 월요일부터 시작
# print(datetime.date(2018,11,30).weekday())
# wd = datetime.date(1,1,1).weekday()
# print(wday[wd])

# wd = datetime.date(2018,11,30).weekday()
# print(wday[wd])


# 이건 직접 가정하고 짠것이라서 다름!
wdays = ['일','월','화','수','목','금','토']
year = int(input('년도는?'))

wday = ((year-1)*365 + ((year-1)//4 - (year-1)//100 + (year-1)//400)) % 7

print('%d년의 12월 31일은 %s요일' % (year-1, wdays[wday]))

# 만년 달력...?