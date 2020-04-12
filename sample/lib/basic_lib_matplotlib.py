# coding:utf-8
# Matplotlib可以通过绘图帮助用户找出异常值，进行必要的数据转化，得出有关模型的idea。
# Matplotlib是数据分析重要的可视化工具。
# python中用matplotlib画多幅图时出现图形部分重叠的解决方案
# https://blog.csdn.net/ymznice/article/details/83274600

# 1.  figure和subplot
# Matplotlib的图像都位于figure中，可以用plt.figure()创建一个新的figure。
# 使用plt.subplot()创建一个或多个subplot才能绘图。
import numpy as np
import numpy.random as random
import matplotlib
import matplotlib.pyplot as plt

# fname 为你下载的字体库路径，注意 SimHei.ttf字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="../font/SimHei.ttf")
# 调整subplot周围的边距
plt.subplots_adjust(wspace=5, hspace=10)
plt.figure(figsize=[16.5, 12.5])
plt.tight_layout(pad=0.4, w_pad=3.0, h_pad=3.0)

plt.subplot(2, 2, 1)
plt.title("图1", fontproperties=zhfont1)
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.hist(random.randn(100), bins=20, color="g")
plt.legend(['图例1'], loc='upper left', prop=zhfont1)

plt.subplot(2, 2, 2)
plt.title("图2", fontproperties=zhfont1)
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.scatter(np.arange(30), np.arange(30) + 3 * random.randn(30), edgecolors='b')
plt.legend(['图例2'], loc='lower right', prop=zhfont1)

plt.subplot(2, 2, 3)
x = np.arange(1, 50)
y = 2 * x
plt.title("图3", fontproperties=zhfont1)
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
# 控制图标的范围
plt.xlim([0, 50])
plt.ylim([0, 100])
# 通过xsticks与yticks函数：指定坐标轴的刻度
plt.xticks(np.linspace(0, 50, 11))
plt.yticks(np.linspace(0, 100, 11))
# 'k-- '是一个线性选项，用于告诉Matplotlib绘制黑色虚线图。
plt.plot(x, y, 'r--')
# 设置图例
plt.legend(['图例3'], loc='best', prop=zhfont1)

plt.subplot(2, 2, 4)
plt.title("图4", fontproperties=zhfont1)
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.plot(random.randn(50), 'k--')
# 设置图例
plt.legend(['图例4'], loc='best', prop=zhfont1)
# 将图表保存到文件（支持文件格式：pdf、png、svg、jpg）
plt.savefig('figpath.svg', bbox_inches='tight')
plt.show()
