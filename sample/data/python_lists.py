# coding:utf-8
cars = ["Benz", "Buick", "BMW", "Ford", "Toyota"]
print(cars)
# 将元组转化为列表
print("list转化为tuple:{0}".format(tuple(cars)))

# 访问列表第一个元素
print(cars[0])
# 访问列表的最后一个元素
print(cars[-1])
# 得到列表的长度
cars_length = len(cars)
print(cars_length)
# 列表遍历
for car in cars:
    print(car)
# 修改列表的某个元素
cars[0] = "Honda"
print(cars)

# 在列表末尾追加元素
cars.append("SUV")
cars.append("SUV")
print(cars)

# 该元素在列表中出现的个数
count = cars.count("SUV")
print("SUV元素在列表中出现的个数:{0}".format(count))

# 在指定位置插入元素
cars.insert(1, "Audi")
print(cars)

# 删除第一次出现的该元素
cars.remove("SUV")
print(cars)

# 返回最后一个元素，并从list中将其删除
car = cars.pop()
print(car)
print(cars)

# 追加cars_new，即合并cars_new到cars上
cars_new = ["BYD", "KIA"]
cars.extend(cars_new)
print(cars)

# 排序
cars.sort()
print(cars)

# 倒序
cars.reverse()
print(cars)

# 删除指定下标的元素
del cars[-1]
print(cars)

# 切片
cars_new_2 = cars[0:3]
print(cars_new_2)

# list复制  cars_new_3为cars_new_2的克隆，即另一个副本
cars_new_3 = cars_new_2[:]
print(cars_new_3)
# 删除指定下标范围的元素
del cars_new_3[:]
print(cars_new_3)

# list操作符: +  *
print([1, 2] + [3, 4])
print([2] * 4)
