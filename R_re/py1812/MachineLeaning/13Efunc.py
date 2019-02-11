# 파이썬 외장 함수
# 사용하기 전에 반드시 해당 함수가 있는 모듈을
# import 문으로 초기화 시켜야함

# sys 모듈
# 파이썬 인터프리터가 제공하는 기본기능 제공
# sys.exit() : 파이썬 프로그램 실행 중지
# sys.path : 파이썬 모듈이 저장된 위치 출력/지정
# sys.getdefaultencoding() : 시스템의 인코딩 확인
# sys.version() : 파이썬 버젼 확인

import sys
print(sys.path)
sys.path.append('c:/Java/mypy36lib') # 새로운 파이썬 라이브러리 경로 추가
print(sys.path)

#sys.exit(0)  # 정상종료

# 프로그램 임의 종료 : sys.exit(0)
# 함수 임의 종료 : return
# 반복 임의 종료 : break

print('시스템 인코딩',sys.getdefaultencoding())
print('파이썬 버젼',sys.version)

# while True:
#     print('-=성적 프로그램=-')
#     print('1. 성적 데이터 입력')
#     print('2. 성적데이터 전체 조회')
#     print('3. 성적 데이터 검색')
#     print('4. 성적 데이터 수정')
#     print('5. 성적 데이터 삭제')
#     print('0.프로그램 종료')
#     print('----------------------')
#     code = input('작업을 선택하세요(0,1,2,3,4,5)')
#
#     if code == '1':
#         print('데이터 입력 완료')
#     elif code == '0':
#         sys.exit(0)


# os 모듈
# 시스템 환경변수, 디렉토리, 파일을 다루게 해주는 기능 제공
# os.envrion : 환경변수 확인
# os.chdir : 디렉토리 변경
# os.getcwd : 현재 작업 디렉토리 확인
# os.mkdir : 디렉토리 생성
# os.glob : 파일목록을 리스트로 가져옴

import os

print('시스템 환경변수', os.environ)
print('현재 디렉토리', os.getcwd())

print('디렉토리 변경 - c:/Java/data', os.chdir('c:/Java/data'))

print('현재 디렉토리', os.getcwd())
print('파일목록 확인', os.listdir('c:/Java/data'))

# print('디렉토리 생성1',os.mkdir('abc'))
# print('디렉토리 생성2',os.makedirs('xyz/123/987'))  # 파일 여러개를 동시에 만듬
print('파일목록 확인', os.listdir('c:/Java/data'))

# print('디렉토리 제거', os.rmdir('abc'))
# print('디렉토리 제거', os.removedirs('xyz/123/987'))

print('디렉토리 존재 유무', os.path.isdir('abc'))
print('디렉토리 존재 유무', os.path.isdir('c:/Java/data'))
print('파일 존재 유무', os.path.isfile('c:/Java/data/titanic.csv'))
print('파일 존재 유무', os.path.exists('abc'))
print('파일 존재 유무', os.path.exists('c:/Java/data/titanic.csv'))

print('파일크기 확인', os.path.getsize('c:/Java/data/titanic.csv')/1024)

print('디렉토리명/파일명 분리1', os.path.split('c:/Java/data/titanic.csv'))
print('디렉토리명/파일명 분리2', os.path.splitext('c:/Java/data/titanic.csv'))

print('디렉토리명/파일명 분리3', os.path.dirname('c:/Java/data/titanic.csv'))
print('디렉토리명/파일명 분리4', os.path.basename('c:/Java/data/titanic.csv'))

print('디렉토리명/파일명 합체',
      os.path.join('c:/Java/data','steve_ko.txt'))

joinlist =('c:/Java/data','steve_ko.txt')
print('디렉토리명/파일명 합체',
      os.path.join(joinlist[0], joinlist[1]))

print('절대경로 얻기', os.path.abspath('hr'))



# time
# 시간과 날짜 관련 함수 제공
import time

#print(time.time())   # 1970.01.01을 기준으로 초단위 출력
#print(time.localtime())
#print(time.ctime())

#time.sleep(1)  # 지정한 시간만큼 지연


# calendar : 달력을 출력하는 기능 제공
# import calendar
#
# print(calendar.calendar(2019))
# print(calendar.prmonth(2019,5))
#
# print('2019.12.25의 요일', calendar.weekday(2019,12,25))   # 0이 월요일, 6은 일요일
#
# print('2019.7의 첫날 요일과 마지막 일', calendar.monthrange(2019,8))  # 31일이고


# random : 난수를 생성하는 기능 제공
import random

# print('난수값 확인', random.random())
# print('난수값 확인', random.randint(1,10))
# print('난수값 확인', random.randint(1,10))
#
# sayHello = ['a','b','c','d','e']
# print('섞기 전',sayHello[0])
#
# random.shuffle(sayHello)
# print('섞은 후',sayHello[0])
#
# # ex) 로또 생성기 프로그램 작성
# # 1 ~ 45 사이의 임의의 숫자 6개가 생성되도록 함
# # 단, 중복 숫자가 나오지 않도록 Set을 이용함
#
# s1 = set([1,2,3,1,4,5])
# print(s1)
#
# s1.add(2)
# print(s1)

s1 = set()
while True:
    s1.add(random.randint(1,45))
    if len(s1) == 6 :
        break;
print(s1)


s2 = set()
while len(s2) != 6:
    s2.add(random.randint(1,45))
print(sorted(s2))