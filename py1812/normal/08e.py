# 패키지 package
# 각 함수 , 클래스들을 용도별로 분리해서
# 작성하는 것은 모듈
# 그런데, 이러한 모듈들이 모이면 뒤죽박죽
# 모듈 집합 -> 패키지

# 파이썬에서는 패키지를 만드려면
# 디렉토리 생성 -> __init__.py 파일 생성하면됨
# py3 이상 __init__ 만들지 않아도
# 패키지로 인식

import mathutils.mathutil

sum = mathutils.mathutil.add(10,10)
print(sum)

# 함수 호출시 패키지, 모듈명을 생략하려면

from mathutils.mathutil import add

sum = add(3,'a')
print(sum)

