# 감성사전 만들기
# 네이버 영화리뷰파일(ratings.txt)을 기초로 하여
# 긍정/부정 사전 생성


Sys.setenv(JAVA_HOME='c:/Java/jdk1.8.0_181')
library(rJava)
library(KoNLP)
library(stringr)
library(dplyr)
library(rvest)

useNIADic()

# 어휘분석
# 명사추출x, 기본품사 추출x, 상세품사 추출o
# 명사, 형용사, 동사등을 추출해서 감성 사전 구축
# simplePos09 : N(명사), P(동사/형용사)
# simplePos22 : NC(명사), PV(동사), PA(형용사)


str1<-'10점 내 생애 최고의 영화 심금을 울리네요'
str2<-'도대체 뭐가 충격적이라는 거지..
진짜 과대평가된 영화네요'
str3<-'와.. 드디어 AMD가 자기네 그래픽 드라이버에
문제 있다는걸 인정했네요..'

word1a <- extractNoun(str1)  # 명사
word1b <- SimplePos09(str1)  # 기본품사
word1c <- SimplePos22(str1)  # 상세품사

word1a
word1b
word1c

word2a <- extractNoun(str2)  # 명사
word2b <- SimplePos09(str2)  # 기본품사
word2c <- SimplePos22(str2)  # 상세품사

word3a <- extractNoun(str3)  # 명사
word3b <- SimplePos09(str3)  # 기본품사
word3c <- SimplePos22(str3)  # 상세품사

# 명사(NC) 추출
doc <- as.character(str1)        # 문자형 변환
doc <- paste(SimplePos22(doc))   # 상세품사로 추출
doc <- str_match(doc, '[가-힣]+/NC')
doc
doc.nc <- doc[!is.na(doc)]
doc.nc


# 추출된 데이터 파일로 저장
setwd('c:/Java/data')
doc.nc <- as.data.frame(doc.nc)
write.csv(doc.nc,'doc.nc.csv',fileEncoding='UTF-8')


# 형용사(PA)
doc1 <- as.character(str1)     
doc1 <- paste(SimplePos22(doc1))
doc1 <- str_match(doc1, '([가-힣]+)/(PA)')

doc.pa <- doc1[!is.na(doc1)]
doc.pa

doc.pa <- as.data.frame(doc.pa)
write.csv(doc.pa,'doc.pa.csv',fileEncoding='UTF-8')

# 동사(PV)
doc2 <- as.character(str1)     
doc2
doc2 <- paste(SimplePos22(doc2))
doc2
doc2 <- str_match(doc2, '[가-힣]+/PV')
doc2
doc.pv <- doc2[!is.na(doc2)]
doc.pv

doc.pv <- as.data.frame(doc.pv)
write.csv(doc.pv,'doc.pv.csv',fileEncoding='UTF-8', row.names = F)








# steve jobs 연설문에서 명사, 형용사, 동사를 추출해 파일 생성
sv <- readLines('steve_ko.txt',encoding='UTF-8')

sv <- as.character(sv)
sv <- paste(SimplePos22(sv))
doc.nc <- str_match(sv, '[가-힣]+/NC')
doc.nc <- doc.nc[!is.na(doc.nc)]
doc.nc

steve.nc <- as.data.frame(doc.nc)
write.csv(steve.nc,'steve.nc.csv',
          fileEncoding = 'UTF-8',
          row.names = F)
