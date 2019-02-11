# 워드 클라우드
# cran.r-project.org/web/packages/wordcloud2
install.packages('wordcloud2')
devtools::install_github('lchiffon/wordcloud2', force=T)
library(wordcloud2)

head(demoFreq)
str(demoFreq)

wordcloud2(demoFreq, size = 1, shape = 'star')
wordcloud2(demoFreq, size = 1, shape = 'star',
           fontFamily = '맑은 고딕')
wordcloud2(demoFreq, size = 1,
           fontFamily = '맑은 고딕',
           minRotation = -pi/2,
           maxRotation = -pi/2)
wordcloud2(demoFreq, size = 1,
           fontFamily = '맑은 고딕',
           minRotation = -pi/6,
           maxRotation = -pi/6)
wordcloud2(demoFreq, size = 1, 
           color = 'random-light',
           backgroundColor = 'black')


# Documents\R\win-library\3.5\wordcloud2
figPath=system.file("examples/t.png",
                    package="wordcloud2")
wordcloud2(demoFreq, figPath = figPath,
           size = 1.5, color="skyblue")


########
wordcloud2(demoFreq, size = 1,
           color = 'skyblue',
           figPath = 'c:/Java/data/h.png')
wordcloud2(demoFreq, size = 1,
           color = 'skyblue',
           figPath = 'c:/Java/data/bh.png')
########

