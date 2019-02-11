# 자연어 처리

# 텍스트분석 3가지 유형
# 텍스트분류
# 텍스트군집
# 텍스트요약

# 형태소 분석
주어진 단어 또는 어절을 구성하는 각 형태소를
분리한 후 분리된 형태소의 기본형 및 품사정보를 추출

# 형태소
의미가 최소 단위로서
더 이상 분리할 수 없는 가장 작은 의미 요소

# KoNLP : korean natural language processing
한글 자연어 처리 분석 패키지
KoNLP는 rJava, memoise 패키지가 부수적으로 필요
# github.com/haven-jeon/KoNLP


install.packages('devtools')
install.packages('rJava')

install.packages('memoise')
install.packages('KoNLP')
install.packages('dplyr')

library(devtools)
library(rJava)
library(memoise)
library(KoNLP)
library(stringr)
library(dplyr)


Sys.setenv(JAVA_HOME='C:/Java/jdk1.8.0_181')
# JDK 설치 위치 지정


# 형태소 분석을 위한 참고사전이 필요
# 분석할 문장에 포함된 단어들이
# 사전에 알맞는 형태(품사)로 정의되어 있어야
# 정확한 분석 가능
# 이를 위해 KoNLP에는 세종사전이 포함되어 있음
#useSejongDic()    # 370957
useNIADic()       # 983012 단어수가 가장 많음!
#useSystemDic()    # 283949

# 형태소 분리 예
extractNoun(text)  명사 위주 분류
SimplePos09(text)  품사를 9개 기준으로 분류
N:명사, P:동사/형용사, M:부사
J:조사, E:어미, X:접미사

SimplePos22(text)  품사를 22개 기준으로 분류 
MorphAnalyzer(text) 품사를 상세한 수준으로 분류


text <- '아버지 가방에 들어가신다'
extractNoun(text)
SimplePos09(text)
SimplePos22(text)
MorphAnalyzer(text)

text <- '아버지가 방에 들어가신다'
extractNoun(text)
SimplePos09(text)
SimplePos22(text)
MorphAnalyzer(text)

text <- '나는 보리밥을 먹었다'
extractNoun(text)
SimplePos09(text)
SimplePos22(text)
MorphAnalyzer(text)

text <- '롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다'
extractNoun(text)
SimplePos09(text)
SimplePos22(text)
MorphAnalyzer(text)


ex) 대통령 연설문에서 자주 언급되는 단어를
분석하고 워드클라우드로 시각화하기

speech <- readLines('c:/Java/data/speech.txt')
# txt 파일의 내용을 읽어서 변수에 저장

head(speech, n=5)

# 1전처리 작업
# 불필요한 불용어(공백,특수문자)를 처리
# gsub : 문자열 치환 함수
# gsub(패턴, 치환문자, 대상)

speech <- gsub('[~?!@%&#()_+=<>]', '', speech)
speech <- gsub('[0-9]', '', speech)
speech <- gsub('[a-zA-Z]', '', speech)
speech <- gsub('[ㄱ-ㅎ]', '', speech)
speech <- gsub('[ㅜㅠ]', '', speech)
speech <- gsub('\\-', '', speech)

speech <- gsub('물뽕|입하|광고|할인', '', speech)

head(speech)


# 2명사추출
nouns <- extractNoun(speech)

wdc <- table(unlist(nouns))
추출된 명사의 빈도표 작성  

df_word <- as.data.frame(wdc, stringAsFactor=F)
빈도표로 작성된 데이터를 데이터프레임으로 변경
head(df_word)

df_word <- rename(df_word, 
                  word=Var1, freq=Freq)
데이터프레임의 각 열 이름 변경

df_word$word <- as.character(df_word$word)
df_word <- filter(df_word, nchar(word)>=2)
문자길이가 2자 이상인 단어를 걸러냄

top20 <- df_word %>%
         arrange(desc(freq)) %>%
         head(20)
df_word의 내용을 빈도수로 정렬한 후 
상위 20개만 추려냄

top20


# 3워드클라우드
# cran.r-project.org/web/packages/wordcloud2
# install.packages('wordcloud2') mask 작동안함
devtools::install_github("lchiffon/wordcloud2")
library(wordcloud2)

