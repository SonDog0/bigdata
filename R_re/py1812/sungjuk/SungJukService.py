#성적 처리 서비스 클래스
from sungjuk.Student import Student
class SungJukService:
    def readSungJuk(self):
        #성적데이터 입력받은후 성적 클래스 객체로 생성
        name = input('이름은?')
        kor = int(input('국어는?'))
        eng = int(input('영어는?'))
        mat = int(input('수학은?'))
        return  Student(name,kor,eng,mat)

    def computeSungJuk(self,std):
        #총점 편귱 학점 계산
        std.tot = std.kor + std.eng + std.mat
        std.mean = std.tot / 3
        std.grd = '가'
        if std.mean >= 90:
            std.grd = '수'
        elif std.mean >= 80:
            std.grd = '우'
        elif std.mean >= 70:
            std.grd = '미'
        elif std.mean >= 60:
            std.grd = '양'

    def printSungJuk(self,std):
        msg = "%s %d %d %s" % (std.name,std.tot,std.mean,std.grd)
        print(msg)

    def saveSungJuk(self):  # DB에 성적 저장
        pass

    def readOneSungJuk(self):  # 성적조회
        pass

    def readAllSungJuk(self):  # 모든 성적 조회
        pass

    def modifySungJuk(self):  # 성적 수정
        pass
    def removeSungJuk(self):  # 성적 삭제
        pass
