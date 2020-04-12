# coding:utf-8


import random

# 应用实例：文本文件的操作

# 示例1：先生成1~122的随机数，再产生字符对应的ASCII码，然后将满足大写字母、小写字母、数字和一些特殊符号（例如：'\n', '\r', '*', '&', '^', '$'）
#       条件的字符逐一写进test.txt中，当光标到达10001时停止写入。
with open('test.txt', 'w') as f:
    while 1:
        # 在python中的random.randint(a,b)用于生成一个copy指定范围内的整数。其中参数a是下限，参数b是上限，生成度的随机数n: a <= n <= b。
        i = random.randint(1, 122)
        x = chr(i)
        if x.isupper() or x.islower() or x.isdigit() or x in ['\n', '\r', '*', '&', '^', '$']:
            f.write(x)
        if f.tell() > 10000:
            break

# 示例2：逐个字节输出test.txt文件中的前100个字节字符和后100个字节字符。
with open('test.txt', 'r') as f:
    print(f.read(100))
    f.seek(9900)  # 将光标移动到倒数第9900的位置
    print(f.read())

# 示例3：逐行输出test.txt文件中的所有字符。
with open('test.txt', 'r') as f:
    for line in f:
        print(line)

# 示例4：复制test.txt文件中的文本数据，生成一个新的文本文件。
f = open('test.txt', 'r')
g = open('test1.txt', 'w')
for contents in f:
    g.write(contents)
f.close()
g.close()

# 示例5：统计test.txt文件中大写字母、小写字母、数字出现的频率
with open('test.txt', 'r') as f:
    u = 0
    l = 0
    d = 0
    for line in f.readlines():
        for content in line:
            if content.isupper():
                u += 1
            elif content.islower():
                l += 1
            elif content.isdigit():
                d += 1
print('大写字母有%d个,小写字母有%d个,数字有%d个' % (u, l, d))