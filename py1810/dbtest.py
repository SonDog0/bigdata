
import pymysql

# mysql connection 생성
conn = pymysql.connect(host='13.209.88.188', user= 'son', password= '931027',db='SON_MARIADB', charset='utf8')

curs = conn.cursor()
msg = [] 
# sql 질의문 실행
sql = 'select * from CRM'
curs.execute(sql)

# 결과 집합 처리
for rs in curs.fetchall():

    msg.append(rs[0])

for i in range(0,len(msg)):
    f = open('./dbtest.txt', 'a' , encoding='UTF-8')
    f.write( msg[i]+'\n')
    f.close()

#mysql connection 닫기
conn.close()


