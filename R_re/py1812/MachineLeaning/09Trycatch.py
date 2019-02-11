"""
# python 예외처리
프로그램을 만들다 보면 수많은 에러가 발생함
코드를 잘못 작성하거나, 실행상의 문제로 인해 에러가
발생하면 프로그램 실행이 중단되기도 함

하지만, 프로그램이 중단되는 것을 피하기 위해
이러한 에러는 무시하고 넘어가줬으면 싶을때도 있고
에러에 따른 적절한 처리를 하고 싶을 때도 있을것임

파이썬에서는 try-catch-except 코드로 예외처리를 할 수 있음
"""
"""
# error vs exception
프로그램 실행 중 오작동이나 비정상적인 종료를 유발 - error
error => 컴파일 오류, 실행오류

컴파일 오류 - 코드 오작성 원인 => 개발자 조치가능

실행오류1 - 실행상의 논리적 오류가 원인 => 개발자 조치 가능
ex) 숫자입력요구 -> 문자입력 -> 오류발생

실행오류2 - 실행상의 외적 오류 원인 => 개발자 조치 불가능
ex) 디비접속프로그램 -> 네트워크 오류 -> 조치 불가능
ex) idc 화재발생 -> 시스템 불능 -> 조치 불가능
위의 경우에는 복구할 수 없는 심각한 오류 발생!



예외 : 개발자가 완전히 조치 할 수 없는 심각하지만
어느정도 수습할 수 있는 수준의 덜 심각한 오류
예외처리를 통해 프로그램의 비정상 종료를 막을 수 있음
"""

# 오류발생예
print('프로그램 실행 시작')
print(10/5)
#print(10/0)

lists=[1,2,3]
print(lists[2])
#print(lists[3])

print('프로그램 실행 끝')


# try - except 문
# try:
#     오류발생 구문
# except:
#     오류 발생시 처리할 코드

try:
    print(10/1)
except:
    print('초등학교도 안나오셨어요..?')

try:
    print('begin1')
    print(10/1)
    print('end1')
except:
    print('초등학교도 안나오셨어요..?')

try:
    print('begin2')
    print(10/0)    # 오류 발생시 except로 넘어감
    print('end2')  # 즉, 오류 발생시 이 코드는 실행되지 않음
except:
    print('초등학교도 안나오셨어요..?')


# exception 절에 예외이름을 지정하면
# 특정 예외발생했을 때만 처리 코드를 실행 할 수 있음

try :
    # lists = [1,2,3]
    # lists[3] = 9
    # print(10/0)
    print('%d'%'a')
except IndexError:
    print('리스트의 인덱스가 초과됨')
except ZeroDivisionError:
    print('초딩나왔...?')
except Exception as e:
    print(e,'오류 발생')

# 파이썬 3의 예외처리 계층도
# python.org -> dacumentaion -> python 3.x docs -> Library Reference -> Exception hierarchy