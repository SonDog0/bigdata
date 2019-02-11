# 기본연산
2

# 수식
2+2
4/2
2+7*2

# 연산순위 : (),*
4*6+5

# 변수(할당연산자 : =)
a = 3
b = 3 + 75
b          # 변수 b값을 화면에 표

# 변수( 할당연한자 : <- )

c <- 3
d <- c*75
d

5 ->e
e

rm(e)     # 변수제거 


# '변수.멤버' 형태로 변수 선언 가능
name <- '혜교'
kor <- 99
eng <- 98
mat <- 99
good.code <-12345

sj.name <-'지현'
sj.kor <- 99
sj.eng <- 98
sj.mat <- 99

sj.name

# 변수의 자료형
x <- 10
class(x)         #변수의 자료형 조사
is.integer(x)    #변수가 정수형인지 조사
is.numeric(x)    #변수가 실수형인지 조사

y <- 10L
class(y)
is.integer(y)    #변수가 정수형인지 조사
is.numeric(y)    #변수가 실수형인지 조사

# 문자를 넣을시 : '' or ""
a <-'asd'
class(a)
is.character(a)
nchar(a)       # 문자 수 출력

today <-'2018-10-22'
z <- as.Date(today)  # 날짜형으로 변환 
class(z)
as.numeric(z)       #날짜를 숫자로 변환
                    #1970-01-01 기준

b <-TRUE            #논리형( 소문자 불가 )
b <- T              # TRUE 를 T로 FALSE를 F로 변환 가능
class(b)
is.logical(b)


TRUE*5
FALSE*5

# 변수 목록 확인
ls()

# 산술연산자

# 관계연산자 : >, <, ==, !=
x <- 10
y <-100
x > y
x < y
x == y
x != y