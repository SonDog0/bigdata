import csv

ins = open('c:/Java/data/cyluse2017.csv', 'r', encoding='utf-8')

rdr = csv.reader(ins, delimiter=',')

mainz = []
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
a10 = []
a11 = []
a12 = []

kkd = []
for line in rdr:
    kkc = str(line).replace('[', '')
    kkc = str(kkc).replace(']', '')
    kkc = str(kkc).replace("'", '')
    kkc = str(kkc).replace("'", '')

    kkd = kkc.split(',')

    a1.append(kkd[0])
    a2.append(kkd[1])
    a3.append(kkd[2])
    a4.append(kkd[3])
    a5.append(kkd[4])
    a6.append(kkd[5])
    a7.append(kkd[6])
    a8.append(kkd[7])
    a9.append(kkd[8])
    a10.append(kkd[9])
    a11.append(kkd[10])
    a12.append(kkd[11])

ins.close()

kkd = []
for liss in range(len(a1)):
    print(a1[liss], a2[liss])



#goodsQuestForm > ul > li:nth-child(2) > div.txt_qna.qustion > div > p > span