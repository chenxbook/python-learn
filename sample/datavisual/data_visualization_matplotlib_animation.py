import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# 自定义动画

# 定义画布，默认值，这个fig需要，虽然默认大小设置，fig需要挂在动画上
fig = plt.figure()

# 坐标轴刻度
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))

# color='blue'=蓝色，否则默认为清淡蓝色
line, = ax.plot([], [], lw=2, color='blue')


# 因为动画，所以初始化列表线条
def init():
    line.set_data([], [])
    return line,  # 注意逗号


# 定义动画
def animate(i):
    # x取值范围从0~2，等差数列，分成1000，越大线条越平滑
    x = np.linspace(0, 2, 1000)
    # 动画x和y的值与i的从0～i的取值有关，才动起来
    y = np.sin(2 * np.pi * (x - 0.01 * i))

    line.set_data(x, y)
    return line,  # 注意逗号


# 将fig挂在动画上面
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
# 如果需要保存动画，就这样
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
# 标题名称
plt.title('Sin-a-subplot')
plt.show()
