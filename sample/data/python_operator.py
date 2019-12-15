# coding:utf-8
a = 60
b = 10
c = 0
d = 3

# 1.算术运算符
#  %取模 - 返回除法的余数
c = a % b
print("%取模-c的值为：", c)

# //取整除 - 返回商的整数部分（向下取整）
c = a // b
print("//向下取整-c 的值为：", c)

# 2.比较运算符
if a == b:
    print("a 等于 b")
else:
    print("a 不等于 b")

# 3.赋值运算符
c *= a
print("c的值为：", c)

# 4.逻辑运算
if not (a and b):
    print("变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("变量 a 和 b 都为 true")

# 5.位运算  60的二进制  0011 1100
# 十进制数60转换成二进制整数-用60除以2直到尽头。把余数倒过来就行
c = a << 2  # 240 = 1111 0000
print("左移两位，c的值为：", c)

c = a >> 2  # 15 = 0000 1111
print("右移两位，c的值为：", c)

c = ~a  # -61 = 1100 0011
print("取反，c的值为：", c)

# 6.成员运算符 in、not in

list = [1, 2, 3, 4, 5]

if a in list:
    print("变量a在给定的列表中 list 中")
else:
    print("变量a不在给定的列表中 list 中")

if b not in list:
    print("变量b不在给定的列表中list 中")
else:
    print("变量b在给定的列表中 list 中")

# 7.身份运算符
if a is b:
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if a is not b:
    print("a 和 b 没有相同的标识")
else:
    print("a 和 b 有相同的标识")

# 8.运算符优先级
e = a + (b * c) / d  # 60 + (10*0)/3
print("a + (b * c) / d 运算结果为：", e)
