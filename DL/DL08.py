# 단어 임베딩을 사용해 유사성 파악하기
# 원핫인코딩 vs 토큰임베딩

# 단어임베딩을 구현해서 word2vec 기능을 사용하려면
# 구글에서 만든 gensim 라이브러리를 설치해야함

from gensim.models import word2vec
from gensim.models.keyedvectors import KeyedVectors

# 문장 읽어옴
with open('./sentences.txt ' , 'r' , encoding='utf-8') as f :
    text = f.readlines()
print(text)
print(type(text))

tokens = [s.split() for s in text] # 공백기준으로 단어별로 분리

print(tokens)

# 단어임베딩 생성

embeddings = word2vec.Word2Vec(tokens , size = 5 , window= 1 , negative= 3 , min_count= 1)
# size = 벡터의 차원수
# window = 맥락파악을 위한 주변 단어 수
# negative = 학습시 정답/ 오답에 대한 점수 비율
# min_count = 임베딩 대상 출현 조건 (최소 1번 출현 단어 )

print(embeddings)
# 단어임베딩 모델 저장
# 1 : gensim으로 모델 저장
embeddings.save('gensim.model')
# 2 : word2vec으로 모델 저장
embeddings.wv.save_word2vec_format('word2vec.model' , binary=False)

# 단어 유사성 확인
# 모델 불러오기
model1 = word2vec.Word2Vec.load('gensim.model')
model2 = KeyedVectors.load_word2vec_format('word2vec.model' , binary=False , encoding='utf-8')

# 해당 단어의 워드 임베딩 벡터값 살펴보기
print(model1.wv['너를'])
# print(model2.wv['너를'])
# 유사성 확인
print(model2.most_similar('나는'))
print(model2.most_similar('사랑해'))

# word2vec + deep learning 샘플 사이트
# ronxin.github.io/wevi
# word2vec과 단어임베딩의 작동원리 파악
# apple , orange , rice => eat
# juice , milk , water => drink
# 훈련횟수가 200~250번 정도 일때
# eat , drink에 대한 군집효과가 좋아짐


# 한국어 word2vec 구현 사이트
# w.elnn.kr/search/

# pretrained korean word2vec model 이용한 유사도 확인
kor_w2v = word2vec.Word2Vec.load('c:/Java/data/ko.bin')
print('pretrained korean word2vec model 이용한 유사도 확인')
print(kor_w2v.most_similar('미움'))
print(kor_w2v.most_similar('사랑'))
print(kor_w2v.most_similar('너'))
print(kor_w2v.most_similar('나'))

# 케라스를 이용한 단어수준의 원핫인코딩
from keras.preprocessing.text import Tokenizer

texts  = ['The cat sat on the mat.' , 'The dog ate my homework.']

tokenizer = Tokenizer(num_words=10)
tokenizer.fit_on_texts(texts) # 단어 토큰화

sequns = tokenizer.texts_to_sequences(texts)
# 문자열을 정수 인덱스의 리스트로 변환

onehot = tokenizer.texts_to_matrix(texts , mode = 'binary')


print(sequns)
print(onehot)

