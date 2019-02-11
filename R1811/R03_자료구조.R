# 변수의 자료형
x <- 10
class(x) # 변수의 자료형 조사
is.numeric(x) # 변수가 실수형인지 조사
is.integer(x) # 변수가 정수형인지 조사

y <- 10L

y
class(y)
is.integer(y)
is.numeric(y)

z <- 'abc' #문자형
class(z)
is.character(z)
nchar(z)

today <- '2018-10-22'
a <- as.Date(today) # 날짜형 변수로 변환
class(a)
as.numeric(a) #날짜를 숫자로 변환
# 출력된 숫자는 1970년 1월 1일 기준으로 며칠이 지났는지

b <- TRUE # 논리형 ( 소문자 불가)
class(b)
is.logical(b)

TRUE * 5      # T 는 값 1로 되어있음
FALSE * 5   #F는 값 0으로 되어잇음

# 변수목록 확인
ls()

#관계연산자( >, < , ==, !=)
X<-10
y<-100

X>y
X==y
X<y
X!=y

# R의 자료구조
# 스칼라 : 변수에 한개의 값을 변수에 저장
age <- 27
name <- '홍길동'

# 벡터 : 변수에 동일한 유형의 값들을 저장
# c(), seq(), rep() 함수를 사용해서 벡터 생성
# 일반적으로 하나의 변수(속성)를 저장하는 최소 단위

?c
?seq
?rep

num10 <- c(1,2,3,4,5,6,7,8,9,10)
num10

sj.name <- c('혜교', '지현', '수지')
sj.name

logi <- c(T,F,F)
twotype <- c(1,2,"3") # 백터안에 서로 다른 유형 자료의 정의
twotype

twotype2 <- c("1","2",3)
twotype2

twovec <- c(9,8,7, c(1,2,3), c(4,5,6))
# 백터안에 백터를 정의
twovec

num10 <- c(1:10) # '시작 : 끝' 형태로 벡터 정의
#numdoo <- c(0,2,4,6,8,10)
numeven <- seq(0, 10, 2) # 시작, 끝, 간격 형태로 정의
numeven
numodd <- seq(1, 10 ,2) # 시작, 끝, 간격 형태로 백터정의
# 홀수
numodd

rep1 <- rep(1:3, 3) # 특정숫자를 반복 출력
rep2 <- rep(1:3, each = 3) # 각각 출력
rep1
rep2

# 33, -5, 20, 21, 22, 23, 12, -2, -1, 0, 1, 2, 3
# 넣어보기

#num <- c(33, -5, 20, 21, 22, 23, 12, -2, -1, 0, 1, 2, 3)
nums <- c(33, -5, 20:23, 12, -2:3)
nums

# 백터 값 참조하기
# 백터의 각 요소는 []를 사용해서 위치를 
# 지정하고 참조할 수 있음
num10[5]    # 특정 요소 추출
num10[-3]   # 특정요소 제외시킴

# 백터에는 이름을 부여할 수 있음
# names()에 원하는 이름을 벡터로 넘겨줌
# 백터의 각 요소는 이름으로도 접근 가능

kor <- c(32, 45, 98)
names(kor) <- c('혜교','지현','수지')
kor
kor['수지']


# 결측치 처리
# 만약 변수 값이 존재하지 않으면 NA로 지정
one <- c(1,3,5,7,NA)
is.na(one)

# 변수만 선언하고 값을 초기화하지 않은 경우 NULL로 지정
one <- c(2,4,6, NULL)
is.null(one)
two <- NULL
is.null(two)

# NA, NULL 차이
# NA는 결측치로 인식 - 요소는 존재, 데이터만 없음
# NULL은 객체가 없음 - 요소도 없음, 데이터도 없음
# 리스트
# 성격이 다른 자료구조(벡터, 행렬, 리스트, 데이터프레임DF)를 객체로 생성
# 메모리 영역에는 키와 값 형태로 저장 - python의 dict와 유사
# 키를 통해 값을 불러 올 수 있음 - 값은 벡터, 행렬, 리스트, DF이 올 수 있음
# list 함수로 객체생성
# list 처리함수는 unlist(), lapply(), sapply() 등이 있음


sj = c('혜교', 99, 98, 99)  
sj

sj = list('혜교', 99, 98, 99)   # 키 없이 리스트 생성
sj
sj[[1]]   # 값 '혜교'에 대한 키 확인
sj[[1]][1] # 값
sj[[2]][1]
sj[1]   # 값과 키를 같이 출력
sj[2] 

class(sj) # 자료구조 유형 출력

# 리스트 구조를 벡터 구조로 변경
vsj = unlist(sj)
vsj 

# 하나이상의 값으로 리스트 객체 생성
num = list(c(1:5), c(6:10))
num
num[[1]]
num[[2]]
num[1]
num[[1]][4]
num[[2]][3]
num[2]

# 키와 값 형식으로 리스트 객체 생성
# list(키 = 값, ... ...)

sj  = list (name = '혜교', kor = 99, eng = 98, mat = 99)
sj

sj$name
sj$mat

sj[[1]]
sj[1]
sj[2]


