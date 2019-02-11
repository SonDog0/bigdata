# 이전 예제를 함수버젼으로 리팩토리

# 11번
def cheapnote(dollar, euro) :
    x = dollar*1119
    y = euro*1270
    return x,y

print(cheapnote(780,650))

# 결혼 연봉에 따라 세금 계산
def computexax(ismarried, sal):
    tax=0
    if (isMarried == 1):
        if (sal < 3000):
            tax = sal*0.1
        else :
            tax = sal*0.25
    else:
        if (sal < 6000):
            tax = sal*0.1
        else :
            tax = sal*0.25
    return isMarried, sal, tax

sal = int(input('연봉은?'))
isMarried = int(input('결혼여부는? (예:1,아니오:2)'))
print(computexax(isMarried,sal))   # 통으로 받기
a,b,c = computexax(isMarried,sal)
print(a) # 하나씩 받기
print(b) # 하나씩 받기
print(c) # 하나씩 받기




# 윤년체크
def leapyear (year):
    msg = '윤년이 아닙니다'
    if (year %4 == 0 and year %100 != 0 or year %400 == 0):
        msg = '윤년입니다'
    return year, msg

year = int(input('연도는?'))
print(leapyear(year))