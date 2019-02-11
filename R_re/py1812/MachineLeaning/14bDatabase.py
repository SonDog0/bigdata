# 파이썬 데이터베이스 프로그램

# 성적 데이터를  mysql의 sungjuk 테이블에 저장하는 클래스
# PyMySQL 패키지를 미리 설치해둬야 함
import pymysql

class  protoSJDAO :

    insertsql = "insert into sungjuk(name,kor,eng,mat) VALUES(%s,%s,%s,%s)"
    selectsql = " select sjno,name,kor,eng,mat from sungjuk order by sjno "
    selectOnesql = " select sjno,name,kor,eng,mat from sungjuk where name =%s order by sjno "
    updatesql = " update sungjuk set name = %s, kor = %s, eng = %s, mat = %s where sjno = %s "
    deletesql = " delete from sungjuk where sjno = %s "

    # mysql 연결, 해제 관련 함수 정의
    def makeConn(self):
        conn = pymysql.connect(host='54.180.30.113',
                               charset='utf8', user='kimkim',
                               password='123456', db='kimkim')
        return conn
    def closeConn(self, conn):
        conn.close()

    def insertSungJuk(self, sj):
        # mysql 연결객체 생성
        conn = self.makeConn()
        # mysql 접속 후 커서 얻어옴
        cursor = conn.cursor()

        param = (sj.name, sj.kor, sj.eng, sj.mat)

        # 쿼리 실행
        cursor.execute(self.insertsql, param)
        conn.commit()

        # mysql 연결객체 제거
        self.closeConn(conn)

        # 결과출력
        print('성적 저장 완료')

    def selectSungJuk(self):
        conn = self.makeConn()
        # cursor = conn.cursor()
        cursor = conn.cursor(pymysql.cursors.DictCursor)


        # 질의를 실행하고 결과를 리스트형태로 저장
        cursor.execute(self.selectsql)
        rows = cursor.fetchall()   # 실행하고 결과를 받아오기 위하여 fetchall를 써야함

        # 전체 성적 데이터 출력
        sjs =[]
        for row in rows:
            # sj = SungJuk(row[0],row[1],row[2],row[3])
            sj = SungJuk(row['name'],row['kor'],row['eng'],row['mat'])
            sj.sjno = row['sjno']      # 학생번호 저장
            sjs.append(sj)

        self.closeConn(conn)
        return sjs

    def selectSungJukOne(self, name):
        conn = self.makeConn()
        cursor = conn.cursor(pymysql.cursors.SSDictCursor)
        param = (name)
        cursor.execute(self.selectOnesql, param)
        rows = cursor.fetchall()

        for row in rows:
            sj = SungJuk(row['name'],row['kor'],row['eng'],row['mat'])
            sj.sjno = row['sjno']
        self.closeConn(conn)

        return sj




    def updateSungJuk(self, sj):
        conn = self.makeConn()
        cursor = conn.cursor()
        param = (sj.name, sj.kor, sj.eng, sj.mat, sj.sjno)
        cursor.execute(self.updatesql, param)
        print('수정된 데이터 수', cursor.rowcount)
        conn.commit()
        self.closeConn(conn)

    def deleteSungJuk(self, sjno):
        conn = self.makeConn()
        cursor = conn.cursor()
        param = (sjno)
        cursor.execute(self.deletesql,param)
        conn.commit()
        print('삭제된 데이터 수', cursor.rowcount)
        self.closeConn(conn)




class SungJuk:
    def __init__(self,name,kor,eng,mat):
        self.sjno = 0       # 학생번호 추가
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def __str__(self):
        pass


# # 성적 클래스의 객체 생성
psjdao = protoSJDAO()
#sj = SungJuk('혜교',98,65,78)
#
#psjdao.insertSungJuk(sj)

# 전체 성적 데이터 화면에 출력
sjs = psjdao.selectSungJuk()
for sj in sjs:
    print(sj.sjno,sj.name,sj.kor,sj.eng,sj.mat)

# 특정 학생 성적 데이터 출력
sj = psjdao.selectSungJukOne('혜교')
print(sj.sjno,sj.name,sj.kor,sj.eng,sj.mat)

# 수정하기
sj = SungJuk('아이유',99,98,99)   # 수정될 학생정보
sj.sjno=2                        # 수정할 학생번호
psjdao.updateSungJuk(sj)         # 변화가 없으면 수정된 데이터로 취급되지 않음

# 학생번호로 삭제하기
psjdao.deleteSungJuk(5)