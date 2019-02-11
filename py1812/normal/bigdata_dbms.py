import pymysql
import csv



# filein = open('data/P_row_utf-8.csv', 'r', encoding='utf-8')
# rdr = csv.reader(filein)
# tmp = []
# for line in rdr:
#     # print(line)
#     tmp.append(line)
# filein.close()
# print('\r\n')
#
# print(tmp[0])



filein = open('data/hello01.csv', 'r', encoding='utf-8')
rdr = csv.reader(filein)
tmp = []
for line in rdr:
    print(line)
    tmp.append(line)
filein.close()
print('\r\n')
print(tmp[0][0])



# mysql connection 생성
conn = pymysql.connect(host='13.209.88.188', user= 'son', password= '931027',db='SON_MARIADB', charset='utf8')

curs = conn.cursor()


# sql 질의문 실행
sql = 'insert into r_row values(%s,%s,%s,%s)'
for i in range(0,3):
    curs.execute(sql,(tmp[i][0],tmp[i][1],tmp[i][2],tmp[i][3]))

conn.commit()

sql = 'select count(rownum) from r_row'
curs.execute(sql)



# 결과 집합 처리
# for rs in curs.fetchall():
#     print(rs[0], rs[1], rs[2], rs[3])  #배열 기반 커서




#mysql connection 닫기
conn.close()
