# 모듈 파일

def add(x,y) :
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

# 모듈 파일에 일바적인 코드를 작성하는 경우
# import 문을 호출하면 자동으로 실행됨
# 즉 , 단독으로 실행할때만 이 코드가 실행되고
# 모듈로 사용할때 이코드는 실행되면 안되어야 함
# 이러한 무네를 해겨하려면 다음과 같은 코드를 추가

if __name__ == '__main__':
    print('---')
    print('hello !')
    print('---')

