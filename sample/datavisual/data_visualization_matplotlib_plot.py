# coding:utf-8
# 导入Numpy(数学运算)和Matplotlib的pyplot两个模块
# matplotlib.pyplot.plot(x, y, label="标签颜色", color="折线颜色", linestyle="折线类型", linewidth="线宽",
# marker="标记点符号", markersize="标记点大小")

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False

# 1.使用plot来绘制折线
# 修改标签文字和线条粗细
plt.title("squre number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.plot(x_values, y_values, linewidth=5)
print("===================折线图1=========================")
plt.show()

# 2.使用Matplotlib绘制一个正弦和余弦函数曲线
# 创建X轴的数据：从-PI到PI的256个等差数字
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# 使用cos和sin函数以x为自变量创建C和S
C, S = np.cos(x), np.sin(x)
zhfont1 = matplotlib.font_manager.FontProperties(fname="../font/SimHei.ttf")
# 修改标签文字和线条粗细
plt.title("正弦与余弦曲线", fontsize=24)
# 使用plot()分别绘制正弦和余弦函数
plt.plot(x, C)
plt.plot(x, S)
print("===================正弦与余弦曲线===================")
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
plt.plot(x, y1, color="green", linewidth=1.0, linestyle="-", label="y1")
# 绘制红色，宽度为2个像素的虚线
plt.plot(x, y2, color="red", linewidth=2.0, linestyle="--", label="y2")
# 设置横轴的上下限为-1~6
plt.xlim(-1, 6)
# 设置纵轴的上下限为-2~10
plt.ylim(-2, 10)
# 设置图例
plt.legend(loc="upper left")
# 注释特殊点位
# scatter([x][y],s="点的大小")函数用于绘制散点图
plt.scatter([3], [6], s=30, color="blue")
plt.scatter([3], [0], s=30, color="red")
# annotate("标注内容",xy=(要在哪个位置点标注内容))
plt.annotate("(3,6)", xy=(3.3, 5.5), fontsize=16)
plt.annotate("(3,0)", xy=(3.3, 0), fontsize=16)
# 想给点添加注释，需要使用text(x,y,s)函数
plt.text(4, -0.5, "该处为重要点位", fontdict={'size': 12, 'color': 'green'})
# 保存图表
# plt.savefig()函数：
#  支持png/pdf/svg/ps等，以后缀名来指定
#  dpi=分辨率,
#  bbox_inches='tight'，尝试剪除图表周围的空白部分
#  facecolor/edgecolor：
plt.savefig("pic.png", dpi=100, bbox_inches='tight', facecolor="purple", edgecolor="blue")
print("===================折线图2=========================")
plt.show()

# 4.使用bar()函数绘制一个柱状图
# 创建1个点数 8 x 6 的窗口，并设置分辨率为80像素/英寸
plt.figure(figsize=(8, 6), dpi=80)
# 设置柱子总数
N = 6
# 包含每个柱子对应值的序列
values = (5, 16, 20, 25, 23, 28)
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.55
# 绘制柱状图，每根柱子的颜色为蓝色
ps = plt.bar(index, values, width, label="月均气温", color="#87CEFA")
# 设置横轴标签
plt.xlabel("月份")
# 设置纵轴标签
plt.ylabel("温度（摄氏度）")
# 添加标题
plt.title("月均气温")
# 添加纵横轴的刻度(1st列表的值代表刻度，2nd列表的值代表所显示的标签)
plt.xticks(index, ('一月', '二月', '三月', '四月', '五月', '六月'))
# arange函数用于创建等差数组：np.arange([start, ]stop, [step, ]dtype=None)
plt.yticks(np.arange(0, 50, 10))
# 添加图例
plt.legend(['温度'], loc="upper right")
print("===================柱状图==========================")
plt.show()

# 5.使用pie()函数绘制一个柱状图
labels = '大一', '大二', '大三', '大四'  # labels设置各个分片的标签
sizes = [15, 30, 45, 10]  # 数值列表
# 将"大二"突出显示
explode = (0, 0.1, 0, 0)  # explode指定饼图中突出的分片
# autopct设置标签中的数字格式; shadow设置是否有阴影；startangle设置从哪个角度开始绘制饼图
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 确保饼图是个圆形
plt.title('饼图示例')
print("===================饼图===========================")
plt.show()
