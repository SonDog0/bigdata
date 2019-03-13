import pandas as pd
import matplotlib.pyplot as plt

# # 막대 그래프를 이용해서 각 변수별 생존자 알아보기
# # 성별 생존자 현황
# survived = train[train['survived'] == 1]['sex'].value_counts()
# dead = train[train['survived'] == 0]['sex'].value_counts()
#
# df = pd.DataFrame([survived, dead])
# df.index = ['survived','dead']
# df.plot(kind='bar', stacked=True, figsize=(10,5))
# # df.plot(kind='bar', stacked=False, figsize=(10,5))


son  = pd.read_csv('c:/java/ddrdata/plot.csv')

vec_x = []
vec_y = []
temp = []
x_val = son.iloc[:,0]
y_val = son.iloc[:,1]


for i in range(0,len(x_val)):
    vec_x.append(x_val[i])

print(len(x_val))

for i in range(0,len(y_val)):
    vec_y.append(y_val[i])

print(vec_x)


# plt.plot(x_val,y_val,'ro')

plt.show()






# 기본 산점도
# x = np.linspace(0,10,50)
# y = np.sin(x)
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(x,y)
# plt.show()





