# coding:utf-8

# 1.集合创建
s1 = {'P', 'y', 't', 'h', 'o', 'n'}
print(type(s1))
print(s1)

# 整型的集合
s2 = {1, 2, 3}
print(s2)

# 混合类型的集合
s3 = {1.0, 'Python', (1, 2, 3)}
print(s3)

# 从列表创建
list_1 = ['P', 'y']
s4 = set(list_1)
print(s4)

# 创建空集合
s5 = set()
print(type(s5))
print(s5)

# 从字符串创建
st = "HelloWorld"
s6 = set(st)
print(s6)

# 确定性
print('H' in s6)
print('P' not in s6)

# 2.集合的运算


