# 삼국지를 이용해서 자동문장 생성하기
import json , random , re
from konlpy.tag import Okt



def make_dic(words):
    tmp = ['@'] # @는 문장의 시작을 의미하는 기호
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3 : continue # 단어가 3개 모일때 까지 반복 실행
        if len(tmp) > 3 : tmp = tmp[1:] # 단어가 3개 모이면 단어사전에 등록
        # print(tmp)
        set_word3(dic,tmp)
        # if word == '.' : # 문장 처리가 끝나면 다음 처리를 위해 초기화
        #     tmp = ['@']
        #     continue

    return dic

def set_word3 (dic , s3):
    w1 , w2, w3 = s3
    if w1 not in dic : # 단어 사전에 등록되지 않았다면
        dic[w1] = {} # dic 사전형에 w1 키값을 비워둠
    if w2 not in dic[w1] :
        dic[w1][w2] = {} # 변수dic w1 키값 안에 w2 키값을 생성
    if w3 not in dic[w1][w2]:
        dic[w1][w2][w3] = 0

    dic[w1][w2][w3] += 1 # 단어 묶음 중 마지막 단어에 다음언어로 이동할 확률을 명시

def word_choice(sel):
    keys = sel.keys()
    sel_word = random.choice(list(keys))
    return sel_word

def make_sentence(dic):
    ret = []  # 자동 생성한 문장 저장용 변수
    if '@' not in dic: return 'no @ in dic!!'
    top = dic['@'] # @를 시작으로 해서
    w1 = word_choice(top) # 첫번째 단어 자동 선택
    w2 = word_choice(top[w1]) # 두번째 단어 자동 선택
    ret.append(w1)
    ret.append(w2)

    while True:
        w3 = word_choice(dic[w1][w2]) # 세번째 단어 자동 선택
        ret.append(w3)
        if w3 == '.' : break
        w1,w2 = w2,w3 # 생성된 이전 단어를 자리 이동
    ret = ' '.join(ret)
    return ret

def make_morph(docs): # 형태소 분석 및 형태 파악
    twitter = Okt()

    malist = twitter.pos(docs, norm=True)

    words = []
    for word in malist:
        if word[1] not in ['Punctuation']:  # 문장부호 제외
            words.append(word[0])
        if word[0] == '.':  # 마침표 등록
            words.append(word[0])
        if word[0] == '?':
            words.append(word[0])

    dic = make_dic(words)
    # print(dic)

    json.dump(dic,open('c:/java/data/3kingdoms.json' ,'w' , encoding='utf-8'))

def read_novel(fname):
    fname = '/'.join(['c:java/data',fname])
    with open(fname, 'r') as f:
        docs = f.readlines()
    return docs


# 프로그램 시작부

docs = read_novel('3kingdoms.txt')
#
# print(docs[:5])
# print('\n')

# 필요없는 특수문자 제거
docs2 =''.join(docs) #리스트를 일반 문자열로 변환
# print(docs2[:50])

docs2= re.sub(r'\s+',' ',docs2).strip()  #공백, 줄바꿈 제거
# print('공백, 줄바꿈 제거')
# print(docs2[:50])

# 형태소 분석
make_morph(docs2) # json 덤프생성

# 단어사전을 메모리에 적재
word_dic = json.load(open('c:/java/data/3kingdoms.json' , 'r' ))

# 자동문자 생성
print('random_1' , make_sentence(word_dic))
print('random_2' , make_sentence(word_dic))
print('random_3' , make_sentence(word_dic))



