# 파이썬 난수 생성
from random import *

print(randint(1,100))   # 1~100사이 난수

# 18번

# 19번
"""
year = int(input('윤년여부를 알고싶은 년도를 입력하세요 : '))

if (year % 4 ==0 and year % 100 != 0
    or
    year %400 == 0) :
    print('%d는 윤년입니다' % year)
else :
    print('%d는 평년 입니다')
"""
"""
# 22번
from random import *

magic = randint(1,100)
lucky = int(input('1~100사이 숫자를 입력하세요 :'))
msg = '정답'

if (magic > lucky) :
    msg = '숫자 작음'
elif(magic < lucky) :
    msg = '숫자 큼'
print(msg, lucky, magic)
"""

# if문과 리스트 객체를 함께 사용 가능
games = ['롤','스타','일랜시아','포켓몬스터','테일즈위버']
if '일랜시아' in games :
    msg ='일랜시아가 게임목록에 존재'
else :
    msg = '게임목록제 존재 하지 않음'
print(msg)

# ex)로그인 테스트
uid = ['abc123','xyz123']
pwd = ['123456','987654']

myuid = input('아이디는? ')
mypwd = input('비밀번호는? ')

if myuid in uid :
    if mypwd in pwd :
        msg = '로그인 성공'
    else :
        msg = '비밀번호 틀림'
else :
    msg = '아이디 틀림'
print(msg)