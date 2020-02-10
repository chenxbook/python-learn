# coding:utf-8
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





