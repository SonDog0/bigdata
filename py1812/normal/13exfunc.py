# 파이썬 외장 함수
# 사용하기 전에 반드시 해당 함수가 있는 모듈을
# import 문으로 초기화 시켜야함

# sys 모듈
# 파이썬 인터프리터가 제공하는 기본기능 제공
# sys.exit(): 파이썬 프로그램 실행 중지
# sys.path(): 파이썬 모듈이 저장된 위치 출력
# sys.getdefaultencoding() : 시스템의 인코딩 확인
# sys.version() : 파이썬 버전 확인


# import sys
#
# print(sys.path)
#
# sys.path.append('C:/Java/mypy36lib')
#
# print(sys.path)
# print(sys.getdefaultencoding())
# print(sys.version)

# sys.exit(0) 임의로 정상종료
# 함수 임의종료 return
# 함수 임의 종료 break

# while True:
#     print('성적프로그램')
#     print('1.입력')
#     print('2.출력')
#     print('3.검색')
#     print('4.삭제')
#     print('5.수정')
#     print('6.종료')
#     print('------')
#
#     code = input ('작업선택 : ')
#     if code == '1':
#         print('입력완료')
#     elif code == '0' :
#         sys.exit(0)


# os 모듈
# 시스템 환경변수 , 디렉토리 ,파일을 다루게 해주는 기능 제공

import os
print(os.environ)
print(os.getcwd())
os.chdir('D:/Sonjunghoon/py1812/data')
print(os.getcwd())

print('파일목록확인', os.listdir('D:/Sonjunghoon/py1812/data'))

print('디렉토리 생성1', os.mkdir('abc'))