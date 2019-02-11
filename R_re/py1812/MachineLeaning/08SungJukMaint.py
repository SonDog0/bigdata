from sungjuk.SungJukService import SungJukService
from sungjuk.Student import Student

sjsrv = SungJukService()

sj1 = sjsrv.readSungJuk()
sjsrv.computeSungJuk(sj1)

sjsrv.printSungJu(sj1)
print(sj1)


