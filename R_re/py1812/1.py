class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출


james = Person()
james.hello()  # Hello