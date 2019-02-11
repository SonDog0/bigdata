# 인구 주택 총 조사표를 참조
# 각 변수들을 벡터 선언
id <- c(1:9)
sex <- c('여자','여자','여자','여자','남자','여자','여자','여자','남자')
age <- c(68,29,7,3,26,52,62,10,58)
rs <- c('가구주의 배우자','가구주의 배우자','자녀','자녀','자녀','가구주의 배우자','가구주의 배우자','자녀','가구주')
ach <- c('초등학교','초등학교','초등학교','안 받았음','중학교','초등학교','고등학교','초등학교','중학교')
bnum <- c(3,0,NA,NA,NA,2,1,NA,NA)

#applewood auto group표를 참조
# 각 변수들을 벡터 선언
Age <- c(21,23:26,rep(27:29,each=2),rep(30:30,each=3))
Profit <- c('$1,387','$1,754','$1,817','$1,040','$1,273',
           '$1,529','$3,082','$1,951','$2,692','$1,206',
           '$1,342','$443','$754','$1,621')
Location <- c('Tionesta','Sheffield','Sheffield','Sheffield','Kane',
              'Sheffield','Kane','Kane','Tionesta','Sheffield',
              'Kane','Kane','Olean','Sheffield')
Vehicle-Type <- c('Sedan','SUV','hybrid','Compact','Sedan',
                  'Sedan','Truck','SUV','Compact','Sedan',
                  'Sedan','Sedan','Sedan','Truck')
Previous <- c(0,1,1,0,1,1,0,1,0,0,2,3,2,1)

#나이에 따른 신생아 몸무게 추이
# 각 변수들을 벡터로 선언 (이변량 분석)
age <- c(01,03,05,02,11,09,03,09,12,03)
weight <- c(4.4,5.3,7.2,5.2,8.5,7.3,6.0,10.4,10.2,6.1)

plot(age,weight)

mean(age)
mean(weight)
sd(weight)                    # 표편
cor(age,weight)               # 상관계수 그래프에서는 x,y

abline(lm(weight~age))        # 상관계수에 따른 선형회귀직선 (y~x)

#환자 투약 효과에 대한 표
# 각 변수들을 벡터 선언 

PatlentID <-C(1:4)
AdmDate <-c('10/15/2014','11/01/2014','10/21/2014','10/28/2014')
Age <- c(25,34,28,52)
Diabetes <- c(Type1,Type2,Type1,Type1)
Status <- c('Poor', 'Improved','Exeelent','Poor')
# 매니저에 대해 리더쉽 설문조사 결과 표
# 각 변수들을 벡터 선언

Manager <-c(1:5)
Date <-c('10/24/14','10/28/14','10/01/14','10/12/14','05/01/14')
Country <- c('US','US','UK','UK','UK')
Gender <-c('M','F','F','M','F')
Age <-c(32,45,25,39,99)
q1<-c(5,3,3,3,2)
q2<-c(4,5,5,3,2)
q3<-c(5,2,5,4,1)
q4<-c(5,5,5,NA,2)
q5<-c(5,5,2,NA,1)