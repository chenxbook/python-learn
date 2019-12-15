# coding:utf-8
# Python内置的range函数可以迭代地生成一组数字序列
for number in range(10):
    print(number)

# len函数用于获取一个数组的长度，将range函数与len函数相组合，就可以实现遍历数组的功能
array = ['a', 'b', 'c', 'd', 'e']
for index in range(len(array)):
    print(index, array[index])
