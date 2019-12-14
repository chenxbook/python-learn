# coding:utf-8
# 1.类的定义与创建


class Cat(object):
    # 一次模拟小猫的简单尝试
    def __init__(self, name, age):
        # 初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小猫被命令下蹲
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # 模拟小猫被命令打滚
        print(self.name.title() + " rolled over!")


# 创建小猫的实例
# 命名规范中，首字母大写的名称指定的是类，而小写名称指的是根据类创建的实例。
my_cat = Cat(name="tommy", age=3)
# 要访问实例的属性，可以使用句号点表示
print("My cat's name is " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + " years old.")

# 类的方法调用
my_cat.roll_over()
my_cat.sit()


# 2.构造函数
# __init__(self, ...),这个方法被称为构造函数，用来初始化对象(实例)，在创建对象时调用。

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello! My name is ", self.name)


# 创建对象实例
p = Person("张三")
p.say_hi()
