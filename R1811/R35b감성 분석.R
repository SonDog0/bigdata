# 감성분석 2 - 한글데이터 이용
# 군산대학교 한국어 감성 사전을 이용
# dilab.kunsan.ac.kr/knusl.html

library(stringr)
library(dplyr)
library(rvest)

setwd('c:/Java/data')
pos <- readLines('positive_ko.txt')
neg <- readLines('negative_ko.txt')

# 분석데이터 초기화
docs <- readLines('steve_ko.txt',
                  encoding = 'UTF-8')

# 전처리 작업
docs <- gsub('[[:punct:]]','', docs)
docs <- gsub('[[:cntrl:]]','', docs)
docs <- gsub('\\d+','', docs)

# 문장들을 공백단위로 잘른 후 벡터 변환
words <- str_split(docs, '\\s+')
words <- unlist(words)

# 감성분석 
pos.matches <- match(words, pos)
neg.matches <- match(words, neg)

pos.matches <- !is.na(pos.matches)
neg.matches <- !is.na(neg.matches)

# 점수계산 = 긍정일치수 - 부정일치수
score <- sum(pos.matches) - sum(neg.matches)
score





neg <- c(neg,'충격적','과대평가')



ex) 다음 문장이 긍정의 의미를 담고 있는지 분석하라
a<-'10점 내 생애 최고의 영화 심금을 울리네요'
b<-'도대체 뭐가 충격적이라는 거지..
진짜 과대평가된 영화네요'
c<-'와.. 드디어 AMD가 자기네 그래픽 드라이버에
문제 있다는걸 인정했네요..'

c <- str_split(c, '\\s+')
c <- unlist(c)


pos.matches <- match(c, pos)
neg.matches <- match(c, neg)

pos.matches <- !is.na(pos.matches)
neg.matches <- !is.na(neg.matches)

score <- sum(pos.matches) - sum(neg.matches)
score
