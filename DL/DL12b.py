# 마르코프 체인을 이용해서
# 채팅 봇을 만들어 봄

import json , random

def word_choice(sel):
    keys = sel.keys()
    sel_word = random.choice(list(keys))
    print(keys)
    print(sel_word)
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

    # print(w1,w2,w3)




# 사전 파일 읽어
word_dic = json.load(open('c:/java/data/dic.json' , 'r', encoding= 'utf-8'))


# print(word_dic)


# 사전에 존재하는 단어 중
# 한 단어 입력시 관련 어구 출력
# print(word_dic['저'])
# print(word_dic['개도'])
# print(word_dic['수지'])


# 자동 문장 생성

print(make_sentence(word_dic))
print(make_sentence(word_dic))
print(make_sentence(word_dic))

