# 의사결정 나무
의사결정 규칙을 계층적 나무구조로 도표화하여
분류 및 예측을 할 수 있는 분석방법
데이터 유형 - 연속형 수치, 범주형 값


데이터를 분석하여 이들 사이에 존재하는 패턴을 
예측가능한 규칙들의 조합으로 나타냄
그 모양이 나무처럼 보인다해서 DT라 부름
마치 스무고개를 통해 문제를 해결하는 것과 유사

ex) 대출시 대상자의 시용평가
    독버섯과 식용버섯을 분류
    다음달에 연체할 가능성이 있는 고객 판별
    약정이 끝나면 다른 통신사로 이동할 고객 판별
    타이타닉에서 살아남을 사람 분류

# 의사결정나무 알고리즘 분류

C4.5, C5.0 : 엔트로피
CART       : 지니지수
CHAID      : 카이제곱통계량 P값, F-검정값

의사결정나무의 가지 생성방법

어떤 입력변수를 이용하여 어떻게 분리하는 것이
목표변수의 분포를 잘 구분할 수 있는지 
파악하는 정도를 순수도/분순도로 정의


순수도 또는 불순도를 기준으로 나무를 성장시킴
즉, 부모마디에서 자식마디로 분리될 때
자식마디는 부모마디보다 순수도가 높거나
불순도가 낮아야함


순수도가 증가/불순도가 감소하는 상황을
정보이론에서는 정보이득information gain이라 함

따라서, 순수도를 계산하는 방식(엔/지/카)에 따라
의사결정 나무 알고리즘이 나뉨(C5/CART/CHAID)


엔트로피 entropy

확률변수의 값이 0,1을 가지는 어떤 확류분포 Y가 있을 때
1)P(Y=0) : 0.5, P(Y=1) : 0.5
  => Y의 확률이 0인지 1인지 구분이 안됨
  (엔트로피 높음 - 무질서 상태)

2)P(Y=0) : 1.0, P(Y=1) : 0
  => Y의 확률이 0인 것이 구분됨
  (엔트로피 낮음 - 질서상태)

3)P(Y=0) : 0.7, P(Y=1) : 0.3
  => Y의 확률이 0이라고 어느정도 구분됨

확률분포가 가지는 확신의 정도를
수치상으로 표현한 것을 엔트로피라 함
확률변수가 각각의 특정값이 나올 확률이 비슷한경우
  -> 엔트로피가 높다고 함

어떤 특정값이 나올 확륭이 높고,
나머지 값의 확률은 낮은경우
  -> 엔트로피가 낮다고 함

즉, 데이터의 무질서도를 정량화해서 표현한 값
어떤 집합의 엔트로피가 높다는 것은
그 집단의 특징을 찾는것이 어렵다는 뜻

물리학에서는 상태가 분산되어 있는 정도를 엔트로피로 정의
여러가지로 고루 분산되어 있으면 e가 높고
특정한 하나의 상태로 몰려있으면 e가 낮음

한편, 각 메세지에 포함된 정보의 기대값을
정보 엔트로피라고 함

일반적으로 엔트로피는 무질서도 또는 
불확실성을 가리키며 0~1사이 값을 가짐

지니지수
엔트로피처럼 확률분포가 어느쪽에 더 치우쳐있는가를 재는 척도
단, 수식에 로그를 사용하지 않으므로
계산량이 적어 엔트로피 대신 많이 사용하기도 함

# R에서의 의사결정나무 관련 패키지
rpart : CART알고리즘 : 지니지수
party : CART알고리즘 개선버전
C50 : 엔트로피 지수 사용


# credit bank
개인 대출을 받은 고객을 분류

고객번호, 나이, 경력, 소득, 우편번호, 가족수,
신카사용금액, 교육수준, 주택대출여부,
개인대출여부, 증권계좌보유, 펀드계좌보유,
신용카드보유

8 : 중졸,고졸,대졸(1,2,3)
10~14 : yes,no(1,0)



# 0.전처리, 탐색적 분석
setwd('c:/Java/data')
bank <- read.csv('creditbanks.txt',sep=',', header=T, stringsAsFactors = F)

