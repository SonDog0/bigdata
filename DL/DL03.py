# 텐서플로 기초
# 구글에서 만든 딥러닝 오픈소스 패키지 - c++로 작성
# 코드가 복잡하고 개념이 다소 어려운 감이 있어서
# 케라스라는 추상화 도구를 이용해서 딥러닝 작업 수행함

# 다른 딥러닝 관련 패키지 : Torch , Caffe
# 텐서플로 대안으로 Torch를 추천하기도 함



import tensorflow as tf

msg = 'Hello, Tensorflow!!'
hello = tf.constant(msg)

print(hello)

# 변수와 상수를 선언하고 수식을 작성해서
# 결과를 출력하려 했지만 텐서 정보만 출력됨
# Tensor("Const:0", shape=(), dtype=string)

# 왜냐하면, 텐서플로에서는 정의시점과 실행시점이 나누어져 있기 때문

# 즉, 텐서플로에서는 모델을 구성하는 것과
# 그것을 싱행하는 것을 분리하여 프로그래밍 되어있음
# 지연실행 lazy-evaluation : 주로 함수형 프로그래밍에서 사용

sess = tf.Session() # 코드를 실행하기 위한 세션 생성
print(sess.run(hello))

# 상수 / 변수 연산
# subtract , miliply , div ,mod , abs , square , sqrt , round , exp , log ,maximum , minimum

a = tf.constant(15)
b = tf.constant(30)
c = tf.add(a,b)

print(c)
# Tensor("Add:0", shape=(), dtype=int32)
print(sess.run([a,b,c]))
# 45

#저장도 가능함
temp = sess.run([a,b,c])
print(type(temp))
print(temp[0])


# 텐서의 정의
# 텐서tensor : 다양한 수학식을 계산하기 위한 중요한 자료형
# 단일값 : scalar , 1차원 :vector , 2차원 : matrix , n차원 : tensor
# tensor는 rank와 shape으로 다양한 차원의 데이터를 표현 가능

# 문자/숫자 상수 : rank 0 , shape 0 인 텐서
# [1,2,3] : rank 1 , shape 3 인 텐서
# [[1,2,3] , [4,5,6] ] : rank 2 , shape [2,3] 인 텐서
# [[[1,2,3,] , [4,5,6]]] : rank 3 , shape [2,1,3] 인 텐서

# 텐서 생성관련 함수
# random_uniform : 균등분포에 따르는 난수 생성
# random_normal : 정규분포에 따르는 난수 생성

d = tf.Variable(tf.random_uniform([1], 0 , 10 , dtype=tf.float64 , seed = 1 ))
e = tf.Variable(tf.random_normal([1], 0 , 10 , dtype=tf.float64 , seed = 1 ))

print(d)
print(e)

# Variable 사용 할수 있게 초기화
sess.run(tf.global_variables_initializer())

print(sess.run([d,e]))



# placeholder
# 정의단계에서 변수선언만 하고
# 실행단계에서 변수에 값을 할당
f = tf.placeholder('float')
g=tf.placeholder('float')
h = tf.multiply(f,g)
print(f)

print(sess.run(h,feed_dict={f:35,g:23}))



# 작업 종료 시 close 함수 호출
sess.close()
