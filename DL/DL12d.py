# 채팅봇 만들기

import json,random
from konlpy.tag import Okt


def word_choice(sel):
    keys = sel.keys()
    sel_word = random.choice(list(keys))
    return sel_word


def make_sentence(word):
    if not word in word_dic: return '' # 사전에 없는 단어면 공백 출력
    ret = []  # 자동 생성한 문장 저장용 변수
    if word != '@' : ret.append(word)

    top = word_dic[word] # 입력한 단어를 시작으로 해서
    w1 = word_choice(top) # 첫번째 단어 자동 선택
    w2 = word_choice(top[w1]) # 두번째 단어 자동 선택
    ret.append(w1)
    ret.append(w2)

    while True:
        if w1 in word_dic and w2 in word_dic[w1] :
            w3 = word_choice(word_dic[w1][w2])
        else: w3 = ''
        ret.append(w3)

        if w3 == '.' or w3 == '?' or w3 == '': break
        w1,w2 = w2,w3 # 생성된 이전 단어를 자리 이동
    ret = ' '.join(ret)
    return ret

    print('=>',w1,w2,w3)


def make_reply(text):
    twitter = Okt()

    if not text[-1] in ['.','?']: text += '.' # 문장끝에 마침표가 없으면 마침표를 추가해 줌
    # print(text)

    words = twitter.pos(text)
    for word in words:
        face = word[0]
        if face in word_dic: # 사전에 존재하는 단어라면
            return make_sentence(face) # 그것으로 문장생성
    return make_sentence('@')
    #사전에 존재하지 않는 단어는 임의의 문장 생성


    # 사전에 등록되어있지 않은 단어는 사전에 등록
    # register_dic(words)



# 사전 파일 읽어 오기
word_dic = json.load(open('c:/java/data/dic.json', 'r', encoding='utf-8'))

# 응답 확인하기
print(make_reply('안녕하세요'))
print(make_reply('개'))
print(make_reply('멍멍'))
print(make_reply('하이'))

