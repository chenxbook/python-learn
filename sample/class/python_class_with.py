# coding:utf-8
# with语句
# 需求1：文件处理，用户需要获取一个文件句柄，从文件中读取数据，然后关闭数据
with open("text.txt") as f:
    data = f.read()
# 使用了with语句，不需要try-finally语句来确保文件对象的关闭。因为无论程序是否出现异常，文件对象都将被系统关闭。
