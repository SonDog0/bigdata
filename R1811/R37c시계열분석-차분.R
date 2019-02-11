# 시계열 분석방법
회귀분석, ARMA 모형 : 수학적 이론 근거,
                      변동이 많은 시계열 자료에 적용(장기예측)

지수평활법, 시계열 분해법 : 
                      변동이 다소 적은 시계열 자료에 이용(단기예측)

# 시계열 분석 하기전...
시계열은 전형적으로 불규칙 혹은 오차성분을 포함
자료를 특정 패턴으로 분석 가능하도록
급격한 파동을 줄이는(일정하게) 평활화가 필요(smoothing)

# 정상 vs 비정상 시계열
정상 시계열 : 어떤 일정한 값을 중심으로
              일정한 변동폭을 가지며 
              시간에 따라 변하는 형태의 패턴을 가짐
              (평균/분산 일정)

비정상 시계열 : 정상성이 없음.
                평균, 분산이 일정치 않음
                대부분의 주식차트는 비정상 시계열


# 시계열 분석 필요조건
시계열 분석을 위해서 
비정상 시계열을 정상 시계열로 바꿔야 함

시계열을 평활화하는 가장 단순한 방법은
이동평균 MA /차분/변수변환 사용

TTR 패키지의 SMA, zoo 패키지의 rollmean,
forecast패키지의 ma 등이 있음


# 차분과 변수변환
차분 diff : 현재 시점에서 이전시점의 값을
            빼주므로서 차이값을 시계열로 만듦
            diff(데이터, 차분횟수)

변수변환 : 데이터에 log를 씌워서 변화폭을 줄여 시계열로 만듦, 
           분산이 변하는 형태에 적용
              
# 예제) 월간항공기 승객수
ap <- AirPassengers
plot(ap)

# 시계열 자료의 4가지 특성별로 그래프 출력
plot(decompose(ap))


ap <- log(ap)   # 변수변환 실시
plot(ap)

ap1 <- diff(ap)  # 차분 실시
plot(ap1)

ap2 <- diff(ap,2)  # 차분 실시 - 간격이 더벌어지고 높낮이가 더 심해짐
plot(ap2)

ap3 <- diff(ap,3)
plot(ap3)


# 예측
비정상시계열을 정상시계열로 만들었다면 실제 예측해 봄

install.packages('forecast')
library(forecast)

ap1 <- AirPassengers
ap1 <- log(ap1)
ap1 <- diff(ap1)
plot(ap1)

# 시계열을 토대로 예측(임시)
predict <- forecast(ap1)
predict <- forecast(ap1, h=6)
plot(predict)
predict


