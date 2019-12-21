# coding:utf-8
assert 1 == 1
assert len(["Hello World", "12"]) < 10

# 通过try-except捕获断言失败异常
try:
    assert 4 == 1 * 3
except AssertionError as e:
    print("The expression symbol is wrong!")
