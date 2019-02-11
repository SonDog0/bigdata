# 데이터 불러오기
# 키보드로부터 입력받기
x <- 3   # 입력값이 고정
y <- 5
z <- x + y

x <-scan() # 입력종료시 엔터 2번 입력
y <-scan()
z <- x + y
z

name <- scan(what=character())  # 문자입력 받기
name

# 데이터 프레임 생성시 편집기 이용
df <- data.frame()
df <- edit(df)

df

# 기존에 만든 DF를 편집기로 수정
edit(leadership)

# 외부 파일 불러오기 #2
summermedal <- read.table(file.choose(), header=T, sep=',')
head(summermedal)

# 엑셀파일 다루기
install.packages('xlsx')
install.packages('rJava')
Sys.setenv(JAVA_HOME='C:/java/jdk1.8.0_181')

library(xlsx)
library(rJava)

titanic <- read.xlsx(file.choose(),sheetIndex = 1)
head(titanic)
nrow(titanic)

# 인터넷에서 바로 데이터 가져오기
# 세계 GDP 순위 데이터 가져오기
# data.worldbank.org -> 검색창 : gdp ranking
# http://databank.worldbank.org/data/download/GDP.csv
# http://databank.worldbank.org/data/download/GDP.xls

url <-'http://databank.worldbank.org/data/download/GDP.csv'
gdp_rank <- read.csv(url)
head(gdp_rank, 10)

# 전처리
# 1~4행 지우고 1~3,6,7 열 지우기
# 상위 25개국 선별 -> GDP_rank_25
# 데이터프레임을 구성하는 2열에 이름 지정
# Nation, GDP

# 행제거
url <-'http://databank.worldbank.org/data/download/GDP.csv'
gdp_rank <- read.csv(url) 
gdp_rank

gdp_rank <- gdp_rank[-c(1:4),]
head(gdp_rank)
gdp_rank<- gdp_rank[,c(4,5)]
head(gdp_rank)

# 상위 25개국 추출
gdp_rank_25 <- head(gdp_rank, 25)
gdp_rank_25

# 열이름 변경
names(gdp_rank_25) <- c('Nation','GDP')
gdp_rank_25
# colnames(gdp_rank_25) <- c('Nation','GDP') # 참고용

# 행번호 변경
# rownames(gdp_rank_25) <- NULL
rownames(gdp_rank_25) <- 1:nrow(gdp_rank_25)
gdp_rank_25

# 2010 ~ 2015 까지 미국의 주별 1인당 소득자료
# ssti.org -> search : Per Capital Personal Income
# https://ssti.org/blog/useful-stats-capita-personal-income-state-2010-2015
url <-'https://ssti.org/blog/useful-stats-capita-personal-income-state-2010-2015'

install.packages('XML')     # html 소스처리 패키지
install.packages('httr')    # http 프로토콜 처리 패키지
library(XML)
library(httr)

rawdata <-GET(url)  # raw data(16진수)로 넘어옴 
head(rawdata$content)   # 본문만 출력 
head(rawToChar(rawdata$content))   # 16진수를 문자로 변환

html <- readHTMLTable(head(rawToChar(rawdata$content)), stringAsFactors=F)

# html 소스중 table 태그 부분만 추출
str(html)

incomes <- as.data.frame(html)  # DF로 변환
head(incomes)

# 필드명 변경(state 2010 2011 2012 2013 2014 2015)
names(incomes) <- c('state','2010','2011','2012','2013','2014','2015')
head(incomes)
tail(incomes)

str(incomes)


# 결과물 화면 저장하기
# cat() - 문자열과 변수를 결합
x <- 10
y <- 20
z <- x * y
cat('x * y =',z,'입니다')

# 파일에 데이터 저장
# sink() 함수 사용
setwd('c:/Java/data')

library(RSADBE)
data(Severity_Counts)
SeverityCounts <- Severity_Counts
SeverityCounts


library(RSADBE)
data(Severity_Counts)   # Severity_Count 데이터셋
sink('SeverityCounts.txt')  # 저장할 파일 지정
SeverityCounts <- Severity_Counts   # 데이터셋을 변수에 지정
SeverityCounts   # 화면에 출력되지 않고 파일에 출력  
sink()           # 저장할 파일 닫기


# psych 패키지의 galton 데이터셋을
# galton.txt로 저장
library(psych)
data(galton)
sink('galton.txt')
gal <- galton
gal
sink()

# titanic, gdp_rank_25, incomes DF를 각각 저장
sink('titanic.txt')
titanic
sink()

sink('gdp_rank_25.txt')
gdp_rank_25
sink()

sink('incomes.txt')
incomes
sink()


# 파일에 데이터 저장
# write.table() 함수 사용
setwd('c:/Java/data')
write.table(SeverityCounts, 'severity.txt')
write.table(SeverityCounts, 'severity1.txt', row.names=F)
write.table(SeverityCounts, 'severity2.txt', quote=F)  # 인용부호 F

# 파일에 데이터 저장
# write.xlsx() 함수 사용
library(xlsx)
write.xlsx(SeverityCounts, 'severity.xlsx')

# 파일에 데이터 저장
# write.csv() 함수 사용
write.csv(SeverityCounts, 'severity.csv',row.names=F, quote=F)


# titanic, gdp_rank_25, incomes DF를 각각 저장
# txt, xlsx, csv
write.table(titanic,'titanic2.txt')
write.xlsx(titanic,'titanic2.xlsx')
write.csv(titanic,'titanic2.csv')

write.table(gdp_rank_25,'gdp_rank_25_2.txt')
write.xlsx(gdp_rank_25,'gdp_rank_25_2.xlsx')
write.csv(gdp_rank_25,'gdp_rank_25_2.csv')

write.table(incomes,'incomes2.txt')
write.xlsx(incomes,'incomes2.xlsx')
write.csv(incomes,'incomes2.csv')

