# coding:utf-8
# 1.if语句
age = 19
if age >= 18:
    print("You are old enough to drive！")

# 2.if-else语句
if age > 18:
    print("You are an adult")
else:
    print("You are an underage")

# 3.if-elif-else语句
age = 40
if age < 18:
    print("You are an underage")
elif 18 <= age < 40:
    print("You are a young man.")
elif 40 <= age < 60:
    print("You are middle-aged.")
else:
    print("You are an old man.")
