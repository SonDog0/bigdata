# 박스 그래프(box and whiskers plot) - 상자수염 그래프
# 연속형 변수에 대해 최소/ 1사분위/중위/3사분위/최대값등을
# 시각적으로 확인 할 수 있게 그리는 그래프

# mtcars 데이터셋
mtcars
?mtcars
summary(mtcars)
boxplot(mtcars$mpg, data=mtcars,ylim=c(10,35),
        col=rainbow(1), names=c('mpg'))

# cyl 별 연비 현황파악
mtcars$cyl
boxplot(mpg~cyl, data = mtcars,ylim=c(10,35))

# gear 별 차량 연비
mtcars$gear
boxplot(mpg~gear, data = mtcars, ylim=c(10,35))

# 평균을 계산해서 그래패에 점으로 표시
means <- tapply(mtcars$mpg, mtcars$gear, mean)

points(means, col='red', pch=18)


# 핫도그 컨테스트 데이터셋 참고
# 핫도그 우승자의 핫도그 먹은 개수 현황을
# 박스 그래프로 작성
boxplot(hotdog$Dogs.eaten, data=hotdog, names = c('Dogs.eaten'))

# 타이타닉 데이터셋
# 탑승자의 나이 현황
boxplot(titanic$Age, data=titanic)

# 인사정보hr-employees
# 사원들의 급여 현황
boxplot(emp$SALARY, ylim=c(2000,26000))
means <- mean(emp$SALARY)
means
points(means,col='red',pch=18)

# 이상치 24000을 제외하고 다시 박스그래프 작성
sal <- emp$SALARY[emp$SALARY != 24000]
means <- mean(sal)
means
points(means, col='blue',pch=18)
