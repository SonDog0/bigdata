exam <- read.table(file.choose(), header=T, sep=',',stringsAsFactors = F)
str(exam)
summary(exam)
# 2015년 중구지역의 월별 교통사고 발생건수
# exam2 <- exam[c(13:24),]
exam2 <- exam[exam$자치구명=='중구',]
exam2

# 산점도 : 점
plot(exam2$월,exam2$발생건수,type='p',col='red',ylim=c(0,150),xlim=c(0,13),
     xlab='월',ylab='발생건수',main='2015 중구 교통사고 발생건수')
grid()
text(exam2$발생건수, cex=0.5, lab=exam2$발생건수, adj=c(1.5,0))
# text(exam2$발생건수, cex=0.7, lab=exam2$월, adj=c(2,-1))

# 산점도 : 선
plot(exam2$월,exam2$발생건수,type='l',col='red',ylim=c(0,150),
     xlab='월',ylab='발생건수',main='2015 중구 교통사고 발생건수')
grid()
text(exam2$발생건수, cex=0.5, lab=exam2$발생건수, adj=c(1.5,0))


# 산점도 : 둘다
plot(exam2$월,exam2$발생건수,type='b',col='red',ylim=c(0,150),
     xlab='월',ylab='발생건수',main='2015 중구 교통사고 발생건수')
grid()
text(exam2$발생건수, cex=0.5, lab=exam2$발생건수, adj=c(1.5,0))


# 2015년 관악구지역의 월별교통사고 발생건수
# exam3 <- exam[c(241:252),]
exam3 <- exam[exam$자치구명=='관악구',]
exam3

# 산점도 : 점
plot(exam3$월,exam3$발생건수,type='p',xlab='월',ylab='발생건수',main='관악구 월별 교통사고')
grid()
text(exam3$발생건수, cex=0.5, lab=exam3$발생건수, adj=c(1.5,0))
# 산점도 : 선
plot(exam3$월,exam3$발생건수,type='l',xlab='월',ylab='발생건수',main='관악구 월별 교통사고')
grid()
text(exam3$발생건수, cex=0.5, lab=exam3$발생건수, adj=c(1.5,0))

# 산점도 : 둘다
plot(exam3$월,exam3$발생건수,type='b',xlab='월',ylab='발생건수',main='관악구 월별 교통사고')
grid()
text(exam3$발생건수, cex=0.5, lab=exam3$발생건수, adj=c(1.5,0))


# 중구 관악구 함께 뽑기

plot(exam3$월,exam3$발생건수,type='b',pch=1,
     xlab='월',ylab='발생건수',col='blue',
     main='2015 중구,관악구 월별 교통사고')

lines(exam2$월,exam2$발생건수,type='b',pch=2,
      xlab='월',ylab='발생건수',col='red')

legend('topleft',c('중구','관악'), pch=c(2,1), col=c(2,1))


# 자동차 연비 데이터셋 mtcars
str(mtcars)

# 병아리 사육 데이터셋 ChickWeight
str(ChickWeight)
