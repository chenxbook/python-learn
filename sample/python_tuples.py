# coding:utf-8
tup1 = ('physics', 'chemistry', 1997, 2000)
print(tup1)
# 将元组转化为列表
print("tuple转化为list:{0}".format(list(tup1)))
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup2 = ('2008',)
print(tup2)
# 元组与列表类似，下标索引从0开始，可以进行截取，组合等。
print("tup1[2]:{0}".format(tup1[2]))
# 切片
print("tup1[0:2]:{0}".format(tup1[0:2]))

# 逆转元组元素
print(tup1[::-1])
# 连接
tup3 = tup1 + tup2
print(tup3)
# 重复
print(tup3 * 3)
