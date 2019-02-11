# R 패키지 수 보기시
# 패키지 : 활용가능한 함수와 재현 가능한 예제 데이터셋, 
# 사용방법 및 설명서, 도움말 등으로 구성
# R을 설치하면 기본적으로 7개의 패키지가 미리 설치됨


# R 기본 설치 패키지 수 보기
available.packages()

dim(available.packages()) # 12825개의 패키지 표시

sessionInfo() # 현재 R 실행환경, 언어집합, 설치된 패키지 표시

# 새로운 패키지 설치
# install.packages('설치할패키지명')
install.packages('stringr')

# 설치한 패키지 확인 
installed.packages()

# 패키지 제거
remove.packages('stringr')

# 패키지를 설치하고 난 후, 사용하려는 패키지는 메모리에 적재해야 함
# 패키지 사용/적재
library('stringr')  # 오류표시함 (추천!)
require('stringr')  # 경고표시

library()           # 설치된 패키지 확인


# R은 기본적으로 통계 패키지 이므로
# 다양한 데이터셋이 제공됨
data()


# R이 제공하는 기본예제
demo()                 # 데모 목록 표시

demo('graphics')       # 그래프 예제


# R의 도움말
help('Nile')          # 도움말
?Nile                 # 도움말

example(Nile)         # 함수, 데이터셋 사용예


Nile                  # 나일강 범람 수위 조사 데이


help.start()          #R에서 제공하는 기본도움말
# http://homepage.usask.ca/~chl948/doc/manual/R-intro-ko.html


# 실습
# RSADBE 패키지를 설치하고 
# 이 패키지의 도움말을 확인하고
# 데이터셋을 사용해본다

install.packages('RSADBE')
library(RSADBE)
help('RSADBE')

data(GC)
?GC
GC

data(Severity_Counts)
?Severity_Counts
Severity_Counts


# vcd 패키지 설치
# 사용가능한 함수 & 데이터집합 확인
install.packages('vcd')
library(vcd)
require(vcd)
help('vcd')
help(package='vcd')
data()



