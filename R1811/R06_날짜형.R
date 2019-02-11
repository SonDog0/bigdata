# 날짜형 다루기 
Manager <-c(1:5)
date <-c('10/24/14','10/28/14','10/01/14','10/12/14','05/01/14')
Country <- c('US','US','UK','UK','UK')
Gender <-c('M','F','F','M','F')
Age <-c(32,45,25,39,99)
q1<-c(5,3,3,3,2)
q2<-c(4,5,5,3,2)
q3<-c(5,2,5,4,1)
q4<-c(5,5,5,NA,2)
q5<-c(5,5,2,NA,1)

leadership <- data.frame(Manager,date,Country,Gender,Age,q1,q2,q3,q4,q5)
str(leadership)

# 날짜가 factor로 작성됨 
# 날짜가 문자형으로 작성됨 (,stringsAsFactors = F)

# 문자형식을 날짜로 변환 - as.Date()
# 기본형식은 시스템의 locale에 따름(yyyy-mm-dd)
dates <- c('2018-01-01','2018-12-31')
class(dates)
newdates <- as.Date(dates)
class(newdates)

# 만일, 다른형식의 날짜를 사용한다면
# 적절한 형식지정자를 사용
strDates <- c('01/01/2018','12/31/2018')
newDates <- as.Date(strDates)
newDates # 올바른 날짜형식이 생성 x

newDates <- as.Date(strDates,'%m/%d/%Y')
newDates # 시스템 local 에 맞게 출력

# leadership의 date 변수를 적절한 날짜 형식으로 변환
# fmt <- '%m%d%Y'   # %Y : 4자리 년도
# fmt <- '%m%d%Y'   # %y : 2자리 년도

fmt <- '%m/%d/%y'
leadership <- within(leadership, { date <- as.Date(date, fmt)})
str(leadership)

# 오늘 날짜/시간 출력
Sys.Date()
Sys.time()

#날짜 출력 형식
today <- Sys.Date()
format(today, format='%B %d %Y')
format(today, format='%A')
format(today, format='%d %a %m %b %y')
?as.Date

#날짜 계산
startdate <- as.Date('2015-04-24')
enddate <- as.Date('2018-10-25')
enddate - startdate

# 생년월일을 기준으로 지금까지 몇일이 지났는지 계산
# 그녀와 사귄지 몇일이 지났는지 계산
# 그녀와 결혼한지 몇일이 지났는지 계산
# 헤어진지 몇일이 지났는지
birthday <- as.Date('1991-05-16')
enddate <- as.Date('2018-10-25')
today - startdate +1

# 태어난 날의 요일
format(birthday, format='%A')

# 고급 날짜 계산 : difftime
difftime(today, birthday, units='weeks' ) #주로 계산
difftime(today, birthday, units='hours' ) #시간으로 계산
difftime(today, birthday, units='days' ) #일로 계산