num = list(num1=c(1:5), num2=c(6:10))
num[[1]][4]
num$num1[4]
num[["num1"]][4]
num$num2[3]

num$num1

#값 수정
sj$kor = 55    # 원소 수저

sj
sj$mat = NULL # 원소 제거
sj

num$num1 = 1

num


# 리스트 크기 확인
length(sj)
length(num)


# 데이터프레임
#R에서 가장 많이 사용하는 자료구조
#데이터베이스의  테이블 구조와 유사
# 컬럼 단위로 서로 다른 데이터 저장 가능
# 리스트와 벡터의 혼합형 - 컬럼은 벡터/리스트, 데이터는 벡터
#data.frame(), read.table(), read.csv() 로 객체 생성
#기타 처리함수는 str(), ncol(), nrow(), summary(), subset() 등이 있음
# 벡터나 행렬로 데이터프레임 객체 생성 가능
# txt, csv, excel 파일 등으로 데이터프레임 객체 생성 가능

# 먼저, 벡터로 각 변수들을 정의
names = c('혜교', '수지', '지현')
kor = c(99,98,99)
eng = c(55,77,96)
mat = c(78,56,23)

sj = data.frame(names, kor, eng, mat)
sj
sj = data.frame(이름=names, 국어=kor, 영어=eng, 수학=mat)
sj

# 행렬로도 데이터프레임 객체 생성

# txt 파일로 데이터프레임 객체 생성
customers = read.table('c:/Java/data/customers.csv', header=T, sep=',')  # 제목없음, 쉼표구분

customers

# java/data/hr/EMPLOYEES.csv
emp = read.table('c:/Java/data/hr/EMPLOYEES.csv', header = T , sep=',')
emp

# csv파일로 데이터프레임 객체 생성
getwd()   # 현재 작업 디렉토리 확인
setwd('c:/Java/data')  # 작업 디렉토리 변경
books = read.csv('books.csv', header=T)
books

# 변수이름 직접 지정
name = c('고객번호', '이름', '주소', '연락처')
customers = read.csv('customers.csv', header=F, col.names=name)
customers

# 데이터프레임 구조 확인
str(books)
str(customers)
str(emp)

# 문자열이 범주형(팩터)으로 바뀌는 것을 방지
customers = read.csv('customers.csv', header=F, col.names=name, stringsAsFactors=F)
str(customers)

# 데이터프레임 다루기
sj$국어   # 특정 열 하나만 출력

sj$이름

as.character(sj$이름)  # 범주형 변수를 문자형으로 변환

# 특정 열 하나이상 출력
#sj['국어', '영어', '수학']
# sj[2], sj[3], sj[4]
sj[,c(2:4)]
sj[c(2,4)]
sj[c(3)]

sj[c(2),]  # 2행만 출력
sj[c(1,3),]  # 1행, 3행만 출력


#데이터프레임 속성 살펴보기

sj
names(sj)  # 컬럼명 출력
ncol(sj) # 컬럼=변수=열 수 
nrow(sj)  # 행수

a = c('hello', 'age', '혜교')
nchar(a)

# 기술 통계량 확인
# 최대, 최소, 중위수, 평균, 사분위수 등을 요약
summary(sj)

# 많은 행으로 구성된 데이터 프레임 조회
numbers = data.frame( x = 1:10000)
numbers

head(numbers)  # 위에서 6행 출력
tail(numbers)
head(numbers, 10)
tail(numbers, n=3)

# 변수출력시 데이터프레임이름 생략
# attach, detach /with 사용하면 이름 생략 가능

sj$이름 = as.character(sj$이름)
sj$국어

attach(sj)
이름
국어
영어
수학
detach(sj)

attach(books)
bkid
bkname
publish
price
detach(books)

# 범주형 factor 팩터
#factor는 범주형 데이터를 표현하기 위해 사용
#범주형 : 데이터의 값이 정해진 범위 특정 값으로만 분류되는 유형
# level : 범주형 변수가 가질 수 있는 값의 목록

# 성별 : 남, 여 / M,F / male, female
# factor()를 이용해서 범주형 변수 생성

gender <- factor('남', c('남', '여'))
gender

levels(gender)  # gender 변수가 가질수 있는 값의 범위

gender <- '여'

# gender <- '동물' #범주형 변수가 문자형으로 바뀜
#levels(gender)
#gender

gender <- factor('여', c('남','여'))
as.numeric(gender)
gender
gender <- factor('남', c('남','여'))
as.numeric(gender)
gender
# 범주형 변수를 숫자형으로 바꾸면, 정의된 순서대로 수가 부여됨

hobby <- c('게임', '여행', '운동', '독서', '운동', '여행')

# 문자형 벡터를 범주형 벡터로변환가능
fhobby <- as.factor(hobby)
fhobby
# 순서형으로 변환
as.numeric(fhobby)  # 알파벳순, 가나다순, 숫자순


#행렬
# 벡터의 2차원 배열
# 동일한 유형의 요소들로 구성
# 1행은 문자, 2행은 숫자와 같은 구성은 불가
# matrix 함수로 행렬 객체 생성
# rbind(), cbind()를 이용해서 행렬을 다룸

