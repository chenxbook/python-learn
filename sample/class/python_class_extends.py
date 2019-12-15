# coding:utf-8


# 1.创建1个Animal类
class Animal(object):
    def run(self):
        print("Animal is running...")


# 1.1. 创建Cat类继承Animal
class Cat(Animal):
    # 子类获取了父类的全部功能
    pass


# 1.2. 创建Dog类继承Animal
class Dog(Animal):
    # 用户对代码进行改进，重写覆盖了父类的run()方法
    def run(self):
        print("Dog is running...")

    # 用户可以给子类增加一些方法
    @classmethod
    def eat(cls):
        print("Eating meat...")


cat = Cat()
cat.run()
dog = Dog()
dog.run()
dog.eat()
