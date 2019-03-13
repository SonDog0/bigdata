# 텔렉램 봇챗 만들기
# 텔레그램은 카카오톡과 같은 유명한 인터넷 메신저 프로그램
# bot은 특정 작업을 수행하도록 고안된 자동화 프로그램
# 마치 인간이 하는 행동을 흉내내도록 만들었음
# 메신저 봇은 사람과 자동으로 대화를 하도록 디자인된 프로그램
# 봇의 활용용도는 메세지를 보내거나 채팅방의 데이터를 수집하는 등의 다양한 용도로 사용됨

# 텔레그램에 bot 추가하기
# telegram.org 에 윈도우용 telegram 다운로드 (portable 버전 사용 )

# 텔레그램 실행 -> '한국어로진행' 클릭
# BotFather 라는 대화방 추가함 -> '시작' 클릭
# /newbot -> 봇 생성 시작
# 봇 고유 이름이 생성되면 ㅔ텔레그램 인증키를 생성해 줌 (중요 ! )(

# Use this token to access the HTTP API:
# 652932835:AAFRZd1XeRtM1p-bzF8jMJ-27q9ftOWgJLI
# Keep your token secure and store it safely, it can be used by anyone to control your bot

# 생성한 봇 대화방 추가 - '시작' 클릭

# 파이썬용 텔레그램 라이브러리 설치
# pytohn-telegram-bot 패키지는
# 텔레그램을 쉽게 이용할수 있도록 지원하는
# wrapper 패키지
# 터미널에서 pip install python-telegram-bot

import telegram

mytoken = '652932835:AAFRZd1XeRtM1p-bzF8jMJ-27q9ftOWgJLI'

bot = telegram.Bot(token = mytoken)
# API 토큰키를 이용해서 봇생성

updates = bot.getUpdates()

for u in updates:
    print('메세지' , u.message)


# 메세지 응답하기
chat_id = bot.getUpdates()[-1].message.chat.id
# 가장 최근에 온 메세지의 id를 알아냄

bot.sendMessage(chat_id = chat_id , text = '하이하이, 방가방가')
# 지정한 chat_id에 메세지 전송


