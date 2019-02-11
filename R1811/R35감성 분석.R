# 감성분석

특정 대상에 대하여 소비자가 느끼는
감성(긍정,부정)과 그 이유를 분석

감성분석은 사전이 얼마나 많은 양의 
정제된 감성어를 포함하고 있는지에 따라
분석의 품질이 달라질 수 있음

감성 분석사전을 구축하기 위해서는 다양한
머신러닝 기법을 통하여 구축할 수 있으나,
정확성을 높이기 위해서는
사람이 직/간접적으로 참여하는 과정이 필요

감성 분석 사전은 보통 '극성'을 기반으로 구축됨
즉, 긍정/부정의 의미를 담고 있는 단어들을
기반으로 사전을 구축하고 이것을 이용해서
감성분석을 실시함

#영어기반 감성분석
install.packages('twitteR')
install.packages('ROAuth')

library(twitteR)
library(ROAuth)
library(plyr)
library(stringr)
library(ggplot2)

# 트위처API를 이용해서 수집한
# 애플/삼성에 대한 트윗 데이터를 불러오기
setwd('c:/Java/data')
load('apple.RData')
load('samsung.RData')

# 총 트윗수 출력
length(apple.tweets)
length(samsung.tweets)

# 트윗데이터의 자료형 파악
class(apple.tweets)
class(samsung.tweets)

# 트윗데이터 일부 확인
apple.tweets[1:5]
samsung.tweets[1:5]

# 첫번째 트윗데이터의 상세정보 확인
tweet <- apple.tweets[[1]]
tweet$getScreenName()        # 작성자
tweet$getText        # 본문(트윗)


# 모든 트윗에서 본문만 추출하는 함수 생성
# lapply
apple.text <- lapply(apple.tweets, 
                     function(t){t$getText()})
head(apple.text)


# 감성분석을 위한 감성사전을 불러옴
pos.word <- scan('positive-words.txt',
                 what='character',
                 comment.char = ';')

neg.word <- scan('negative-words.txt',
                 what='character',
                 comment.char = ';')

# 기존 감성사전에 새로운 단어를 추가
pos.word <- c(pos.word,'upgrade')
neg.word <- c(neg.word,'waiting','standby')

tail(pos.word)
tail(neg.word)

# 트윗내용을 바탕으로 감성기반 분석 후 점수 출력
score.sentiment <- 
  function(sentences, pos.word, neg.word, 
           .progress='none') {
    
    # 관련 패키지 추가 및 등록
    library(plyr)
    library(stringr)
    
    # 감성 분석후 점수 산출하는 함수 정의
    scores <- laply(sentences, 
                    function(sentence, pos.word, neg.word){
                      # 의미없는 단어(문장부호, 기호, 숫자) 제거
                      sentence <- gsub('[[:punct:]]','',sentence)
                      sentence <- gsub('[[:cntrl:]]','',sentence)
                      sentence <- gsub('\\d+','',sentence)
                      
                      # 소문자로 변환 후 문장을 단어 단위로 분리
                      sentence <- tolower(sentence)
                      word.list <- str_split(sentence, '\\s+')
                      words <- unlist(word.list)
                      
                      # 분리된 단어와 감성 사전의 단어와 비교
                      pos.match <- match(words, pos.word)
                      neg.match <- match(words, neg.word)
                      
                      pos.match <- !is.na(pos.match)
                      neg.match <- !is.na(neg.match)
                      
                      # 점수계산 = 긍정일치수 - 부정일치수
                      score <- sum(pos.match) - sum(neg.match)
                      
                      return(score)
                      
                    }, pos.word, neg.word, 
                    .progress = .progress)
    
    # 내부 함수 실행 결과를 데이터프레임으로 변환
    scores.df <- data.frame(score=scores, 
                            text=sentences)
    
    return(scores.df)
  } #score.sentiment

# apple에 대한 트윗을 기반으로
# 감성분석 후 점수 출력
apple.score <- score.sentiment(apple.text, pos.word, neg.word,
                               .progress = 'text')

# 감성분석 결과를 그래프로 출력
# 0보다 크면 긍정의 의미
hist(apple.score$score)


# 삼성
samsung.text <- lapply(samsung.tweets, 
                     function(t){t$getText()})

samsung.score <- score.sentiment(samsung.text, pos.word, neg.word,
                                 .progress = 'text')

hist(samsung.score$score)

