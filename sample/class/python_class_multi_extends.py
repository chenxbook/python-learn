# coding:utf-8
# 用户不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以构造出所需要的子类。
# Mixin的目的就是给一个类增加多个功能，在设计时可以优先考虑多重继承来组合多个Mixin的功能。
# 通过组合，用户可以创造出合适的服务。

# 将动物划分为哺乳类 和 鸟类
# 鸟类：能跑的鸟类，能飞的鸟类
# 哺乳类：能跑的哺乳类，能飞的哺乳类。


# 1.创建1个Animal类
class Animal(object):
    pass


# 大类-哺乳类
class Mammal(Animal):
    pass


# 大类-鸟类
class Bird(Animal):
    pass


# 跑功能
class RunnableMixin(object):
    @classmethod
    def run(cls):
        print("Running...")


#  飞功能
class FlyableMixin(object):
    @classmethod
    def fly(cls):
        print("Flying...")


# 狗
class Dog(Animal, RunnableMixin):
    pass


# 蝙蝠
class Bat(Animal, FlyableMixin):
    pass


dog = Dog()
dog.run()

bat = Bat()
bat.fly()
