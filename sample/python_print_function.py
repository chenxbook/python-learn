# coding:utf-8
# format函数格式化输出
str = "Hello World"
length = len(str)
print("字符串{0}的长度是:{1}".format(str, length))

data = ["Xiaoming", 20]
print("{0[0]} is {0[1]} years old.".format(data))

# 输出时自定义间隔符
print('hello', 'world', sep=",")

# 输出时自定义结束符
print('hello', 'world', end=".")


