"""
# 조건문
주어진 상황에 따라 적절 한 명령문을 수행하는 문장
프로그래밍에서 조건을 판단하여
해당 조건에 맞는 상황을 수행하는 데 사용됨
조건문 작성시 반드시 들여쓰기에 따라 문장을 작성해야 함
조건문은 일반적으로 비교연산자를 이용한 문장이나
논리연산자를 이용한 문장으로 구성
비교연산자 : x > 100, y != 123
논리연산자 : (x > 100) and (y != 123)




if 조건문 :
    수행할 문장

if 조건문:
    수행할 문장1
else:
    수행할 문장2

"""

# 총점이 90보다 크면 '우수'라고 출력
total = 85

if (total >= 90):
    print('우수')
else :
    print('공부하세요')
# 나이가 18보다 크고 20보다 작거나 같으면 '성년을축하해'라고 출력
age = 19

if (age >18 and age <= 20) :
    print('성년을 축하해')
else :
    print('넌 머냐')

"""
# if ~ else if 조건문을 단순하게 작성하기
if 조건문1 :
    수행문장
elif 조건문2 :
    수행문장
elif 조건문3 :
    수행문장
else :
    수행문장
"""

# 나이에 따라 축하메세지 출력
# 19~30; 31~40; 41 ~
age = 34
"""
if age >19 and age <=30 :
    print('성년을 축하해')
elif age > 30 and age <=40 :
    print('장년을 축하해')
else :
    print('중년을 축하해')
"""

if age >40 :
    print('중년을 축하해')
elif age >30 :
    print('장년을 축하해')
elif age >=19 :
    print('성년을 축하해')

# 만 나이 계산 프로그램
# 생년과 월일을 입력받아 만 나이 출력
# 생년 => 1984
# 월일 =>  1215
print('-= 만나이 계산 프로그램 =-')
print('이름, 생년, 월일 순으로 입력하세요')
name = input('이름입력')
byear = int(input('생년입력'))
bdate = int(input('월일 입력'))

"""
from datetime import datetime
year = datetime.today().year
month = datetime.today().month
day = datetime.today().day

age = year - byear

if bdate <= month*100 + day :
    age=age    
    print('%s님의 만나이는 %d입니다' % (name, age))
else :
    age = age -1
    print('%s님의 만나이는 %d입니다' % (name, age))
"""

from datetime import datetime
year = datetime.today().year
date = str(datetime.today().month) + str(datetime.today().day)

age = year - byear

if int(date) < bdate:
    age=age-1
    print('%s님의 만나이는 %d입니다' % (name, age))
else:
    age = age
    print('%s님의 만나이는 %d입니다' % (name, age))