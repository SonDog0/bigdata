# 소설 '토지'를 word2vec으로 워드임베딩 한 후
# 단어간 유사성 알아보기


# # sorted 함수 알아보기
# data1 = [4,3,10]
# print(sorted(data1)) # 기본 오름차순
# print(sorted(data1,reverse=True)) # 내림차순
#
# data2 = {'c' : 3 , 'a' : 4 , 'b' : 1 }
# print(sorted(data2)) # dict의 키를 기준으로 정렬
# print(sorted(data2,reverse=True))
#
# print(data2)
# print(data2.items()) # dict의 key, value 함께 출력
#
# print('\n리스트 정렬 ')
# print(sorted(data2.items()))
#
# print('\ndict의 value를 기준으로 정렬  ')
# print(sorted(data2.items() , key = lambda x:x[1], reverse= True))
# # lmabda x:x[1] => x요소 {'c' : 3 } 중 첫번째 index를 찾아냄


from konlpy.tag import Okt

text = []
with open('c:/Java/data/lands.txt','r') as f:
    docs = f.readlines()

# print(docs[:5])

# 소설 내용 중 명사만 추출해서 빈도수 측정
twitter = Okt() # 트위터 형태분석기 초기화
word_dict = {}

for doc in docs:
    words = twitter.pos(doc)
    # print('words 값 = >', words)
    # print('\n\n')
    for word in words:
        # print('word 값 = >', word[0])
        # word[0] = value
        # word[1] = 품사
        print('\n\n')
        if word[1] == 'Noun': # 단어의 품사가 명사 이라면
            if not (word[0] in word_dict): # 단어 사전에 등록되지 않은 새단어이면
                word_dict[word[0]] = 0
                # word_dict에 word[0] , 즉 단어명이 , 추가됨
                # ex )
                # word_dict['것'] = 0 -> # {'것', 0}

             # 이미 단어 사전에 등록된 단어라면
            word_dict[word[0]] += 1
            # word_dict['것'] = 1 -> # {'것', 1}
print('word_dict 값 = >' , word_dict.items())


# 빈도순으로 단어들을 내림차순 정렬
keys =sorted(word_dict.items(), key= lambda x:x[1] , reverse= True)

# 빈도가 높은 상위 50개의 단어를 출력
for word, count in keys[:50]:
    print('{0}({1})'.format(word,count), end = '')







