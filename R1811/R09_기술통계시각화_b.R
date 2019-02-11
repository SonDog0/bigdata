# 막대 그래프
# 도수분포표를 막대 모양으로 시각화 한 것
# 자료의 범주별 빈도를 요약해서 나타내는 그래프



dose <- c(20,30,40,45,60)
drugA <- c(16,20,27,40,60)
drugB <- c(15,18,25,31,40)

barplot(dose, col='red')
barplot(drugA, col='blue')
barplot(drugB, col='green')

barplot(dose, xlab='환자번호' , ylab='약물반응도' , main='약물에 대한 환자 반응도',
        col=c('red','orange','yellow','green','blue'), names.arg=c(1:5))

barplot(drugA, xlab='환자번호' , ylab='약물반응도' , main='약물에 대한 환자 반응도',
        col=c('red','orange','yellow','green','blue'), names.arg=c(1:5),
        horiz=T)

# leadership  데이터에서
# 매니저별 나이 막대그래프
manager = c(1,2,3,4,5)
date = c(as.Date('2010-10-24'),as.Date('2010-10-28'),
         as.Date('2010-01-14'),as.Date('2010-12-14'),
         as.Date('2005-01-14'))
country = c('US','US', 'UK','UK', 'UK')
gender = c('M','F','F','M','F')
age = c(32,45,25,39,99)
q1 = c(5,3,3,3,2)
q2 = c(4,5,5,3,2)
q3 = c(5,2,5,4,1)
q4 = c(5,5,5, NA, 2)
q5= c(5,5,2,NA,1)


leadership = data.frame(manager, date, country, gender, age, q1, q2, q3, q4, q5)

leadership
str(leadership)


barplot(leadership$age, names.arg = c(1:5),
        xlab='매니저번호', ylab='나이', main='매니저별 나이 현황',
        col=seq(1:5))

# 매니저별 국적 현황 - 막대그래프
table(leadership$country)
barplot(table(leadership$country), xlab='국적',ylab='빈도수',main='매니저별 국적 현황')


# 매니저별 성별
genders<- table(leadership$gender)
barplot(genders, xlab='성별',ylab='빈도수',main='매니저별 성별 현황',
        ylim=c(0,4), col=c('red','blue'))


# hotdog-winner
# 연도별 학도그 먹은 갯수를 그래프로 작성
hotdog_winner <- read.table(file.choose(), header=T, sep=',',stringsAsFactors = F)
head(hotdog_winner)
str(hotdog_winner)

barplot(hotdog_winner$Dogs.eaten, names.arg=c(1980:2010))

setwd('c:/Java/data')
hotdog <- read.csv('hot-dog-winners.csv', sep=',',stringsAsFactors = F, header = T)
barplot(hotdog$Dogs.eaten, names.arg = hotdog$Year)

# 핫도그 컨테스트 우승국
str(hotdog)
countrys<-table(hotdog$Country)   # 알파벳 순 정렬 
countrys<-sort(table(hotdog$Country),decreasing = T)     # 크기별 정렬 내림차순

barplot(countrys, col=seq(1:4))

winners <- sort(table(hotdog$Winner), decreasing = T)
barplot(head(winners,3))


# apllewood 데이터 셋을 참고 막대 그래프
apple <- read.table('applewood.txt', sep=' ',header = T, stringsAsFactors = F)
str(apple)

# 지역별 자동차 판매대수
location <- sort(table(apple$Location),decreasing=T)
barplot(location, ylim = c(0,60), xlab = '지역',ylab = '판매대수', main='지역별 자동차 판매대수',
        col=c('red','orange','yellow','green'), las=2)

# 차종별 판매대수 
vhicle <- sort(table(apple$Vehicle.Type), decreasing = T)
barplot(vhicle, xlim = c(0,70), xlab ='자동차 판매 대수' ,ylab = '차종', main='차종별 자동차 판매대수',
        col=c('red','orange','yellow','green','blue'), las=2, horiz=T)


# 타이타닉 데이터 셋
# 성별 생존수를 막대 그래프로 작성
titanic <- read.csv('titanic.csv', sep=',', header = T, stringsAsFactors = F)
str(titanic)
sex<- table(titanic$Sex)
survived <- table(titanic$Survived)

barplot(sex)
barplot(survived)

ex <- table(titanic$Sex, titanic$Survived)
barplot(ex[,2], ylim=c(0,250))


# 클래스별(승선권유형-pclass)별 생존수  
survived <- table(titanic$Pclass,titanic$Survived)
barplot(survived[,2], ylim=c(0,140), main='생존자')  
barplot(survived[,1], ylim=c(0,400), main='사망자')

# 누적 막대 그래프
barplot(survived, ylim=c(0,600), main='사망자')

barplot(survived, xlim=c(0,600), main='사망자', beside=T, horiz = T, names.arg=c('사망자','생존자'),col=c('red','blue','green'))
legend('topright',c('1등석','2등석','3등석'), pch=1, col=c('red','blue','green'))

str(titanic)




# S:southampton, C:cherbourg, Q: queens
# 승선 지역별 탑승자수
# ok <- !is.na(titanic$Embarked)
ok <- titanic$Embarked != ''
em <- table(titanic$Embarked[ok])
em
barplot(em, ylim=c(0,650))

# 승선 지역별 성별
table(titanic$Sex,titanic$Embarked)
emsex <- table(titanic$Sex,titanic$Embarked)
barplot(emsex ,ylim = c(0,650), beside=T, col=c('red','blue'),
        names.arg = c('etc','cherbourg','queens','southampton'))
legend('topleft', c('여자','남자'), fil=c('red','blue'))

# 승선 지역별 승선권 유형
table(titanic$Pclass,titanic$Embarked)
emti <- table(titanic$Pclass,titanic$Embarked)
barplot(emti, beside=T, col= c('red','blue','green'),
        names.arg = c('etc','cherbourg','queens','southampton'))
legend('topleft', c('1등석','2등석','3등석'), fil=c('red','blue','green'))

# 승선 지역별 생존자, 사망자 수
table(titanic$Survived, titanic$Embarked)
emsu <- table(titanic$Survived, titanic$Embarked)
barplot(emsu, beside=T, col=c('red','blue'),
        names.arg = c('etc','cherbourg','queens','southampton'))
legend('topleft', c('사망자','생존자'), fil=c('red','blue'))
