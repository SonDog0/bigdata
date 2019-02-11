# 초코렛 봉지에 든 초코렛 색깔 비율 조사
# 초코렛 색상을 범주형 변수로 선언하고 level과 각 범주에 할당된 서수를 확인
Color <- c('Blue', 'Green', 'Orange', 'Yellow', 'Red', 'Brown')
fColor <- as.factor(Color)
levels(fColor)
as.numeric(fColor)

# 고객평가 빈도표를 참고하여 평가지표를 범주형 변수로 선언
# level 과 각 범주에 할당된 서수를 확인하세요
Rating <- c('Superior', 'Good', 'Average', 'Poor', 'Inferior')
fRating <- as.factor(Rating)
fRating
levels(fRating)
as.numeric(fRating)
