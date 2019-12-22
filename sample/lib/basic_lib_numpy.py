# coding:utf-8
# 除非显示说明，否则np.array()会尝试为新建的数组推断出一个较为合适的数据类型。
# 数据类型保存在一个特殊的dtype()对象中
# 1. 一个列表的转换
import numpy as np
import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5, 6]
arr1 = np.array(data)
print(arr1)
# shape: 表示维度大小的数组; dtype：用于说明数组数据类型的对象
print("arr1.shape:{0},\narr1.dtype:{1}".format(arr1.shape, arr1.dtype))

# 2.创建多维数组：嵌套序列将会被转换成一个多维数组
data2 = [[1, 2, 3], [4, 5, 6]]
arr2 = np.array(data2)
# 可以用astype的方法显示更改数组的dtype
arr2 = arr2.astype(np.float64)
print(arr2)
print("arr2.shape:{0},\narr2.dtype:{1}".format(arr2.shape, arr2.dtype))

# 3.数组和标量之间的运算
print("=========================数组和标量之间的运算===================================")
# 大小相等的数组之间的任何算术运算都会应用到元素集
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = arr3 * arr3
print(arr4)
arr5 = arr3 - arr3
print(arr5)
# 数组和标量的运算会将那个标量传播到各个元素
arr6 = 1 + arr3
print(arr6)
arr7 = arr3 * 0.5
arr7.astype(np.float64)
print(arr7)

# 4.索引和切片
arr8 = np.arange(10)
print(arr8)
# [0 1 2 3 4 5 6 7 8 9]
# 4.1 一维数组的切片索引
print("======================一维数组的切片索引===================================")
print("arr8[4]:{0}".format(arr8[4]))
arr8_slice = arr8[3:7]
# [3 4 5 6]
print(arr8_slice)
# 当将一个标量赋值给一个切片，该值会自动传播到整个选区。
arr8[3:7] = 12
print(arr8)
# 4.2 高维数组的切片索引
# 在一个二维数元素组中，各索引位置上的元素不再是标量而是一维数组
# 可以对各个元素进行递归访问。可以传入一个以逗号隔开的索引列表来选取单个元素
print("======================高维数组的切片索引===================================")
arr9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr9)
print(arr9[1])
print(arr9[1, 2])
# 花式索引是利用整数数组进行
# empty()创建新数组，只分配内存空间，不填充任何值
print("======================花式索引===================================")
arr10 = np.empty((8, 4))
print(arr10)
for i in range(8):
    arr10[i] = i
print(arr10)
print("======================以特定的顺序选取行子集===================================")
# 为了以特定的顺序选取行子集，只需要传入一个用于指定顺序的整数列表或ndarray即可
arr10_chid = arr10[[4, 3, 0, 6]]
print(arr10_chid)
print("======================将一维数组改为二维数组===================================")
# 当一次传入多个数组时，它返回的是一个一维数组，其中的索引对应各个索引元组
arr11 = np.arange(32)
print(arr11)
# 将一维数组改为二维数组
arr12 = arr11.reshape((8, 4))
print(arr12)

# 5.数组转置和轴对称
print("======================数组转置和轴对称==================================")
arr13 = np.arange(15).reshape(5, 3)
print(arr13)
# 数组转置： 数组不仅有transpose()方法，还有一个特殊的T属性。
print(np.transpose(arr13))
print(arr13.T)
print("======================高维数组：数组转置和轴对称==================================")
arr15 = np.arange(16).reshape((2, 2, 4))
print(arr15)
# 对于高维数组，transpose()需要得到一个由轴编号组成的元组
arr16 = np.transpose(arr15, (1, 0, 2))
print(arr16)

# 6.利用数组进行数据处理
print("======================利用数组进行数据处理=================================")
# NumPy数组可以将很多数据处理任务表述为简洁的数组表达式（否循环则需要编写）
# np.meshgrid()函数接受两个一维数组，并产生两个二维矩阵(对应两个数组中所有的(x,y)对)
points = np.arange(-5, 5, 0.01)  # 1000个间隔相等的点
xs, ys = np.meshgrid(points, points)
print(ys)
print("======================公式：sqrt(x^2 + y^2)================================")
# 根据网络对函数求值的结果
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title('Image plot of % \sqrt{x^2 + y^2}$ for a grid of values')

# 7.数学和统计方法
# 用户可以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算
print("======================数学和统计方法=================================")
arr18 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr18.cumprod(1))