# 5X2 행렬 생성

# 단순행렬 생성
a <- matrix(1:10)  # 열 우선으로 행렬
a

# 5X2 행렬 생성 12345 67890 - 행우선
a <- matrix(1:10, nrow=2) # 앞의 숫자는 행, 뒤숫자는 열로 지정
a
a <- matrix(1:10, ncol=2) # 열우선
a

# 2X5 행렬 생성 12 ,34, 56, 78, 90
a <- matrix(1:10, nrow=5)

# 3X3 행렬
b <- matrix(1:9, nrow=3)  # 행우선
b
b <- matrix(1:9, ncol=3) # 열우선
b

#행의 수보다 큰 수가 들어왔을 때
b <- matrix(1:10, nrow=3)
b         # 나머지 수가 반복되어 들어감

# 데이터 입력 순서 조절
b <- matrix(1:9, nrow = 3)  # 열우선
b
b <- matrix(1:9, nrow=3, byrow=T) # 행우선
b

# 행렬을 테이블 형태로 생성  : 행기준
x1 <- c(5,40,50:52)
x2 <- c(30,5,6:8)
x1
x2

x <- rbind(x1, x2)
x

y1 <- c('a', 10)
y2 <- c('b', 20)
y <- rbind(y1, y2)
y           # 벡터에서처럼 혼합형 데이터는 모두 문자형으로 변환

# 행렬을 테이블 형태로 생성: 열기준
x <- cbind(x1, x2)
x

# 10~ 19사이의 값을 2행 행렬로 표시
z <- matrix(10:19, nrow=2)
z

# 1행 전체 출력
z[1,]
# 5열 전체 출력
z[,5]
# 2행 3열의 값 출력
z[2,3]
# 1행 2열/ 3열/ 4열/ 5열 출력
z[1,c(2:5)]

# 행렬의 크기
nrow(x)
ncol(x)     
dim(x)      #행/열 동시출력
length(x)

# 행렬간 연산
a <- matrix(1:12, nrow=3)
b <- matrix(13:24, nrow=3)

a + b
a * b
a == b
a != b
a / b

# 행렬의 행/ 열에 이름 부여
colnames(a)
rownames(a)

colnames(a) <- c('첫번째','두번째', '세번째', '네번째')
rownames(a) <- c('one', 'two', 'three')

a


# 행렬 생성시 행/열 이름지정
matrix(1:4, nrow=2, dimnames=list(c('a','b'), c('x','y')))

# 배열
# n - 차원의 행렬과 유사
# 배열의 차원은 dim으로 확인
# array 함수로 배열 객체 생성
# 다른 자료구조에 비해 활용빈도 낮음

#3x2X3 형태의 배열 생성
d <- array(c(1:18), c(3,2,3))
d

# 배열 요소에 접근 
d[,,2]  # 두번째 면에 접근
d[1,,]  # 1행만 모두 출력
d[,2,]  # 2열만 모두 출력
d[3,,3] # 3번째 면의 3행만 출력

# 배열구조 확인
nrow(d)
ncol(d)
dim(d)


# 데이터 프레임에서의 부분집합subnet 추출
person <- c('peter', 'lois', 'meg', 'chris', 'stewie')
age <- c(42,40,17,41,1)
gender <- c('M','F','F','M','M')


# 데이터 프레임 생성시 범주형 변수로의 변환은 적용하지 않음
profiles <- data.frame(person,age,gender, stringsAsFactors = F)

profiles
str(profiles)


# person과 gender만 표시(gender가 먼저)


# Brian, 7, M 등의 데이터를 profiles에 추가 (행추가)
newOne <- data.frame(person='Brian', age=7, gender='M',
                     stringsAsFactors = F)
profiles <- rbind(profiles, newOne)
profiles

# 새로운 열을 추가
funny <- c('high', 'high', 'low', 'med', 'hige', 'med')
profiles <- cbind(profiles, funny)
profiles

# 새로운 열을 추가 : 계단식 이용
# age를 이용해서 총 개월 수를 계산후 열로 추가
profiles$age # 나이만 추출
profiles$age * 12
# 이름$추가할 열 이름 <- 계산식
profiles$months <- profiles$age * 12
profiles


# 성별이 남자인 행만 추출
# 데이터 프레임의 각 항목에서 특정 요소를 가르키려면
# 인덱스나 열이르므 사용
# ex) profiles[1,3]
# 조건식을 DF의 인덱스로 사용가능
profiles$gender == 'M'

# 성별이 여자인 행만 추출
# 단, 성별 열은 제외하고 추출
profiles[profiles$gender == 'F', -3]

# 나이가 10살이상인 사람은?
profiles[profiles$age > 10]

# 유머감각이 높은 사람은?
profiles[profiles$funny == 'high',]

# 나이가 10살 이상이고, 유머 감각이 높은 사람만 출력
profiles[profiles$age >= 10 | profiles$funny == 'high',]

# 나이가 10살 이상이거나, 유머감각이 높은 사람은?
profiles[profiles$age >10 & profiles$funny =='high',]
