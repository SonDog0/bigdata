# 인구 주택 총 조사표를 참조
# 각 변수들을 벡터 선언
id <- c(1:9)
sex <- c('여자','여자','여자','여자','남자','여자','여자','여자','남자')
age <- c(68,29,7,3,26,52,62,10,58)
rs <- c('가구주의 배우자','가구주의 배우자','자녀','자녀','자녀','가구주의 배우자','가구주의 배우자','자녀','가구주')
ach <- c('초등학교','초등학교','초등학교','안 받았음','중학교','초등학교','고등학교','초등학교','중학교')
bnum <- c(3,0,NA,NA,NA,2,1,NA,NA)

ex1 <- data.frame(ID=id,성별=sex,나이=age,가구주와의관계=rs,학력=ach,자녀수=bnum,stringsAsFactors = F)
ex1


# 안됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#applewood auto group표를 참조
# 각 변수들을 벡터 선언
Age <- c(21,23:26,rep(27:29,each=2),rep(30:30,each=3))
Profit <- c('$1,387','$1,754','$1,817','$1,040','$1,273',
            '$1,529','$3,082','$1,951','$2,692','$1,206',
            '$1,342','$443','$754','$1,621')
Location <- c('Tionesta','Sheffield','Sheffield','Sheffield','Kane',
              'Sheffield','Kane','Kane','Tionesta','Sheffield',
              'Kane','Kane','Olean','Sheffield')
Vehicle_Type <- c('Sedan','SUV','hybrid','Compact','Sedan',
                  'Sedan','Truck','SUV','Compact','Sedan',
                  'Sedan','Sedan','Sedan','Truck')
Previous <- c(0,1,1,0,1,1,0,1,0,0,2,3,2,1)

ex2 <- data.frame(Age,Profit,Location,Vehicle_Type,Previous,stringsAsFactors = F)
ex2

#환자 투약 효과에 대한 표
# 각 변수들을 벡터 선언 

PatlentID <- c(1:4)
AdDate <- c('10/15/2014','11/01/2014','10/21/2014','10/28/2014')
Age <- c(25,34,28,52)
Diabetes <- c('Type1','Type2','Type1','Type1')
Status <- c('Poor', 'Improved','Exeelent','Poor')

ex3 <- data.frame(PatlentID,AdDate,Age,Diabetes,Status,stringsAsFactors = F)
ex3

ex3[c(2,4)]
ex3[c('Age','status')]

ex3[c(2)]
ex3[c('Age')]
ex3$Age


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

leadership <- data.frame(Manager,Date,Country,Gender,Age,q1,q2,q3,q4,q5,stringsAsFactors = F)
ex4
str(ex4)

#applewood auto group csv 이용 
ex5 <- read.table('applewood.txt',header = T, sep=' ',stringsAsFactors = F)
ex5

# 판매이익을 문자형으로 변환 
ex5 <- read.table('applewood.txt',header = T, sep=' ')
ex5$Profit <- as.character(ex5$Profit)
str(ex5)

# 기술통계량 확인
summary(ex5)

# 매니저리더쉽 설문조사
# leadership
# 설문 문항에 대해 sumq, meanq변수 추가
newOne =data.frame(sumq=q1+q2+q3+q4+q5, meanq=(q1+q2+q3+q4+q5)/5)
leadership <- cbind(leadership,newOne)
leadership

#나이를 대상으로 새로운 범주형 변수 생성
newOne
# 나이가 30미만 : 초년
# 나이가 30이상 75미만 : 중년
# 나이가 75이상 : 노년 


# psych 패키지의 galton 데이터셋을 조사하시오
install.packages('psych')
library('psych')
help(psych) # 유전학, 의학, 통계학을 기초로 우성 유전자 증대 목적
data(galton)     # 부모/자식 키 조사, 관계조사 
str(galton)
summary(galton)

