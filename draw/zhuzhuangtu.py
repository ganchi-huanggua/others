import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
size = 3
a = np.array([83.926, 75.762, 43.04])
b = np.array([82.169, 79.448, 66.903])

# x轴坐标, size=5, 返回[0, 1, 2, 3, 4]
x = np.arange(size)


# 有a/b/c三种类型的数据，n设置为3
total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width)
plt.title("l2p pseudo labeled cifar100")
plt.xlabel("labelled ratio")
plt.xticks(x, ["25%", "5%", "1%"])  # 设置X轴显示哪些值，分开设好读
plt.ylabel("acc@1")
plt.yticks(range(30, 110, 10))  # 其实许多时候可以先看看默认的情况，不合适再改
plt.ylim([30, 100]) 

# 画柱状图
plt.bar(x, a, width=width, label="l2p")
plt.bar(x + width, b, width=width, label="l2p_pseudo_labelled")
# 显示图例
plt.legend()
# 显示柱状图
plt.show()