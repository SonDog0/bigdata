# 성적 데이터를 mysql의 sungjuk 테이블에 저장하는 클래스
import pymysql

class protoSJDAO:

    def insertSungJuk(self,sj):
        conn = pymysql.connect(host = '13.209.88.188' , user = 'son' , password = '931027', db = 'SON_MARIADB', charset= 'utf8')

        # mysql 접속후 커서 얻어옴
        cursor = conn.cursor()

        # 실행할 mysql 쿼리 작성
        sql = " insert into sungjuk(name, kor ,eng , mat) VALUES( %s, %s , %s ,%s)"

        param =(sj.name, sj.kor, sj.eng , sj.mat)

        # 쿼리 실행
        cursor.execute(sql,param)
        conn.commit()

        # 연결객체 제거
        conn.close()

        print('성적 데이터 저장되었습니다.')

        pass

    def selectSungjuk(self):
        conn = pymysql.connect(host = '13.209.88.188' , user = 'son' , password = '931027', db = 'SON_MARIADB', charset= 'utf8')

        # mysql 접속후 커서 얻어옴
        cursor = conn.cursor()

        # 실행할 mysql 쿼리 작성
        sql = ' select * from sungjuk order by sjno '

        # 쿼리 실행
        # 결과를 리스트로 가져옴
        cursor.execute(sql)

        rows = cursor.fetchall()


        # 결과데이터를 한행씩 뽑아서 출력
        # for row in rows:
        #     print(row[0],row[1],row[2],row[3])
        #     # print(row['name'], row['kor'], row['eng'], row['mat'])


        # 연결객체 제거
        conn.close()
        return rows


    def selectSungjukOne(self,name):
        pass

    def updateSungjuk(self,sj):
        pass

    def deleteSungjuk(self,sj):
        pass


class SungJuk:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat


    def __str__(self):
        pass


# 성적 클래스 객체 생성
sj = SungJuk('혜교',99,65,78)

psjdao = protoSJDAO()
# psjdao.insertSungJuk(sj)
rows = psjdao.selectSungjuk()

for row in rows:
    print(row[0] , row[1],row[2] ,row[3],row[4],row[5])