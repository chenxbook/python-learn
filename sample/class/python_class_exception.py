# coding:utf-8
import random

# 视图打开一个不存在的文件，运行之后跑出FileNotFoundError异常
# fr = open("/not there", "r")

# 1.Python中捕获与处理异常

# 1.1 try-except语句中的使用

try:
    fr = open("/not there", "r")
except FileNotFoundError:
    print("This file is not exist！")

# 1.2 try-except-else语句的使用
a = 1
b = 2
c = "1"
try:
    assert a < b
    d = a + b
except AssertionError as e:
    print("a<b")
except TypeError as e:
    print(e)

else:
    print("Program execution successful")

# 在以上代码块中，尝试捕获两个异常，分别是 AssertionError异常 和 TypeError异常。
# 但是，程序运行顺利，没有发生异常，所以执行else语句。

# 猜数字游戏: 随机取1～10中的任意一个数字，然后让游戏者猜。
num = random.randint(1, 10)
while True:
    try:
        guess = int(input('Please  enter  1～10 :'))
    except Exception as e:
        print(e)
        print("Input error! Please enter num : 1～10 ")
        continue
    if guess > num:
        print("guess Bigger:", guess)
    elif guess < num:
        print("guess Smaller:", guess)
    else:
        print("Great，you guess correct. game over!")
        break


# 2.自定义异常类
# 自定义一个名为ShortInputException的异常类，其用来判断用户输入的字符串长度是否满足大于或等于3要求。

class ShortInputException(Exception):
    def __init__(self, length, at_least):
        Exception.__init__(self)
        self.length = length
        self.at_least = at_least


try:
    s = input('Enter something')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
    else:
        print(s)
except ShortInputException as ex:
    print('ShortInputException: The input was length %d, but was expecting at least %d .' % (ex.length, ex.at_least))
else:
    print("No exception was raised.")
