# 연속확률분포

정수로 셀수 없기에 구하고자 하는 사건을 구간으로 산출하고
구간의 면적으로 확률을 구함

사건을 그래프로 산출 -> 그래프 면적으로 확률 계산

구간의 총면적은 1

확률값을 구하려면 총구간과 구하는 구간을 알아야함
확률분포에 따라 총면적 모양이 다름


# 중요 연속확률분포
# 균등분포, 정규분포, 지수분포

# 균등분포
# 확률변수의 값은 최소/최대값으로 결정됨
# 모든 확률변수에 대해 동일한 값 가짐

ex) 주유소에 팔리는  휘발유양 2000~5000리터 균등분포
 => 확률변수는 하루중 판매되는 휘발유 x리터를 의미

쇼핑몰 회원가입 절타 5~10분
확률변수는 1명의 고객이 회원가입시 걸리는 x분

ex) 0/2
dunif(0.5,min=0,max=2)  # y값을 구함
?dunif

vals <- dunif(-1:3,0,2)
plot(y=vals, x=c(-1:3), type = 'l')


# 0.5이하 확률
punif(0.5,min = 0, max = 2, lower.tail = T)

# 0.5이상 확률
punif(0.5,min = 0, max = 2, lower.tail = F)


ex) 제주도 여행 비행기 60~70분걸린다고 할 때,
비행기가 64~67분사이에 도착할 확률
단, 균등분포를 따른다.

punif(67,min = 60, max = 70, lower.tail = T) - punif(64,min = 60, max = 70, lower.tail = T) 

서울에서 춘천까지 고속버스를 타는데 70~80qns 74분안에 갈 확률

punif(74,min = 70, max = 80, lower.tail = T)

punif(74,min = 70, max = 80)  # 기본값: 이하 T

punif(74,70,80)


시멘트 회사의 주간 시멘트 생산량은 100~170
155톤이상 생산할 확률
punif(155,100,170,lower.tail = F)

vals <- dunif(90:180,100,170)
plot(y=vals,x=c(90:180), type='l')


통학버스 대기시간 0~30 => 25분이상 기다릴 확률
punif(5,0,30)

10~20분 기다릴 확률
punif(20,0,30) - punif(10,0,30)

vals <- dunif(-10:40,0,30)
plot(y=vals, x=c(-10:40), type='l')

a<-(0:5)
b<-dunif(a,0,30)
polygon(c(0,a,5),c(0,b,0),col='red')




a<- (0:0.5)
b <- dunif(a,0,2)
polygon(c(0,a,0.5),c(0,b,0), 
        col='green')



# 정규분포
x <- seq(5,35)
a<-dnorm(x,mean=20,sd=3.1)
b<-dnorm(x,mean=20,sd=4.1)
c<-dnorm(x,mean=20,sd=5)

plot(a, type = 'l', col='red')
lines(b, type = 'l', col='blue')
lines(c, type = 'l', col='green')

# 상품3개 상품무게 정규분포
평균 283/301/321
표편 : 1.6

x <- seq(250,350)
a<-dnorm(x,mean=283,sd=1.6)
b<-dnorm(x,mean=301,sd=1.6)
c<-dnorm(x,mean=321,sd=1.6)

plot(a, type = 'l', col='red')
lines(b, type = 'l', col='blue')
lines(c, type = 'l', col='green')

#  표준 정규분포
x <- seq(5,35)
a<-dnorm(x,mean=20,sd=3.1)
b<-dnorm(x,mean=20,sd=4.1)
c<-dnorm(x,mean=20,sd=5)

plot(a, type = 'l', col='red')
lines(b, type = 'l', col='blue')
lines(c, type = 'l', col='green')

# 정규분포에서 1이하의 확률
pnorm(1,mean=0,sd=1)

a <- seq(-5,5, length=1000)
b <- dnorm(a, mean=0, sd=1)
plot(a,b,type='l',col='red')

c <- seq(-5,1, length=1000)
d <- dnorm(c, mean=0, sd=1)
polygon(c(-5,c,1),c(0,d,0),col='red')

# 평균키 173 sd=5
z = (x-mean)/sd

pnorm(183,mean=173,sd=5,lower.tail = F)

a<-(153:193)
b <- dnorm(a,mean=173,sd=5)
plot(a,b, type = 'l',col='red')

c<-(185:193)
d <- dnorm(c,mean=173,sd=5)
polygon(c(185,c,193),c(0,d,0),col='red')




ex) 택시기사 수입 평균 1000 표편 100 정규분포
주당수입 1100에 해당하는 z값 1
주당수입 900에 해당하는 z값 -1
840~1200 확률
pnorm(1200,1000,100)-pnorm(840,1000,100)

1000~1100 확률
pnorm(1100,1000,100)-pnorm(1000,1000,100)




ex) 전구 800 40
750일확률
0

750이상일 확률
pnorm(750,800,40, lower.tail = F)




