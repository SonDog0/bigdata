# 텍스트 데이터 다루기
# 텍스트(단어의 시퀀스 , 문자의 시퀀스 ), 시계열 또는
# 일반적은 시퀀스 데이터를 처리할 수 있는 딥러닝 모델
# 순환신경망 recurrent neural network , 1D convnet

# 문서분류 - 시계열분류 글의 주제나 책의 저자 실별
# 시계열비교 두 문서가 얼마나 밀접한지 여부
# 시퀀스-to-시퀀스, 영어를 프랑스어/일본어로 변환
# 감성분석 , 트잇 ,리뷰가 긍정 / 부정 여부 파악
# 시계열 예측 , 이전 날씨데이터로 향후 날씨 예측
# => 문자언어. 시계열에 대한 통계적 구조를 파악후 해결
# => 자연어 처리를 통해 단어 , 문장 , 문단에 패턴 적용후 인식

# 문자데이터의 패턴화
# 텍스트를 수치형 텐서로 변환하는 과정 필요 => 벡터화
# 텍스트를 단어로 나누고 각 단어를 하나의 벡터로 변환
# 텍스트를 문자로 나누고 각 문자를 하나의 벡터로 변환
# 텍스트를 단어나 문자의 n-그램을 추출 한 후 각 n-그램을 하나의 벡터로 변환
# => 텍스트를 각 나누는 단위 ( 단어 , 문자 , n-그램)를 토큰token 이라함
# 텍스트를 토큰으로 나누는것을 토큰화라 함

# 토큰과 단어를 연결 => 원핫 인코딩 , 토큰임베딩 (이중 단어 임베딩)

# 원핫 인코딩 : 희소행렬 (0으로 채워짐 ) , 고차원( 단어수와 같음 ) , 단어 유사도 표현하기 어려움
# 단어 임베딩 : 실수형 벡터, 저차원(차원의저주를 피함), 단어 유사도 표현 할 수 있음 ,
# 즉 단어 벡터 사이의 추상적이고 가하학적인 관계를 얻기위해 단어를 기하학적인 공간에 나열(매핑)해야함
# 다시 말해, 단어를 R차원의 벡터로 매핑함

# word2vec 작동원리
# '친구를 보면 그 사람을 알 수 있다 '
# '단어 주변을 보면 그 단어를 알 수 있다 '
# 따라서, 비슷한 맥락을 갖는 단어에 비슷한 위치(벡터)를
# 주려면 predictive method 방식으로 훈련을 시켜야함
# 즉 , 일종의 지도학습 형태로 훈련시켜야 함


# 한편 , word2vec은 사실 비지도학습방식의 알고리즘을 사용
# => CBOW , skip-gram 모델을 사용
# CBOW : continous bag of word , 맥락(주변단어)으로 단어 예측