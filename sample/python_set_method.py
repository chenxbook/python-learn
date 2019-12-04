# coding:utf-8
# 使用dir()查看方法列表:
print("使用dir()查看方法列表:{}".format(dir(set)))

s = {'Good', 'Bye', 'Tina'}
# len()返回集合的长度
print("len()返回集合的长度:{}".format(len(s)))
# max()返回集合中最大项
print("max()返回集合中最大项{}".format(max(s)))
# sorted()从集合中的元素返回新的排序列表(不排序集合本身)
print("sorted()从集合中的元素返回新的排序列表:{}".format(sorted(s)))
# sum()返回集合中的所有元素之和
s1 = {1, 2, 5}
print("sum()返回集合中的所有元素之和:{}".format(sum(s1)))
