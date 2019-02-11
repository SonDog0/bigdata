# 히스토그램
# 막대그래프
# 연속형 데이터의 빈도표를 작성해서
# 막대 그래프로 나타낸 것
# x 축 : 변수구간
# y축 : 구간 빈도

heights <- c(168,172,176,163,174,179)
h <- hist(heights, ylim=c(0,3))
h   # 히스토그램 상세정보- 구간 도수 밀도

# 변수 구간 재설정
hist(heights, breaks = 2)
setwd('c:/Java/data')
birth <- read.csv('birth-rate.csv',sep=',',header = T, stringsAsFactors = F)

summary(birth)

# 2008년 출생수를 히스토그램으로 작성
y2008 <- birth$X2008[!is.na(birth$X2008)]
head(y2008)
y2008
str(birth)

# 기본 계급은 0~5, 5~10, ...
hist(y2008,
     main='2008년도 출생자 수',
     xlab='출생자수 구간', ylab='출생자수 빈도수')

# 수정 계급은 0~10, 10~20, ...
hist(y2008, breaks=5,
     main='2008년도 출생자 수',
     xlab='출생자수 구간', ylab='출생자수 빈도수')

# 재수정된 계급은 0~2, 2~4, 4~6, ...
hist(y2008, breaks=25,
     main='2008년도 출생자 수',
     xlab='출생자수 구간', ylab='출생자수 빈도수')

hist(y2008, breaks=25,
     main='2008년도 출생자 수',
     col=rainbow(25))

# 구간의 범위를 벡터로 정의
hist(y2008, breaks=c(0,10,20,30,40,50,60),
     main='2008년도 출생자 수',
     col=rainbow(25))

# seq함수를 사용해서 구간범위 지정
hist(y2008, breaks=seq(0,60,2),
     main='2008년도 출생자 수',
     col=rainbow(25))

hist(y2008, breaks=seq(8,54,2),
     main='2008년도 출생자 수',
     col=rainbow(25))

# 정규 분포 확률밀도 그리기

hist(y2008, breaks=seq(5,55,10),
     main='2008년도 출생자 수',
     col=rainbow(25), freq=F, ylim=c(0,0.05))
lines(density(y2008), lwd=2, col='blue')


# 각 그래프에 도수값 출력
h<-hist(y2008, breaks=seq(5,55,5),
     main='2008년도 출생자 수',col=rainbow(25), ylim=c(0,70))
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))
    # x좌표 y좌표 라벨에 찍을 위치 조정(labels = h$counts, adj=c(0.5,-0.5))


h<-hist(y2008, breaks=seq(5,55,5),col=rainbow(25),
        main='2008년도 출생자 수',
        xaxt="n", yaxt="n")
# axis(1,c(5,10,15,20,25,55))
axis(1,seq(5,55,5), pos=-1)
axis(2,seq(0,70,2), pos=4)


# applewood 판매현황 데이터 참고
applewood<-read.table('applewood.txt',sep= ' ',header=T, stringsAsFactors = F)
summary(applewood)
# 나이별 구매현황을 히스토그램으로 작성
h<-hist(applewood$Age, col=rainbow(7), breaks=seq(15,80,5), ylim=c(0,40), 
        main='차량구매자 나이 분포 ')
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))
hist(applewood$Age, col=rainbow(7), breaks=seq(15,80,5),ylim=c(0,0.05),
     freq = F)
lines(density(applewood$Age), lwd=2, col='black')


# 판매금액 환황을 히스토 그램으로 작성
# 문자 대체 : gsub - apple<-gsub('$',' ',applewood$Profit)
install.packages('stringr')
library(stringr)
applewood$Profit<-str_replace_all(applewood$Profit,'\\$','')
applewood$Profit<-str_replace_all(applewood$Profit,',','')

apple <- as.numeric(applewood$Profit)
apple
summary(apple)

# 계급수 계산법
# 1. 구간 갯수 파악 - 제곱법칙
length(applewood$Profit) #  2^7 ~ 180 ~ 2^8 따라서 계습수: 8

# 2. 구간 범위 지정 : 294 ~ 3292 : (max - min)/k -> 374.75 -> 400

# 3. 구간의 한계값 지정 : 294 ->200, 3292 ->3400


h<-hist(apple, col=rainbow(15), breaks=seq(200,3400,400),ylim=c(0,50),
        main='판매금액 현황',xaxt="n", yaxt="n")
axis(1,seq(200,3400,400), pos=-0.1)
axis(2,seq(0,50,5), pos=200)
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))

hist(apple, col=rainbow(15), breaks=seq(200,3400,400),ylim=c(0,0.0008),
     freq = F)
lines(density(apple), lwd=2, col='black')


# 핫도그 컨테스트 데이터셋
hotdog<-read.csv('hot-dog-winners.csv',sep = ',',header = T, stringsAsFactors = F)
summary(hotdog)
length(hotdog$Dogs.eaten) # 5개
(68-9.1)/5
# 핫도그 우승자의 핫도그 먹은 개수 현황
h <- hist(hotdog$Dogs.eaten, col=rainbow(5),breaks=seq(0,75,15),ylim=c(0,16),
          xaxt='n')
axis(1,seq(0,75,15))
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))

hist(hotdog$Dogs.eaten, col=rainbow(10),ylim=c(0,0.05),
     freq = F)
lines(density(hotdog$Dogs.eaten), lwd=2, col='black')

# 타이타닉 데이터셋
age<-titanic$Age[!is.na(titanic$Age)]
age
# 탑승자의 나이에 현황
h <- hist(age, col=rainbow(10),breaks=seq(0,80,10),ylim=c(0,250))
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))

hist(age, col=rainbow(10),ylim=c(0,0.04),
     freq = F)
lines(density(age), lwd=2, col='black')



#나이대별 사망/ 생존 현황을 히스토그램으로 작성
as<-table(titanic$Age,titanic$Survived)
as






# 인사정보HR 데이터셋 참고
emp<-read.csv('hr/employees.csv',sep=',',header = T, stringsAsFactors = F)
summary(emp$SALARY)
# 사원들의 급여 현황
h <- hist(emp$SALARY, col=rainbow(10),breaks = seq(2000,25000,1000),ylim=c(0,30),xaxt='n')
axis(1,seq(2000,25000,1000), pos=-0.1)
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))

hist(emp$SALARY, col=rainbow(10),ylim=c(0,0.00025),
     freq = F)
lines(density(emp$SALARY), lwd=2, col='black')



# 사원들의 부서 현황
h <- hist(emp$DEPARTMENT_ID, col=rainbow(10),breaks = seq(0,110,10),ylim=c(0,50),xaxt='n')
axis(1,seq(0,110,10), pos=-0.1)
text(h$mids, h$counts, labels = h$counts, adj=c(0.5,-0.5))

hist(emp$DEPARTMENT_ID, col=rainbow(10),ylim=c(0,0.06),
     freq = F)
lines(density(emp$DEPARTMENT_ID), lwd=2, col='black')

