
if __name__ == '__main__':
    print('---')
    print('hello !')
    print('---')

def add(x,y):
    if isinstance(x,int) == False or isinstance(y,int) == False:
        print('숫자를입력하세요')
        return
# return 만쓰면 그냥 종료 
    else:
        return x + y