str(bank)
summary(bank)

분석에 관련없는 고객번호, 우편번호는 제외
banks <- bank[,-c(1,5)]

summary(banks)

banks 데이터에서PersoanlLoan이 레이블(목표변수)임
목표변수를 범주형 변수로 변환함

banks$PersonalLoan <- as.factor(banks$PersonalLoan)


대출여부를 빈도로 확인
table(banks$PersonalLoan)

대출여부를 빈도로 확인
table(banks$PersonalLoan)
대출거부가 대출승인보다 많음 -> 결과왜곡 우려
대출거부 level 값이 0으로 지정 
        -> 혼돈행렬에서는 0은 긍정의 의미
따라서, 의미에 맞게 level 값을 변경

banks$PersonalLoan <- relevel(banks$PersonalLoan, ref='1')
levels(banks$PersonalLoan)


# 1. train/test
library(caret)

str(banks)

set.seed(2018112216)
idx <- createDataPartition(banks[,8], p=0.7, list=F)
train <- banks[idx,]
test <- banks[-idx,]

table(train$PersonalLoan)
table(test$PersonalLoan)


# 2. 의사결정나무
install.packages('rpart')
library(rpart)

dt_banks <- rpart(formula = PersonalLoan~.,
                  data= train,
                  parms = list(split='gini'),
                  method = 'class',
                  control = rpart.control(minsplit = 20, cp=0.01, maxdepth = 10))

# parms    : 나무 가지 생성 기준 설정
# method   : class : 분류, anova: 회귀모델
# control  : 의사결정나무의 가지 생성 정도 설정
#           maxdepth : 가지의 깊이
#           minsplit : 가지 생성 기준 관측값의 최소값
#           cp : 비용 복잡도 지정

# 생성된 모형 확인
summary(dt_banks)

dt_banks

plot(dt_banks,
     compress = T,
     uniform = T,
     branch = 0.8,
     margin = 0.1)

text(dt_banks, use.n = T,
     all=T, cex=0.8)

# 의사결정나무를 보다 세련되게 출력
install.packages('rpart.plot')
library(rpart.plot)
rpart.plot(dt_banks)


library(RColorBrewer)
myCol <- brewer.pal(n=3, name='Set2')
  => 색상팔레트중 3번째 팔레트의 Set2 선택

prp(dt_banks, faclen=0,
    cex=0.8, extra=101,
    box.pal=myCol[dt_banks$frame$yval])

faclen : 그래프 맨 끝에 레이블 출력
extra : 그래프 맨끝에 레이블 빈도 출력
box.pal : 그래프 맨 끝 박스 색상 지정

나무의 각 가지 끝에는 레이블과
그 레이블로 결과를 도출한 정보가 표시
맨 왼쪽 가지의 레이블은 1로 결정 했는데
실제 데이터의 1과 0의 비율이 232 : 1 이기 때문임
아래 7%라는 의미는 특정 케이스로 대출거부될 확률을 나타냄






의사결정나무의 가지수에 따라 성능이 좌우
따라서, maxdepth 값을 얼마로 지정하는것이 
좋을지 판단하는 것도 중요
plotcp(dt_banks)

dt_banks20 <- rpart(formula = PersonalLoan~.,
                  data= train,
                  parms = list(split='gini'),
                  method = 'class',
                  control = rpart.control(minsplit = 20, cp=0.01, maxdepth = 20))

plotcp(dt_banks20)

dt_banks6 <- rpart(formula = PersonalLoan~.,
                    data= train,
                    parms = list(split='gini'),
                    method = 'class',
                    control = rpart.control(minsplit = 20, cp=0.01, maxdepth = 6))

plotcp(dt_banks6)


# 3. 성능평가
pred_banks <- predict(object = dt_banks,
                      newdata = test,
                      type='class')

library(caret)
confusionMatrix(data = pred_banks,
                reference = test$PersonalLoan)




# iris 데이터 셋을 이용해서 의사결정나무 알고리즘 적용
 