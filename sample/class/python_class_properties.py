# coding:utf-8
# 1.类属性和实例属性


class Cat:
    # 一次模拟小猫的简单尝试

    # 增加类属性
    Reproduction_way = "Viviparous"  # 生育后代的方式
    Song_way = "meow,meow"  # 叫声

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
# 访问类的属性
print("小猫的叫声: " + my_cat.Song_way + ".")

# 类的方法调用
my_cat.roll_over()
my_cat.sit()


# 私有属性与私有方法
class Secret:
    __token = "QWE123456"

    def __unaccessible(self):
        print("Sorry,you can not accessible...")

    def accessible(self):
        print("Yes,you can accessible,and the secret is ...")


secret = Secret()
# secret.__token  私有属性无法从外界进行访问
# secret.__unaccessible() 私有方法无法从外界进行访问
secret.accessible()

# 若需要访问私有属性，可以通过"对象名._类名__私有成员名"进行访问
token = secret._Secret__token
print("token值为:", token)
secret._Secret__unaccessible()
