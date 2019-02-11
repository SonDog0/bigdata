# k-apt.go.kr 크롤링 예제
# 팝업창 자동 닫기, 단지정보 자동 입력
# hello_selenium_06.py 소스 참고

library(RSelenium)
library(rvest)

chrome <- remoteDriver('localhost', 9563, 'chrome')

chrome$open()
chrome$maxWindowSize()
chrome$navigate('http://k-apt.go.kr')

popups <- chrome$findElements('class', 'layerPopup')
#   => 클래스 명이 layerPopup 인 요소들을 추출

# popups[[1]]$getElementAttribute('id')
# popups[[2]]$getElementAttribute('id')
# popups[[3]]$getElementAttribute('id')

for (i in 1:3){
  id <- popups[[i]]$getElementAttribute('id')
  # print(id)
  # js <- paste('closeLyserPopup(\'',id,'\')')
  js <- paste0('closeLyserPopup(\'',id,'\')')
  # print(js)
  chrome$executeScript(js)
  Sys.sleep(1)
}

nav2 <- chrome$findElement('css','a.navi2')
nav2$clickElement()
#   => 단지정보 버튼 추출 후 클릭

combo <- chrome$findElement('xpath',
                            '//*[@class="combo_YYYY"]/option[text()="2018"]')
combo$clickElement()
Sys.sleep(1)
