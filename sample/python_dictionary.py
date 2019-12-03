# -*- coding: UTF-8 -*-
#  1.直接创建字典
d = {'one': 1, 'two': 2, 'three': 3}
print(d)
# 字典的格式化字符串
print("three is %(three)s." % d)

#  2.通过dict()创建字典
items = [('one', 1), ('two', 2), ('three', 3)]
d2 = dict(items)
print(d2)

# 3.通过关键字创建字典
d3 = dict(one=1, two=2, three=3)
print(d3)
print(d3['one'])
print(d3['three'])

# 3.1 获取指定键的值，若值不存在，返回默认值
print("获取指定键的值-D.get(key,default):{0}".format(d3.get('four', 0)))
# 3.2  返回字典键的列表
print("返回字典键的列表-D.keys():{0}".format(d3.keys()))
# 3.3 返回字典值的列表
print("返回字典值列表-D.values():{0}".format(d3.values()))
# 3.4 返回字典项的列表
print("返回字典项列表-D.items():{0}".format(d3.items()))
# 3.5 增加合并字典
d4 = dict(four=4, five=5, six=6)
d3.update(d4)
print("增加合并字典-D.update(dict2):{0}".format(d3))
# 3.6 返回并删除字典中的最后一对键和值
print("得到一个pair,并从字典中删除它，若已空则跑出异常-D.popitem():{0}".format(d3.popitem()))
# 3.7 复制字典，克隆，即另一个版本
d4 = d3.copy()
print("复制字典-D.copy():{0}".format(d4))
#  3.8 清空字典
d3.clear()
print("清空字典-D.clear():{0}".format(d3))

fruit_dict = {'苹果': "apple", "香蕉": "banana", "梨": "pear"}
#  将字典转换为元组
fruit_1_keys = tuple(fruit_dict)
fruit_1_values = tuple(fruit_dict.values())
print("将字典的key转换为元组-tuple(fruit_dict)：{0}".format(fruit_1_keys))
print("将字典的value转换为元组-tuple(fruit_dict)：{0}".format(fruit_1_values))
#  将字典转换为列表
fruit_2_keys = list(fruit_dict)
fruit_2_values = list(fruit_dict.values())
print("将字典的key转换为列表-list(fruit_dict)：{0}".format(fruit_2_keys))
print("将字典的value转换为列表-list(fruit_dict)：{0}".format(fruit_2_values))
