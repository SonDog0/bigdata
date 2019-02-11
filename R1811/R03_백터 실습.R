# 인구주택총조사 표를 참조 데이터 프레임
ID = c(1:9)
gender = c('여자','여자','여자','여자', 
           '남자', '여자','여자','여자','남자')

age = c(68,29,7,3,26,52,62,10,58)
rel = c('가구주의 배우자', '가구주의 배우자', '자녀','자녀',
        '자녀', '가구주의 배우자', '가구주의 배우자', '자녀','가구주')
sch = c('초등학교', '초등학교', '초등학교', NA, '중학교', '초등학교',
        '고등학교', '초등학교', '중학교')
baby = c(3,0, NA, NA, NA, 2, 1, NA, NA)
pop = data.frame(id= ID, gender, age, rel, sch, baby)
pop

# applewood auto group 표를 참조해 데이터 프레임

apple.Age = c(21, 23:26, 27, 27 , 28, 28 , 29 ,29, rep(30:30, 3) )
apple.Profit = c(1387, 1754, 1817, 1040, 1273, 1529, 3082,
                 1951,2692,1206,1342,443,754,1621)

apple.Location= c('Tionesta', 'Sheffield', 'Sheffield', 'Sheffield',
                  'Kane', 'Sheffield', 'Kane', 'Kane', 'Tionesta',
                  'Sheffield', 'Kane', 'Kane', 'Olean', 'Sheffield')
apple.Vehicle_Type = c('Sedan','SUV', 'Hybird', 'Compact', 'Sedan',
                       'Sedan','Truck', 'SUV', 'Compact', 'Sedan',
                       'Sedan', 'Sedan', 'Sedan', 'Truck')
apple.Previous = c(0,1,1,0,1,1,0,1,0,0,2,3,2,1)

applewood= data.frame(age =apple.Age, profit =apple.Profit, location = apple.Location, 
                      vehicle= apple.Vehicle_Type, previous = apple.Previous)

applewood
str(applewood)
nrow(applewood)
ncol(applewood)
applewood[,1]
applewood[,c(1,3,5)]

# 환자 투약 효과에 대한 표 참조 데이터 프레임

patientID = c(1:4)
admdate = c(as.Date('2014-10-15'), as.Date('2014-11-01'), 
            as.Date('2014-10-21'),as.Date('2014-10-28'))

age = c(25,34,28,52)
diabetes = c('Type1', 'Type2', 'Type1', 'Type1')
Status = c('Poor', 'Improved', 'Excellent', 'Poor')

med = data.frame(patientID, admdate, age, diabetes,Status)

med[,c(3,5)]
med[,c('age','Status')]

med$age
med[c(3)]
med[c('age')]

# 매니저에 대해 리더쉽 설문조사 결과 표 참조하여 데이터 프레임
manager = c(1:5)
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


#leadership = data.frame(manager, date, country, gender, age, q1, q2, q3, q4, q5)

leadership
str(leadership)

# 설문문항에 대해 sumq, meanq 변수 추가
# 새로운 변수를 추가하려면 'DF이름$새로운 변수명'
leadership = data.frame(manager, date, country, gender, age, q1, q2, q3, q4, q5)


leadership$sumq <- q1 + q2 + q3 +q4 + q5
leadership
  

leadership$meanq <- leadership$sumq/5
leadership

attach(leadership)
  leadership$sumq <- q1+q2+q3+q4+q5         # attach에서는 변수가 있어야
  leadership&meanq <- leadership$sumq / 5   # 이게 돌아감
detach(leadership)

# within 문으로 변수명을 줄여보자
leadership <- within(leadership, {
  sumq <- q1+q2+q3+q4+q5
  meanq <- sumq / 5
})

leadership  


# 나이를 대상으로 새로운 범주형ageGroup 변수 생성
# 나이가 30이하 :초년
# 나이가 30이상~75 미만 : 중년
# 나이가 75이상 : 노년
leadership$ageGroup[leadership$age < 30] <- '초년'
leadership$ageGroup[leadership$age >= 75] <- '노년'
leadership$ageGroup[leadership$age >= 30 & leadership$age < 75] <- '중년'
leadership  

# whth문으로 간결하게 작성
leadership$agegorup <- c('','','','','')
leadership <- within(leadership, {
  ageGroup[age < 30] <- '초년'
  ageGroup[age >= 75] <- '노년'
  ageGroup[age >= 30 & age < 75] <- '중년'
})


# applewood auto groupd의 csv 파일을 이용해서 데이터 프레임으로 작성

getwd()

applewood = read.csv('applewood.txt', sep=' ')
applewood
str(applewood)

# applewood 중 판매이익을 문자형으로 변환
applewood$Profit = as.character(applewood$Profit)

str(applewood$Profit)

# 기술통계량 확인
summary(applewood)

# psych 패키지의 galton 데이터셋을 조사하세요

install.packages('psych')
library('psych')
help('psych')  # 유전학, 의학, 통계학을 기초로 우성 쥬전자 증대 목적

data()
Gleser
veg
data(galton)  # 부모/자식 키 조사, 관계 조사
str(galton)

summary(galton)


