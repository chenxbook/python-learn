# coding:utf-8
# 1.类方法的调用


class Cat:
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
# 类的方法调用
my_cat.roll_over()
my_cat.sit()

# 2.类方法
# 类对象所拥有的方法，需要用修饰器@classmethod来标识，类方法，可以通过实例对象和类对象去访问。
print("===============================类方法==================================")


class People:
    country = "China"

    @classmethod
    def get_country(cls):  # 类方法
        return cls.country


people = People()
print("通过实例对象访问，country:{}".format(people.get_country()))
print("通过类对象访问，country:{}".format(People.get_country()))

# 3.实例方法
# 不能通过 类对象引用实例方法
print("===============================实例方法===================================")


class InstanceMethod(object):
    def __init__(self, a):
        self.a = a

    def f1(self):
        print("This is {}".format(self))

    def f2(self):
        print("This is {}".format(self.a))


a = "book"
instanceMethod = InstanceMethod(a)
instanceMethod.f1()
instanceMethod.f2()

# 4.静态方法
print("===============================静态方法====================================")


class MathUtil(object):
    @staticmethod
    def sum(arg1, arg2):
        """计算两个数之和"""
        return arg1 + arg2

    @staticmethod
    def print_call_log():
        print("方法已经执行!")


# 调用类的静态方法
result = MathUtil.sum(10, 20)
print("10+20={}".format(result))
MathUtil.print_call_log()

# 5.析构函数
print("===============================析构函数=====================================")


class Test:
    def __init__(self):
        print("初始化构造器")

    def __del__(self):
        print("调用析构函数")

    def test(self):
        print("调用测试方法")


obj = Test()
# obj.test()
# 如果要显示地调用析构函数，可以使用del关键字，方式：del  对象名
del obj
