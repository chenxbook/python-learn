# coding:utf-8
import pandas as pd
from pandas import Series, DataFrame

# 1.Series
print("===========================Series======================================")
obj = Series([4, 7, -5, 3])
print(obj)
# Series的字符串表现形式为索引在左边，值在右边。
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64

# 可以通过Series的values和index属性获取其数组表示形式和索引对象
print("obj.values:{}".format(obj.values))
print("obj.index:{}".format(obj.index))
# 通常，需要创建的Series带有一个可以对各个数据点进行标记的索引
obj2 = Series([4, 3, -5, 7], index=['a', 'b', 'c', 'd'])
print(obj2)
# a    4
# b    3
# c   -5
# d    7
# dtype: int64
# 可以通过索引的方式获取Series中的单个或一组值
print("obj2['a']:{}".format(obj2['a']))
print("obj2[['a','d']]:\n{}".format(obj2[['a', 'd']]))

# 2.DataFrame
print("===========================DataFrame======================================")
# 直接传入一个由等长列表或NumPy数据组成的字典
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
        }
frame = DataFrame(data)
print(frame)
# 如果指定了列序列，DataFrame的列就会按照指定的顺序进行排列
print("===========================DataFrame:指定了列序列=====================================")
frame2 = DataFrame(data, columns=['year', 'state', 'pop'])
print(frame2)

# 3. Pandas读取文件
# read_csv()：从文件，URL、文件型对象中加载带有分隔符的数据，默认分割符为逗号
print("===========================Pandas读取文件======================================")
file = pd.read_csv("hobby.csv")
print(file)
# read_table(): 从文件，URL、文件型对象中加载带有分隔符的数据，默认分割符为制表符("\t")
file2 = pd.read_table("hobby.csv", ",")
print(file2)
# 4. Pandas导出文件
print("===========================Pandas导出文件======================================")
# to_excel(file_path,sep='',index=True,header=True)
# @file_path 表示文件路径
# @sep表示分隔符
# @index代表是否导出行序号
# @header代表是否导出列序号
frame2.to_excel('test.xlsx', float_format='%.5f', index=True, header=True, sheet_name='hobby1')  # float_format 控制精度
