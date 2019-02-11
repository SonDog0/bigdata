# 패키지
# 각 함수, 클래스들을 용도별로 분리해서
# 작성하는 것을 모듈이라 했음

# 그런데, 이러한 모듈들이 모여 뒤죽박죽 섞여 있으면
# 이해도, 활용도가 떨어질 수 있음

# 따라서, 모듈들 역시 성격에 맞게 분류해서
# 관리해야 할 필요성이 대두 - 패키지를 이용해서 모듈들을 관리

# 파이썬에서는 패키지를 만드려면
# 디렉토리 생성 -> __init__.py 파일 생성하면 됨
# python3 이상에서는 __init__.py를 만들지 않아도
# 패키지로 인식 => python2오의 호환을 위해 생성할 것을 권장

# 패키지내 함수를 호출하려면
# import 패키지명.모듈명
import mathutils.mathutil
sum = mathutils.mathutil.add(10,10)
print(sum)

sum = mathutils.mathutil.add('a',10)
print(sum)

# 함수 호출시 패키지명, 모듈명 생략
# from 패키지명.모듈명 import 함수명

from mathutils.mathutil import add
sum = add('a',10)
print(sum)