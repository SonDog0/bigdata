# Tensorflow Interactive Session

# 일반적인 tensorflow Session과 차이점은
# run() 함수를 따로 사용하지 않아도 된다는 점
# 즉 , 코드를 실행하기 위해 Session 객체를

# 명시적으로 사용하지 않아도 됨
# 단 run() -> eval()로 대신함

# 한편, 일반적인 Tensorflow Session 에서도
# Session 객체를 명시적으로 사용하고 싶지 않다면
# with Session문을 사용하면 됨

import tensorflow as tf

sess = tf.InteractiveSession()
# 대화형 쉘처럼 텐서플로세션 생성

msg = 'HEllo, TensorFlow!!'
hello = tf.constant(msg)

print(hello.eval())


sess.close()


sess = tf.InteractiveSession()
msg = 'Hello, again, Tensorflow!!'
hello = tf.constant(msg)

with tf.Session():
    print(hello.eval())


# InteractiveSession 예제 1
sess = tf.InteractiveSession()
x = tf.constant([[1,2]]) # 2차원 텐서
neg_x = tf.negative(x) # 음수 변환

print(neg_x.eval())
sess.close()

# InteractiveSession 예제 2
data = [-1 , 2 , 8 , -1, 0 , 5 ,5.5 , 6 , 13 ]
is5greater = tf.Variable(False) # 논리값 변수
is5greater.initializer.run() # 변수초기화

# i와 i-1 번째 변수의 차가 5이상이면 True를 출력
for i in range (1, len(data)):
    if abs(data[i] - data[i-1]) >= 5:
        tf.assign(is5greater,True).eval()
    else:
        tf.assign(is5greater, False).eval()

    print(data[i] , data[i-1] ,is5greater.eval())

sess.close()