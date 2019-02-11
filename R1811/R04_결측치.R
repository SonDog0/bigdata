# 결측치, 이상치 처리
# 실제 데이터들 중 오류를 포함할 가능성은 언제나 존재
# 따라서 분석 전 이러한 오류들은 바로 수정해야함

# 결측치 missing Value - NA
# 누락된 값, 비어있는 값
# 함수/ 수식 적용 불가 - 분석 결과 왜곡
# 제거 또는 적절한 값으로 대체한 후 분석실시

# 결측치 확인
is.na(leadership)
# 빈도표 작성
table(is.na(leadership))

is.na(leadership$q4) # 결측치 확인
sum(is.na(leadership$q4)) # 결측치 총 갯수

# 결측치 채우기
# 중심 경향 값 넣기 : 평균, 최빈값, 중앙값
# ->( 분석 결과는 비교적 양호 )
# 난수값 넣기 : 정규분포를 따름
# 회귀 분석을 이용한 값 넣기 : 관측치의 특성을 고려
# 상황에 따라 결측치를 제외할 수도 있음

leadership$q4[4] <- 3
leadership$q5[4] <- 3
leadership

leadership$sumq <- c('','','','','')
leadership$meanq <- c('','','','','')
leadership <- within(leadership, {
  sumq <- q1+q2+q3+q4+q5
  meanq <- sumq/5
})
leadership

# 결측치 제거
x <- c(1,2,3,NA,5)
y <- sum(x)
# 결측치가 포함된 벡터에 sum함수 적용 -> 결과는 NA
y

y<-sum(x,na.rm=T)  # 결측치는 제외하고 sum적용

na.omit(x) # 결측치를 자료구조에서 아예 제외
x
na.exclude(x)

# leadership 예제에서는 na.rm=T를 이용해서 계산
leadership <- within(leadership,{
  sumq[1] <- sum(q1[1],q2[1],q3[1],q4[1],q5[1], na.rm=T)
  sumq[2] <- sum(q1[2],q2[2],q3[2],q4[2],q5[2], na.rm=T)
  sumq[3] <- sum(q1[3],q2[3],q3[3],q4[3],q5[3], na.rm=T)
  sumq[4] <- sum(q1[4],q2[4],q3[4],q4[4],q5[4], na.rm=T)
  sumq[5] <- sum(q1[5],q2[5],q3[5],q4[5],q5[5], na.rm=T)
})

# na.omit를 이용해서 계산
leadership <- na.omit(leadership)
leadership
# NA 있는 필드가 사라짐

# 결측치 예제 - titanic (kaggle.com)
# 타이타닉 생존요인 예측
# 변수 설명 : 승객번호, 생존여부(1:생존) , 승선권 등급(1:특석)
# 이름, 성별, 나이, 형제수, 자식수수, 승선권 번호, 승선권 요금
# 객실 번호, 승선항구명(C:cherbourg, Q:queenstown, S:southampton)

setwd('c:/Java/data')
titanic = read.csv('titanic.csv', header=T, sep=',')
head(titanic, 10)  # 위에서 10개 데이터 확인
tail(titanic, 10)  # 아래서 10개 데이터 확인

# 결측치 조사 - 빈도표로 나타냄
is.na(titanic)
table(is.na(titanic))

sum(is.na(titanic$Age))          # 177
sum(is.na(titanic$Cabin))        # 0 
# but 엑셀에서 확인 시 0개가 아님
# 한편, 문자열을 factor형으로 변환하지 말것!
# 빈값""은 반드시 NA로 설ㅈ
titanic = read.csv('titanic.csv', header=T, sep=',',stringsAsFactors = F, na.string=c("NA",""))
table(is.na(titanic))            # 866

sum(is.na(titanic$Age))          # 177
sum(is.na(titanic$Cabin))        # 687 

head(titanic$Cabin, 10)
head(titanic$Age, 10)

# Age 결측치는 177건이므로 적정한 값으로 대체
# Cabin의 결측치는  687이므로 필드 자체를 제거함
titanic$Cabin <- NULL
str(titanic)

# 살아남은 승객 수는 얼마나 되나?
titanic[titanic$Survived == 1,]
nrow(titanic[titanic$Survived == 1,])

table(titanic$Survived == 1)


# 승객 중 남자는 얼마나 되는가?
nrow(titanic[titanic$Sex == 'male',])
table(titanic$Sex)

# 동반한 자녀수가 2이고 남자인 승객 수는?
table(titanic$Parch==2 & titanic$Sex=='male')
nrow(titanic[titanic$Sex == 'male' & titanic$Parch==2, ])

# 살아남은 승객중 남자수와 여자는?
nrow(titanic[titanic$Survived==1 & titanic$Sex=='male', ])

nrow(titanic[titanic$Survived==1 & titanic$Sex=='female', ])

# 서울시 우편번호 파일을 읽어서
# 도로명 주소 '약수암길 9-13'를 조회
zipcode = read.csv('Seoul-2017.10.csv', header=T, sep=',',stringsAsFactors = F, na.string=c("NA",""))

sum(is.na(zipcode))
sum(is.na(zipcode$읍면))
sum(is.na(zipcode$시군구용건물명))
sum(is.na(zipcode$리명))

zipcode[zipcode$도로명 == '약수암길' & (zipcode$건물번호본번 ==9 & zipcode$건물번호부번 ==13),]

# NA값을 ''로 변경
zipcode$읍면[is.na(zipcode$읍면)] <- ''
sum(is.na(zipcode$읍면))
head(zipcode,10)

# 경기도 우편번호 파일을 읽어서
# 각자의 주소 조회
zipcode2 = read.csv('kwd.txt', header=T, sep='|',stringsAsFactors = F, na.string=c("NA",""))
zipcode2[zipcode2$도로명 == '후석로228번길' & zipcode2$건물번호본번 ==24,]


