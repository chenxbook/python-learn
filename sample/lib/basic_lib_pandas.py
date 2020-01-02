# coding:utf-8
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 1.Series
print("===========================1.Series======================================")
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
print("===========================2.DataFrame======================================")
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
print("===========================3.Pandas读取文件======================================")
file = pd.read_csv("hobby.csv")
print(file)
# read_table(): 从文件，URL、文件型对象中加载带有分隔符的数据，默认分割符为制表符("\t")
file2 = pd.read_table("hobby.csv", ",")
print(file2)

# 4. Pandas导出文件
print("===========================4.Pandas导出文件======================================")
# to_excel(file_path,sep='',index=True,header=True)
# @file_path 表示文件路径
# @sep表示分隔符
# @index代表是否导出行序号
# @header代表是否导出列序号
# frame2.to_excel('test.xlsx', float_format='%.5f', index=True, header=True, sheet_name='hobby1')  # float_format 控制精度

# 5. 数据处理
print("===========================5.数据处理=====================================")
data = {'Tom': [170, 26, 30],
        'Mike': [175, 25, 28],
        'Jane': [170, 26, np.nan],
        'Tim': [175, 25, 28]
        }
data1 = DataFrame(data).T;
print(data1)
print("===========================方法一:删除有缺失的值=====================================")
data2 = data1.dropna();
print(data2);
print("===========================方法二:对缺失值进行填充处理==============================")
# 采用均值填充
data3 = data1.fillna(data1.mean())
print(data3)
# 采用中位数填充
data4 = data1.fillna(data1.median())
print(data4)

# 6.层次化索引
print("===========================6.层次化索引====================================")
data = Series(np.random.randn(10), index=[
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
    [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]
])
# 带有多重索引的Series格式化输出
print(data)
print(data.index)
print("===========================选取一个数据集====================================")
print("--data['b']:\n{0}".format(data['b']))
print("--data['b':'c']:\n{0}".format(data['b':'c']))
print("--data[['b','d']]:\n{0}".format(data[['b', 'd']]))
# 可以在内层中进行选取
print("--data[:,2]:\n{0}".format(data[:, 2]));

# 层次化索引在数据重塑和基于分组的操作中扮演者重要的角色
# 一个数据可以通过它的unstack();方法被重新安排到一个DataFrame中
data1 = data.unstack();
print(data1);
# 对于一个DataFrame对象，每个轴都可以有分层索引。
df = DataFrame(np.arange(12).reshape((4, 3)),
               index=[
                   ['a', 'a', 'b', 'b'], [1, 2, 1, 2]
               ],
               columns=[
                   ['Ohio', 'Ohio', 'Colorado'], ['green', 'red', 'green']
               ]
               )
print(df)
# 各层次都可以有名字。如果指定名称，它就会显示在控制台输出中。
df.index.names = ['key1', 'key2']
df.columns.names = ['state', 'color']
print(df)
# 由于有了分部的索引，所以可以轻松地选取列分组
print("df['Ohio']:\n{0}".format(df['Ohio']))

# 7.分级顺序
print("===========================7.分级顺序====================================")
# 7.1 重新分级排序
df1 = df.swaplevel('key1', 'key2')
print(df1)
# 7.2 根据级别汇总统计
df2 = df.sum(level='key2')
print(df2)

# 8.使用DataFrame的列
print("===========================8.使用DataFrame的列====================================")

Df = DataFrame({
    'a': range(7),
    'b': range(7, 0, -1),
    'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
    'd': [0, 1, 2, 0, 1, 2, 3]
})
print(Df)
# 8.1 set_index()方法：将DataFrame的一个或多个列索引转化成行索引
df1 = Df.set_index(['c', 'd'])
print(df1)
# 8.2 reset_index()方法: 将DataFrame的行索引变成列
df2 = df1.reset_index()
print(df2)
