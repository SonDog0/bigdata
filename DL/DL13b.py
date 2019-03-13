# 텔레그램 봇으로 메세지 주고 받기

import json
import random


from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CommandHandler


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


# 텔레그램 챗봇 응답 처리 콜백함수
def reply_message(bot,update):
    # update.message.reply_text('응답 준비중...')
    # update.message.reply_text(update.message.text)

    text = make_sentence(word_dic)
    update.message.reply_text(text)



# 텔레그램 챗봇 도움말 콜백함수

def help_message(bot,update):
    update.message.reply_text('도움말 호출했음')


# 텔래그램 챗봇 소개 콜뱀함수


# 프로그램 실행부

mytoken = '652932835:AAFRZd1XeRtM1p-bzF8jMJ-27q9ftOWgJLI'
word_dic = json.load(open('c:Java/data/dic.json', 'r' ))

print('텔레그램 문장자동생성 봇 초기화 중...')

updater = Updater(mytoken) # 메세지 초기화

# 콜백함수 등록
# 메세지를 수신했을때 처리하는 함수 등록
message_handler = MessageHandler(Filters.text, reply_message)
updater.dispatcher.add_handler(message_handler)

# 명령을 수신했을 때 처리하는 함수 등록
help_handler = CommandHandler('help' , help_message)
updater.dispatcher.add_handler(help_handler)


print('텔레그램 문장자동생성 봇 실행 중...')

# 텔레그램 봇 서버 실행 ( 3초 주기 )
updater.start_polling(timeout=3 , clean= True)
updater.idle()


# restAPI => 웹서버가 필요없음
# 콜뱀함수 -> 계란을 삶는다 20분에 계란 잘삶아짐
# => 1. 1분마다 뚜껑열어서 계란 삶아졌는지 확인
# => 2. 타이머를 20분걸어서 뚜껑열어서 계란 삶아졌는지 확인

