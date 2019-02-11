# 형태소 분석 2
# 영어 텍스트 분석 - tm 패키지

install.packages('tm')
library(tm)

setwd('c:/Java/data')
docs <- readLines('english.txt')

# tm 패키지가 처리하기 용이하도록
# 문장들을 벡터형으로 변환한 후
# 말뭉치로 저장

corp <- Corpus(VectorSource(docs))

corp

inspect(corp) # 말뭉치 내용 확인

# 텍스트 분석을 위한 전처리 작업
# 문장부호 제거
corp <- tm_map(corp,removePunctuation)

# 특정문자 제거
corp <- tm_map(corp,removeWords, c('0','1','2','and','but','not'))  # c()는 추가로 제거 하는것

# 대문자 -> 소문자
corp <- tm_map(corp,tolower)

# 전처리 결과 확인
strwrap(corp)
strwrap(corp[[1]])

# tm 패키지가 분석할 수 이는 형태로 변환
# TermDocument 형식의 행렬 구조
# 단어별 빈도를 측정하기 위한 목적

# 일반 문저 형태로 변환
# corp <- tm_map(corp, PlainTextDocument) - 안됨

tdm <- TermDocumentMatrix(corp)
tdm

# terms: 14, documents: 4
# 문장들 중에서 추출한 단어는 14개
# Sparsity           : 64%  -  의미있는 단어의 비율 64%

# 우리가 보기 편하기 위해 다시 행렬로 변환
tdmm <- as.matrix(tdm)
tdmm

# 단어별 집계 시행
freq <- sort(rowSums(tdmm), decreasing = T)
freq

# 빈도순으로 1~5까지 추출
freq[1:5]

# 막대 그래프로 시각화

barplot(freq[1:10], las = 3)


# 워드 크라우드로 시각화


# 명사추출
library(wordcloud2)
dfword <- data.frame(word=names(freq), freq=freq)
wordcloud2(dfword, size=1, shape='pentagon')

crop <- tm_map(corp, removeWords,
               stopwords('english'))
crop <- tm_map(corp, removeWords,stopwords,
               #c('and','but','not'))
crop <- tm_map(corp, tolower)



# 스탠포드 대학 - 스티브잡스 연설문

docs <- readLines('steve.txt')

#1 말뭉치 생성
crop <- Corpus(VectorSource(docs))
# 전처리
crop <- tm_map(crop, tolower)
crop <- tm_map(crop, removeNumbers)
crop <- tm_map(crop, removePunctuation)
crop <- tm_map(crop, stripWhitespace)
crop <- tm_map(crop, removeWords,
               stopwords('english'))

crop <- tm_map(crop, removeWords,
               c('just','got','the','and','dont','didnt'))


# 빈도분석
tdm <- TermDocumentMatrix(crop)
tdmm <- as.matrix(tdm)
freq <- sort(rowSums(tdmm), decreasing = T)
wc <- freq[1:30]
barplot(wc,las=3)

wc2 <- data.frame(word= names(freq), freq=freq)
wordcloud2(wc2, size = 1, shape='star')


# 트럼프
setwd('c:/Java/data')
docs <- readLines('thrump.txt')

#1 말뭉치 생성
corp <- Corpus(VectorSource(docs))
# 전처리
corp <- tm_map(corp, tolower)
corp <- tm_map(corp, removeNumbers)
corp <- tm_map(corp, removePunctuation)
corp <- tm_map(corp, stripWhitespace)
corp <- tm_map(corp, removeWords,
               stopwords('english'))

corp <- tm_map(corp, removeWords,
               c('just','got','the','and','dont','didnt'))


# 빈도분석
tdm <- TermDocumentMatrix(corp)
tdmm <- as.matrix(tdm)
freq <- sort(rowSums(tdmm), decreasing = T)
wc <- freq[1:30]
barplot(wc,las=3)

wc2 <- data.frame(word= names(freq), freq=freq)
wordcloud2(wc2, size = 1, shape='star')





# tm 패키지를 이용해서
# 특정단어와 연관있는 단어를 찾거나 
# 지정 빈도 이상/미만 단어 검색

findFreqTerms(tdm)
findFreqTerms(tdm, lowfreq = 2)  # 2회 이상
findFreqTerms(tdm, highfreq = 3)  # 3회 이하

findAssocs(tdm,'apple', corlimit = 0.5)
