import matplotlib.pyplot as plt
import numpy as np

# x取值范围从0~5PI，等差数列，分成1000，越大线条越平滑
x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.fill(x, y1, 'b', alpha=0.5)
plt.fill(x, y2, 'r', alpha=0.3)
# 填充，是指在变量和所选择的一个数值之间的颜色
plt.fill_between(x, y1, y2, facecolor='green')
plt.grid(True)

plt.show()

#########################################################
plt.plot(x, y1, 'b', alpha=0.5)
plt.plot(x, y2, 'r', alpha=0.3)
# 添加条件
# 如果数据点比较少的情况下，会有缝隙出现，使用interpolate可以填充缝隙
plt.fill_between(x, y1, y2, where=y1 >= y2, facecolor='green', interpolate=True)
plt.fill_between(x, y1, y2, where=y2 > y1, facecolor='yellow', interpolate=True)
plt.grid(True)

plt.show()
###########################################################

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red', alpha=.25)

plt.xlim(-np.pi, np.pi)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())
plt.show()
