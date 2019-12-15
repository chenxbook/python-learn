# coding:utf-8
st = "Hello World"
# 字符串包含判断操作符: in、not in
print("He" in st)
print("She" not in st)

# 读取字符串的某一部分
print(st[:6])

# string模块提供的方法:

# 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0 ,查找不到返回-1
print(st.find('Hello') > 0)
# 首字母大写
print("字符串:{0},首字母大写:{1}".format(st, st.capitalize()))
# 转小写
print("字符串:{0},转小写:{1}".format(st, st.lower()))
# 转大写
print("字符串:{0},转大写:{1}".format(st, st.upper()))
# 大小写互换
print("字符串:{0},大小写互换:{1}".format(st, st.swapcase()))
# 将string转化为list,以空格切分
print("字符串:{0},转化为list:{1}".format(st, st.split()))

# 字符串的格式化
print("%s's height is %d cm" % ("My brother", 180))
