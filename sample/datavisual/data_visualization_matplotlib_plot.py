# coding:utf-8
# 导入Numpy(数学运算)和Matplotlib的pyplot两个模块
# matplotlib.pyplot.plot(x, y, label="标签颜色", color="折线颜色", linestyle="折线类型", linewidth="线宽",
# marker="标记点符号", markersize="标记点大小")

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# 1.使用plot来绘制折线
print("=================================================使用plot来绘制折线============================================")
# 修改标签文字和线条粗细
plt.title("squre number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.plot(x_values, y_values, linewidth=5)
plt.show()

# 2.使用Matplotlib绘制一个正弦和余弦函数曲线
# 创建X轴的数据：从-PI到PI的256个等差数字
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# 使用cos和sin函数以x为自变量创建C和S
C, S = np.cos(x), np.sin(x)
zhfont1 = matplotlib.font_manager.FontProperties(fname="../font/SimHei.ttf")
# 修改标签文字和线条粗细
plt.title("正弦与余弦曲线", fontsize=24, fontproperties=zhfont1)
# 使用plot()分别绘制正弦和余弦函数
plt.plot(x, C)
plt.plot(x, S)

plt.show()

# 3.绘制一段最基本的折线图
# 创建1个点数 8 x 6 的窗口，并设置分辨率为80像素/英寸
plt.figure(figsize=(8, 6), dpi=80)
# 创建X轴的数据：从-2到6的5个等差数字，分别为-2,0,2,4,6
x = np.linspace(-2, 6, 5)
# 绘制直线1
y1 = x + 3
# 绘制直线2
y2 = 3 - x

# 绘制绿色，宽度为1个像素的实线
plt.plot(x, y1, color="green", linewidth=1.0, linestyle="-")
# 绘制红色，宽度为2个像素的虚线
plt.plot(x, y2, color="red", linewidth=2.0, linestyle="--")
# 设置横轴的上下限为-1~6
plt.xlim(-1, 6)
# 设置纵轴的上下限为-2~10
plt.ylim(-2, 10)
plt.show()
