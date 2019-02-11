# 2번
name = '김성열'
weight = 83
age = 28

print(name,weight,age)

# 3번
x=1;y=2; z=3

3*x; 3*x+y; (x+y)/7; (3*x +y)/(z+2)

# 4번
x,y = 4,8
print(x,y)
x *= y
print(x,y)
x -= y
print(x,y)

# 5번
x=3
print(x+7==10)

# 6번
(-32 + 95) * 12/3
a = (3*4-((-27+67)/4))
print(a,a**8)

print(99 != 10**2 -1)


# 7번
x = 2.5; y=-1.5; m=18; n=4

# 8번
a = 2.5*3/27; b=4*2/30
print(a >= b)

# 9번
# 논리연산의 우선순위 : not > and > or

print( (4<6) or True and False or False and (2>3))


# 10번
# 이윤율 = 잉여가치액 / (고정 + 가변)
benifit = 45/(30+15)

# 11번
# 780달라 or 650 유롷
# 1달라 : 1129.6
# 1유로 : 1280.7

print(780*1129.6 >= 650*1280.7) # 유로로 사는게 이득

# 12번
outer = 3.14*100
inner = 3.14*95
print(outer - inner)

# 13번
# 잘못된 문장 찾기
print("//hello there"+'9')
print()
print

# 14번 - shortcut - circuit

# 15번
print( 27/13 +4.0,
       42.7%3 + 18,
       ((3<4) and 5/8) # 안됨
       ,'a'+'b',
       )

# 16번 증가 /감소 연산자 : 파이썬에서는 안먹힘
n=3; ++n
print("n ==",n)

# 17번 input으로 들어오는 숫자는 문자로 취급 - 형변환 필요
x= int(input('첫번째 정수 입력\n'))
y= int(input('두번째 정수 입력\n'))

print('%d + %d = %d' % (x,y,x+y))
print('%d - %d = %d' % (x,y,x-y))
print('%d * %d = %d' % (x,y,x*y))
print('%d / %d = %d' % (x,y,x/y))

