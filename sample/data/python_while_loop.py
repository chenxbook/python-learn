# coding:utf-8
# while语句
number = 1
while number <= 9:
    print(number)
    number = number + 1

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers):
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print("偶数数组：", even)
print("奇数数组：", odd)