ex) 70 8
80~90학생비율
pnorm(90,70,8) - pnorm(80,70,8)




정규분포 68% : 1
         90% : 1.645
         95% : 1.96
         99% : 2.58

         
         
         

ex) 배터리 19  1.2 체비쉐프 공식에 따른 68% 95%

32:100 = 1:k^2
68% : 대략 1.77

1-1/(1.77^2)







5:100 = 1:k^2
95% : 대략 : 4.47

1-1/(4.47^2)


# 자동차 타이어의 평균 수명이 67000km 2050  
=> 4%미만 교환 보증km 얼마를 설정해야 하나
단, 정규분포 0.4600 => 1.75
67000 - 1.75*2050

pnorm(0.68,0,1)






# 지수분포 : 람다e^(-람다x)
누적 분포함수 : F(x) = 1-e^-람다x
but 계산할 때는 F(x) = 1-e^(x/람다) 로 계산.... 왜지...


반면, 시간이 지날수록 작아지는 경우 지수분포 사용 
ex) 백화점 안내데스크에 고객 문의 요청 시간 간격
제품 수명 

# 이산확률분포의 포아송분포와 밀접한 관련이 있음
ex) 어떤 레스토랑의 저녁시간에는 시간당 6명이 방문한다고 가정할 때
시간당 5명 방문할 확률, 7명이 방문할 확률 => 포아송
반면, 다음고객이 10분이내에 방문할 확률을 구하는 것은 지수분포임


따라서, 포아송분포는 단위 시간/공간 안에서 발생하는 
어떤 사건의 횟수에 대한 확률을 계산

반면, 지수분포는 어떤 사건이 처음으로 발생하기까지 걸린 시간을 기준으로,
이 시간내 발생하는 사건에 대한 확률을 계산
따라서, 이 시간 전 사전발생확률은 0이고, 
이 시간 이후 사건의 평균발생빈도는 1/람다 값이됨


plot(dexp(0:5,1), type = 'l',col='red')
lines(dexp(0:5,0.5), type = 'l',col='blue')
lines(dexp(0:5,1.5), type = 'l',col='green')




exp(?,rate=?)

ex) 전자제품회사에서 생산하는 스마트폰 부품은 
평균수명이 5년이고, 지수분포를 따른다고 할 때
이 부품이 고장나지 않고 6년이상 수명이 지속될 확률

pexp(6,rate=1/5, lower.tail=F)


a<-(0:15)
b <- dexp(a,1/5)
plot(a,b, type = 'l',col='red')

c<-(6:15)
d <- dexp(c,1/5)
polygon(c(6,c,15),c(0,d,0),col='red')




ex) 약국 평균 20초당 1건의 처방전 다음 처방전이 5초이내에 도착할 확률
또한 다음 처방전이 40초 이후에 도착할 확률

?pexp
pexp(5,rate=1/20)
pexp(40,rate=1/20, lower.tail = F)


a<-(0:60)
b <- dexp(a,1/20)
plot(a,b, type = 'l',col='red')

c<-(0:5)
d <- dexp(c,1/20)
polygon(c(0,c,5),c(0,d,0),col='red')


a<-(0:60)
b <- dexp(a,1/20)
plot(a,b, type = 'l',col='red')

c<-(40:60)
d <- dexp(c,1/20)
polygon(c(40,c,60),c(0,d,0),col='red')



ex) A회사에서 판매중인휴대폰의 평균수명은 3년 보증기간 1년, 
1년이내 고장나서 보상받을 확률

pexp(1,rate=1/3)



ex) 한 연인이 데이트를 하기 위해 만날때마다 
남자가 항상 지각한다고 가정하자 평균 8분 지수분포
4~11분 지각할 확률

pexp(11,rate=1/8) - pexp(4,rate=1/8)


ex) 어떠 ㄴ회사이 전원공급장치의 ㅜ명에 대해
보증기간을 정하려 한다. 품질 테스트결과
이 장치의 평균수명 4000시간이라 할 때
판매된 제품의 5%만 교체해주려고 한다.
보증기간을 얼마로 정해야 할까?

  
  
pexp(1,rate = 1/4000)


a<-(0:8000)
b <- dexp(a,1/4000)
plot(a,b, type = 'l',col='red')

c<-(0:60)
d <- dexp(c,1/20)
polygon(c(40,c,60),c(0,d,0),col='red')

팬매제품 5%에 대해 교체

0.05=1-e^-1/4000*x
log(0.95)=-1/4000*x
x = log(0.95)*4000

log(0.95)

0.0513=1/4000*x

0.0513*4000 =205

pexp(205,rate = 1/4000)


ex) 서브웨이 샌드위치 주문 후 기다리는 평균 대기시간이 60초인 지수분포를 따를 때
30초 이하로 기다릴 확률
120초 이상 기다릴 확률
고객의 50% 고객이 기다려야할 대기시간은?
pexp(30,1/60)
pexp(120,1/60, lower.tail = F)

log(1/2)*-60