head(demoFreq)  # wordcloud2 데모용 데이터
str(demoFreq)

wordcloud2(demoFreq, size=1, shape='star')
wordcloud2(top20, size=1, shape='star',
           fontFamily='맑은 고딕')

wordcloud2(demoFreq, size=1,
           minRotation = -pi/2,
           maxRotation = -pi/2)
wordcloud2(top20, size=1, 
           minRotation = -pi/2,
           maxRotation = -pi/2,
           fontFamily = '배달의민족 도현')

wordcloud2(demoFreq, size=1,
           minRotation = -pi/6,
           maxRotation = -pi/6)
wordcloud2(top20, size=1, 
           minRotation = -pi/6,
           maxRotation = -pi/6,
           fontFamily = '배달의민족 도현')


wordcloud2(demoFreq, size=1,
           color='random-light', 
           backgroundColor='grey')


# Documents/R/win-library/3.5/wordcloud2
figPath = system.file("examples/t.png",
                     package = "wordcloud2")
wordcloud2(demoFreq, figPath = figPath, 
           size = 1.5, color = "skyblue")


wordcloud2(top20, 
           figPath="c:/Java/data/bh.png",
           size=1.5,
           backgroundColor='white')



wordcloud2(demoFreq, 
           figPath = "c:/Java/data/h.png", 
           size = 1.5, color = "skyblue", 
           backgroundColor="black")




ex) 2018년 7월, '월드컵'이라는 주제로
트위터에서 각종 텍스트를 수집했다
이를 분석하고 워드클라우드로 시각화하세요

worldcup <- readLines('c:/Java/data/worldcup2018-07-04.txt', encoding = 'UTF-8')

# 전처리
worldcup <- gsub('[~?!@%&#()_+=<>]', '', worldcup)
worldcup <- gsub('[0-9]', '', worldcup)
worldcup <- gsub('[a-zA-Z]', '', worldcup)
worldcup <- gsub('[ㄱ-ㅎ]', '', worldcup)
worldcup <- gsub('[ㅜㅠ]', '', worldcup)
worldcup <- gsub('\\-', '', worldcup)
worldcup <- gsub('\\[', '', worldcup)
worldcup <- gsub('\\]', '', worldcup)
worldcup <- gsub('\\:', '', worldcup)
worldcup <- gsub('\\-', '', worldcup)

worldcup <- gsub('발기|비아그라구|오사|부전|비아그라|일정|이번|드래곤|출처|비아그라부작|
                 스포츠|네이버|구입|다음|씨알|우리|여기클릭→/|오늘|', '', worldcup)

worldcup <- gsub('일본지|초강력|최저가|진짜|브라|조루치료|치료|들이|생각|해서|시작|비야그라|어제|리스|', '', worldcup)


worldcup <- gsub('작업용흥분|사용|건강|수면제|안정|액체|조현|이야기|', '', worldcup)

worldcup <- gsub('해외|하나|시알|신새', '', worldcup)

worldcup <- gsub('아이|으로', '', worldcup)

worldcup <- gsub('물뽕하는|물뽕|물뽕파는절|정품|사람', '', worldcup)

worldcup <- gsub('물뽕하는|물뽕|물뽕파는절|정품|사람', '', worldcup)

# 명사추출
nouns <- extractNoun(worldcup)
wdc <- table(unlist(nouns))
dfwd <- as.data.frame(wdc, stringAsFactors=F)
dfwd <- rename(dfwd, word=Var1, freq=Freq)

dfwd$word <- as.character(dfwd$word)
dfwd <- filter(dfwd, nchar(word) >= 2)

top35 <- dfwd %>% arrange(desc(freq)) %>%
          head(35)
top35

top35[1,2] <- 950  # 수치가 너커무 서서 수치조저

wordcloud2(top35, 
           figPath = "c:/Java/data/h.png", 
           size = 1.5, color = "skyblue", 
           backgroundColor="black")


ex) 토지1권에 쓰인 텍스트를 분석하고 
워드클라우드로 시각화하세요