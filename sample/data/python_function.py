# coding:utf-8
# 定义函数的一般语法：


def greetings():
    """显示简单的问候语"""
    print("Hello World!")


def greeting(username):
    """显示简单的问候语 username-形参"""
    print("Hello {}".format(username))


def printme(strings):
    """打印任何参入的字符串"""
    print(strings)
    return


# 1.函数的调用
greetings()
# 在函数的调用代码greeting("Bob")中，值"Bob"是一个实参
greeting("Bob")
printme("我要调用用户自定义函数")
printme("再次调用同一函数")


# 2.函数的返回
def calculate_sum(arg1, arg2):
    """返回两个参数的和"""
    return arg1 + arg2


total = calculate_sum(10, 20)
print("{0}+{1}={2}".format(10, 20, total))


# 3.位置参数
def power(m, n=3):
    result = 1
    while n > 0:
        n = n - 1
        result = result * m
    return result


# 在power(m,n)中有两个参数，即m和n，这两个参数都是位置参数，在调用的时候传入的两个值按照顺序依次赋给m和n
print("4的三次方：", power(4, 3))

# 4.默认参数
print("4的三次方：", power(4))
print("4的五次方：", power(4, 5))

# 5.关键字参数
print("4的三次方：", power(n=3, m=4))


# 6.可变长度参数
def print_info(arg1, *vartuple):
    """打印任何传入的参数"""
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用print_info()函数
print_info(15)
print_info(15, 30, 45, 60)
