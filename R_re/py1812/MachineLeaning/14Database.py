# 파이썬 데이터베이스 프로그램

# AWS mariaDB : 54.180.30.113
"""
# 디버에서 작업함
create table sungjuk(
    sjno int PRIMARY key auto_increment,
	name varchar(30) not NULL,
	kor decimal(3,0) not NULL,
	eng decimal(3,0) not NULL,
	mat decimal(3,0) not NULL,
	tot decimal(3,0) default 0,
	mean decimal(4,1) DEFAULT 0.0,
	grd char(2) DEFAULT '가',
	regdate datetime default CURRENT_TIMESTAMP
);

insert into sungjuk(name,kor,eng,mat)
VALUES('kim',78,65,12);

select * from sungjuk;
"""

# 성적 데이터를  mysql의 sungjuk 테이블에 저장하는 클래스
# PyMySQL 패키지를 미리 설치해둬야 함
import pymysql

class  protoSJDAO :

    def insertSungJuk(self, sj):
        # mysql 연결객체 생성
        conn = pymysql.connect(host='54.180.30.113',
                               charset='utf8', user='kimkim',
                               password='123456', db='kimkim')
        # mysql 접속 후 커서 얻어옴
        cursor = conn.cursor()

        # 실행할 mysql 쿼리 작성
        sql = "insert into sungjuk(name,kor,eng,mat) VALUES(%s,%s,%s,%s)"

        param = (sj.name, sj.kor, sj.eng, sj.mat)

        # 쿼리 실행
        cursor.execute(sql, param)
        conn.commit()

        # mysql 연결객체 제거
        conn.close()

        # 결과출력
        print('성적 저장 완료')

    def selectSungJuk(self):
        conn = pymysql.connect(host='54.180.30.113',
                               charset='utf8', user='kimkim',
                               password='123456', db='kimkim')
        # mysql 접속 후 커서 얻어옴
        # cursor = conn.cursor()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # 실행할 mysql 쿼리 작성
        sql = " select * from sungjuk "\
            " order by sjno "

        # 질의를 실행하고 결과를 리스트형태로 저장
        cursor.execute(sql)
        rows = cursor.fetchall()   # 실행하고 결과를 받아오기 위하여 fetchall를 써야함

        # 결과 데이터를 한행씩 뽑아서 출력
        # for row in rows:
        #     # row[0],row[1],row[2],row[3]
        #     row['name'],row['kor'],row['eng'],row['mat']



        # selectSungJuk 메서드에 많은 기능이 부가
        # 기능 1 : sungjuk 테이블에서 테이더 가져오기
        # 기능 2 : 가져온 데이터들을 print()로 출력
        # 기능2는 service 클래스에서 처리하도록 변경
        # 즉, 테이블의 각 행을 sungjuk 클래스에 담아
        # 리스트 객체에 추가한 후 return 함
        sjs =[]
        for row in rows:
            # sj = SungJuk(row[0],row[1],row[2],row[3])
            sj = SungJuk(row['name'],row['kor'],row['eng'],row['mat'])
            sjs.append(sj)


        conn.close()
        # return rows     # 책임원칙에 따라 출력은 service쪽에서 한다
        return sjs

    def selectSungJukOne(self):
        pass
    def updateSungJuk(self, sj):
        pass
    def deleteSungJuk(self, sj):
        pass



class SungJuk:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def __str__(self):
        pass


# # 성적 클래스의 객체 생성
# sj = SungJuk('혜교',98,65,78)
#
psjdao = protoSJDAO()
# psjdao.insertSungJuk(sj)

# 전체 성적 데이터 화면에 출력
# psjdao.selectSungJuk()

rows = psjdao.selectSungJuk()

# for row in rows:
#     # print(row[0],row[1],row[2],row[3])
#     print(row['name'],row['kor'],row['eng'],row['mat'])

sjs = psjdao.selectSungJuk()
for sj in sjs:
    print(sj.name,sj.kor,sj.eng,sj.mat)



# emp 테이블 작성
# empid lname fname hdate sal jobid deptid mgrid
# 사원정보 : emp
# 사원정보 저장/조회 : empdao 클래스

