# 튜플
# 리스트와 비슷한 자료형이지만
# 리스트는 []를 사용하지만, 튜플은 () 사용
# 튜플은 삭제, 수정이 불가능


tuple1=()
tuple2=(1,2,3,4,5)     # (1,2,3,4,5,)처럼 써도 문제 없음
tuple3=('a','b','c','d','e')
tuple4=(1,2,3,'a','b','c')

print(tuple2, tuple4)

# 튜플 삭제나 수정해보기
# tuple1.append(1)   # 추가불가
# tuple2[2] = 100    # 수정불가
# del(tuple4[3])     # 삭제불가
del(tuple1)          # 튜플을 통체로 삭제하는건 가능

jumin=(1,2,3,4,5,6,1,2,3,4,5,6,7)
if jumin[6] == 1 : print('남')
else : print('여')

print(jumin[0:6])

# 만일, 튜플의 요소를 변경해야 한다면?
jumin = list(jumin)   # 튜플을 리스트로 변환
jumin[6] = 9          # 요소 변경
jumin = tuple(jumin)
print(jumin)