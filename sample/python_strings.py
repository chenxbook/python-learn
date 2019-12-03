# coding:utf-8
str = "Hello World"
# 字符串包含判断操作符: in、not in
print("He" in str)
print("She" not in str)

# 读取字符串的某一部分
print(str[:6])

# string模块提供的方法:

# 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0 ,查找不到返回-1
print(str.find('Hello') > 0)
# 首字母大写
print("字符串:{0},首字母大写:{1}".format(str, str.capitalize()))
# 转小写
print("字符串:{0},转小写:{1}".format(str, str.lower()))
# 转大写
print("字符串:{0},转大写:{1}".format(str, str.upper()))
# 大小写互换
print("字符串:{0},大小写互换:{1}".format(str, str.swapcase()))
# 将string转化为list,以空格切分
print("字符串:{0},转化为list:{1}".format(str, str.split()))

# 字符串的格式化
print("%s's height is %d cm" % ("My brother", 180))
