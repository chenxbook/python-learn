# coding:utf-8
A = set('abcd')
B = set('cdef')
# 1.子集
# 子集为某个集合中一部分集合，使用操作符"<"执行子集操作，也可以使用issubset()方法完成
C = set('ab')
print("C是否为A的子集:{}".format(C < A))
print("C是否为B的子集:{}".format(C.issubset(B)))

# 2.并集
# 一组集合的并集是这些集合的所有元素构成的集合，而不包含其他元素。
# 使用操作符"|"执行并集操作，也可以使用union()方法完成。
print("A与B的并集:{}".format(A | B))
print("A与B的并集:{}".format(A.union(B)))

# 3.交集
# 两个集合A和集合B的交集是含有既属于A又属于B的元素但没有其他元素的集合。
# 使用操作符"&"执行交集操作，也可以使用intersection()方法完成。
print("A与B的交集:{}".format(A & B))
print("A与B的交集:{}".format(A.intersection(B)))

# 4.差集
# A与B的差集是所有属于A但不属于B的元素构成的集合
# 使用操作符"-"执行差集操作，也可以使用difference()方法完成
print("A与B的差集:{}".format(A - B))
print("A与B的差集:{}".format(A.difference(B)))

# 5.对称差
# 两个集合的对称差是只属于其中一个集合，而不属于另一个集合的元素组成的集合。
# 使用操作符"^"执行对称差操作，也可以使用symmetric_difference()方法来完成。
print("A与B的对称差:{}".format(A ^ B))
print("A与B的对称差:{}".format(A.symmetric_difference(B)))

# 6.更改集合
# add()添加单个元素
s = {'P', 'y'}
s.add('t')
print("add()添加单个元素:{}".format(s))
# update()方法添加多个元素，可以使用元组、列表、字符串或其他集合作为参数
s.update(['o', 'n'])
# 添加列表和集合
s.update(['H', 'E'], {'L', 'M', 'O'})
print("update()添加多个元素:{}".format(s))

# 7.删除元素
# discard() ：若集合中不存在指定的元素，使用discard（）结果保持不变
s.discard('E')
print("discard()去掉一个存在的元素:{}".format(s))
s.discard('S')
print("discard()去掉一个不存在的元素:{}".format(s))
# remove() : 若集合中不存在指定的元素，使用remove()会引发KeyError
s.remove('O')
print("remove()去掉一个存在的元素:{}".format(s))

# 8.清空集合
s.clear()
print("clear()清空集合:{}".format(s))
