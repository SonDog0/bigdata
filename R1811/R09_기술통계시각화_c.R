# 파이 그래프
# 도수분포표를 원 모양으로 시각화 한 것
# 자료의 범주별 빈도 비율을 요약해서 나타내는 그래프

val = c(10,20,30,40,50)
pie(val)

# 시작 각도 위치 지정
pie(val, init.angle = 90)

# 색상과 값 제목 표시
pie(val, init.angle = 90,
    col=rainbow(length(val)), label=c('가','나','다','라','마'))

 
pie(val, init.angle = 90,
    col=rainbow(length(val)), label=paste(val,'%'))
legend(1, 0.9,
       c('가','나','다','라','마'),
       fil=rainbow(length(val)))

# 각 수치간 임의 비율로 그래프 작성

# 각 항목별 비율 계산
pct <- round(val/sum(val)*100)
pct
pval <- paste(pct,'%')
pval



# 매니저별 국적 비율 파이그래프로 작성
val1 <- leadership$country
t1 <- table(val1)
pie(t1, init.angle = 90)
text(0,0.3, 3, col='white')
text(0,-0.3, 2, col='white')

# 매니저별 성별 비율 파이그래프로 작성
val2 <- leadership$gender
t2 <- table(val2)
pie(t2, init.angle = 90)



# 핫도그 컨테스트 최대 우승국 비율
val3 <- hotdog$Country
t3 <- sort(table(val3), decreasing = T)
aa <- round(t3/sum(t3)*100)
aa
?pie
pie(t3, init.angle = 90,
    label=paste(aa,'%'), col=c('red','blue','green','yellow'),
    clockwise = T)
legend('topleft',names(t3), fil=c('red','blue','green','yellow'))

pie(t3, init.angle = 90,
    label=paste(aa,'%'), col=rainbow(t3),
    clockwise = T)
legend('topleft',names(t3), fil=rainbow(t3))


# 핫도그 컨테스트 최다 우승자 비율
val4 <- hotdog$Winner
t4 <- sort(table(val4), decreasing = T)
bb <- round(t4/sum(t4)*100)
bb

pie(t4, init.angle = 90,
    label=paste(bb,'%'), col=rainbow(length(names(t4))),
    clockwise = T)
legend(1,1, names(t4), fill = rainbow(t4))

# 지역별 자동차 판매 대수 비율
apple <-read.table(file.choose(), header=T, sep=' ')
val5 <- apple$Location
t5 <- sort(table(val5), decreasing = T)
cc <- round(t5/sum(t5)*100)

pie(t5, init.angle = 90,
    label=paste(cc,'%'), col=rainbow(length(names(t5))),
    clockwise = T)
legend('topleft', names(t5), fill = rainbow(length(names(t5))))


# 차종별 자동차 판매 대수 비율
val6 <- apple$Vehicle.Type
t6 <- sort(table(val6), decreasing = T)
dd <- round(t6/sum(t6)*100)

pie(t6, init.angle = 90,
    label=paste(dd,'%'), col=rainbow(length(names(t6))),
    clockwise = T)
legend('topleft', names(t6), fill = rainbow(length(names(t6))))




# 타이타닉 데이터 셋
# 생존/ 사망
t7 <- sort(table(titanic$Survived), decreasing = T)
ee <- round(t7/sum(t7)*100)

pie(t7, init.angle = 90,
    label=paste(ee,'%'), col=rainbow(length(names(t7))),
    clockwise = T)

legend('topleft',names(t7),fill=rainbow(length(names(t7))))

# 승선권 유형별
t8 <- sort(table(titanic$Pclass), decreasing = T)
ff <- round(t8/sum(t8)*100)

pie(t8, init.angle = 90,
    label=paste(ff,'%'), col=rainbow(length(names(t8))),
    clockwise = T)

legend('topleft',names(t8),fill=rainbow(length(names(t8))))
# 승선위치별
t9 <- sort(table(titanic$Embarked), decreasing = T)
gg <- round(t9/sum(t9)*100)

pie(t9, init.angle = 90,
    label=paste(gg,'%'), col=rainbow(length(names(t9))),
    clockwise = T)

legend('topleft',names(t9),fill=rainbow(length(names(t9))))






# 타이타닉 생존/사망 비율
titanic<-read.csv('c:/Java/data/titanic.csv', sep=',', header = T, stringsAsFactors = F)
titanic
survive <- table(titanic$Survived)
pct <- round(prop.table(survive) * 100)
pct

pie(pct, label=paste(pct,'%'), col=rainbow(2), clockwise = T)
legend('topleft',c('dead','survived'), fill=rainbow(2))

# 승선권 유형별 비율을 파이그래프로 작성
pclass <- table(titanic$Pclass)
pct <- round(prop.table(pclass)*100)
pct

pie(pct, label=paste(pct,'%'), col=rainbow(3), clockwise = T)
legend('topleft', c('1st','2nd','3rd'), fill=rainbow(3))

# 승선위치별 비율을 파이그래프로 작성
embark <- titanic$Embarked[titanic$Embarked != '']
loc <- table(embark)
pct <- round(prop.table(loc)*100)
pct

pie(pct, label=paste(pct,'%'), col=rainbow(4), clockwise = T)
legend('topleft', c('courgh','queens','southamton'), fill=rainbow(4))


# 성별 생존 비율

# 남/여 생존/사망이 함께 그려서 가독성이 떨어짐
survive <- table(titanic$Sex, titanic$Survived)
pct <- round(prop.table(survive)*100)
pct

pie(pct, label=paste(pct,'%'), col=rainbow(4), clockwise = T)
legend('topleft',
       c('여/사망','남/사망','여/생존','남/생존'),
       fill=rainbow(4))



# 남/여 따로 작성
survive
pctf <- round(prop.table(survive[1,])*100)
pctm <- round(prop.table(survive[2,])*100)
pctf
pctm

pie(pctf, label=paste(pctf,'%'),col=rainbow(2), clockwise=T, main='여자 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

pie(pctm, label=paste(pctm,'%'),col=rainbow(2), clockwise=T, main='남자 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

# 승선권 유형별
pclass <- table(titanic$Pclass, titanic$Survived)
pclass
pct1 <- round(prop.table(pclass[1,])*100)
pct2 <- round(prop.table(pclass[2,])*100)
pct3 <- round(prop.table(pclass[3,])*100)

pie(pct1, label=paste(pct1,'%'),col=rainbow(2), clockwise=T, main='1등석 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

pie(pct2, label=paste(pct2,'%'),col=rainbow(2), clockwise=T, main='2등석 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

pie(pct3, label=paste(pct3,'%'),col=rainbow(2), clockwise=T, main='3등석 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

# * 승성권별 남여 생존비율도 구해보기

# 승원위치별
embark <- titanic$Embarked[titanic$Embarked != '']
survive <- titanic$Survived[titanic$Embarked != '']
loc <-table(embark, survive)

pctc <- round(prop.table(loc[1,])*100)
pctq <- round(prop.table(loc[2,])*100)
pcts <- round(prop.table(loc[3,])*100)

pie(pctc, label = paste(pctc,'%'), col=rainbow(2), clockwise = T, main='courugh 탑승자 사망/ 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

pie(pctq, label = paste(pctc,'%'), col=rainbow(2), clockwise = T, main='qeens 탑승자 사망/ 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))

pie(pcts, label = paste(pctc,'%'), col=rainbow(2), clockwise = T, main='southamton 탑승자 사망/ 생존 비율')
legend('topleft',c('사망','생존'),fill=rainbow(2))


