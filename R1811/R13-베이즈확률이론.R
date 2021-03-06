#나이브 베이즈 확률 이론

#동전을 100회 던졌을때 앞면이 나오는 횟수는?
#전통적 확률에서는 일어난 횟수/전체시도횟수로 계산
# =>경험적 확률 = 일정한 확률로 반복 실행

#만일 A라는 도시에 수지가 태어날 경우
#이 아이가 노벨상을 받을 확률은 얼마나 될까?

#이것을 경험적 확률로 계싼하려면
#이 아이를 여러명 살게하고
#그 중 몇명이 노벨상을 받는지 평가해보면된다.

#문제는 동일한 유전자,환경에 자란 아이를 만들수 있는가?
#이러한 상황에서 베이즈 확률론을 이용한다.
#일어나지 않을 일에 대한 확률을 불확실성이라는 개념으로 이야기 한다.

#몬티홀 문제 - 미국 티비쇼에서 유래한 퍼즐



#아들딸 패러독스
#두 아이가 있는 어떤 집에서 [첫 아이]가 남자일때
#두 아이 모두가 남자일 확률은?

#두 아이가 있는 어떤 집에서 [한명이]남자일때
#두 아이 모두가 남자일 확률은?


#베이즈 정리
#이전의 경험과 현재의 증거를 토대로 어떤 사건의 확률을 추론하는 알고리즘
#따라서, 사건이 일어날 확률을 토대로 의사결정을 하는경우
#그와 관련된 사전정보를 얼마나 알고있나에 따라 크게 좌우한다.

#기하학 - 피타고라스 정리
#확률학 - 베이즈 정리

#베이즈 정리 예제
#삼키기 어려울 정도의 목에 통증 유발 - 인후염
#병원 방문후 검사(정확도 90%) 시행 -> 결과 양성(폐암)
#의사: 이 결과로 폐암일 확률은 10%도 안될 수 있다. 폐암에 걸린 남성은 성인 남성 1%
#환자: 그래도 걱정이 되니 추가 검사 시행 - 음성(!)

#베이즈 정리에 근거, 실제 검사에서 양성이 나왔을때 진짜 폐암에 걸릴 확률은???
베이즈정리 : P(A|B) = P(A)P(B|A)/P(B)
조건부 확률 : P(A n B) = P(A)P(B|A) = P(B)P(A|B)
P(A n B) = P(B)P(A|B)에서
P(A|B) =P(A n B)/P(B) 로 도출가능
P(A|B) =P(A)P(B|A)/P(B)에서
P(A|B) =P(B)P(A|B)/P(B)로도 도출가능

양성일때 -> 폐암일 확률 
P(폐암|양성) = P(폐암 n 양성)/P(양성) = P(폐암)P(양성|폐암)/P(양성)
폐암일때 ->양성일 확률
P(양성|폐암) = P(양성) n 폐암)/P(폐암) = P(양성)P(폐암|양성)/P(폐암)
#정확도 90%검사로 양성일때 폐암일 확률
P(양성|폐암)=0.9
P(음성|폐암)=0.1

#성인남성이 폐암에 걸릴 확률
p(폐암) = 0.01

P(양성) : 폐암이고 진짜 양성일 확률과 폐암이 아닌고 양성일 확률을 더한 확률

P(양성|폐암)P(폐암)+P(양성|1-폐암)P(1-폐암)
0.9*0.01 +0.1*0.99 = -0.108 = 11%

P(폐암)P(양성|폐암)/P(양성)
0.01*0.9/0.108 = 0.083 =>8.3%

#시간이 지나 다시 목이아프코 숨을 쉬기 어려워서 다시 병원에 감
#다시 검사(정확도99%)해보니 역시 양성
#예전 경험에 비춰 별거 아니라고 생각했지만 폐암 확률이 50%증가
#의사는 심각할수 있다 충고
0.99*0.01 +0.01*0.99 = 0.0198
0.01*0.99/0.0198 =>50%


#ex)1.동호회 회원수가 100명일때 여성은 40명남성ㅇ은 60명이다
#이중 기혼인 여성은 16명 남성은 30명이라할때 임의로 뽑은 회원이 기혼이라 할때 여성일 확률은?
P(g)= 0.4
p(m) = 0.6

P(여성|기혼) =  P(여성 n 기혼)/P(기혼)
P(A n B) = P(B)P(A|B)=P(A)P(B|A)을 토대로
P(여성|기혼) =  P(여성 n 기혼)/P(기혼)
P(여성n기혼) =  P(기혼)P(여성|기혼) =P(여성)P(기혼|여성)

P(g) = 0.4
P(기혼|여성) = 16/40 = 0.4
P(기혼) =여성이 기혼일 확률 +남성이 기혼일 확률
P(여성)P(기혼|여성)+P(남성)P(기혼|남성)
0.4*0.4+0.6*0.5 = 0.46
P(A)P(B|A)/P(B)
P(여성|기혼)= P(여성)P(기혼|여성)/P(기혼)
0.4*0.4/0.46 = 0.347 =>약 35%

#2.2개의 조립라인을 가진 공장에서 각 라인에서 생산된 1000대의 휴대폰이 있다. 
#1번/2번 조립라인에서 생산된 휴대폰의 불량품이 각각 10%, 15%일때,
#임의로 뽑은 휴대폰이 불량일때,이것이 1본 조립라인에서 생산되었을 확률은? 
P(1|불량) = P(1)P(불량|1)/P(불량)
P(불량) = P(1)P(불량|1)+P(2)P(불량|2)
P(불량|1) = 0.1
P(불량|2) =0.15
P(1) = P(2) = 1
=0.25
P(1)P(불량|1)/P(1)P(불량|1)+P(2)P(불량|2)
0.5*0.1/(0.5*0.1+0.5*0.15) = 0.4 =>40%

#3.2개의 상자에 검은공과 흰공이 각각2,2/1,2 있다고 할때, 임의로 상자를 선택해서
#공을 1개 꺼냈더니 검은공이 나왔다. 그상자에 남은 공이 모두 흰공일 확률은?
P(A|B) = P(A n B) /P(B)
P(A n B) = P(B)P(A|B)=P(A)P(B|A)

P(b|검은공) = P(A n B)/P(B),P(A n B)/P(B) / P(A)=
  P(b n 검은공)/P(검은공)= P(A)P(B|A)/P(검은공)=
  P(b)P(검은공|b)/P(검은공)

P(B) = 1/2
P(검은공|B) = 1/3
P(A)P(B|A)/P(B)
P(검은공) = P(A)P(검은공|A) + P(B)P(검은공|B)
P(A)P(A|검은공) = 1/2*1/2 = 0.25
0.25 +(1/2 *1/3) = 0.416 =>42%
P(b|검은공) = =P(b)P(검은공|b)/P(검은공)
 0.5*0.3/0.4= 0.375 =>38%


#베이즈 이론의 활용 
#흉부회과 환자 303명 조사(나이,성별,검진정보)
#심장병 여부 판별

 #개인의 나이, 성별, 직업등의 데이터를 토대로 
 #영화 장르 추천 시스템
 
 #메일 제목으로 메일종류를 분석 
 #무료,빅데이터,상담,쇼핑,광고,모집,회원
 
 
 
 
 
 
 
 
 
 
 
 
 
