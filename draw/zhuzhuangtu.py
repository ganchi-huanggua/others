import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
size = 10
# a = np.array([0.9788, 0.9578, 0.9529, 0.9013, 0.8864, 0.8838, 0.9223, 0.8249, 0.8268, 0.8470])
# b = np.array([0.9508, 0.9289, 0.8991, 0.8204, 0.7946, 0.7571, 0.7715, 0.6801, 0.6677, 0.6974])
# c = np.array([0.9535, 0.8974, 0.8831, 0.7964, 0.7529, 0.7303, 0.7259, 0.6493, 0.6115, 0.6360])
all = []
a, b, c = [], [], []
with open("../results/temp.txt", encoding="utf-8") as f:
    target_string = "count: "
    for line in f.readlines():
        if target_string in line:
            idx = line.find(target_string)
            i = idx + len(target_string)
            number = ""
            while line[i].isdigit() or line[i] == '.':
                number = number + line[i]
                i += 1
            all.append(float(number))
print(len(all))
all = [all[i] for i in range(len(all)) if i % 12 == 11 or i % 12 == 10 or i % 12 == 9]
print(len(all))

for i in range(len(all)):
    if i % 3 == 0:
        a.append(all[i])
    elif i % 3 == 1:
        b.append(all[i])
    elif i % 3 == 2:
        c.append(all[i])

a = np.array(a)
print(len(a))
b = np.array(b)
c = np.array(c)

# x轴坐标, size=5, 返回[0, 1, 2, 3, 4]
x = np.arange(1, 11)

# 有a/b/c三种类型的数据，n设置为3
total_width, n = 0.8, 3
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width)
plt.title("l2p+self-training future oot psudo label in iter 3")
plt.xlabel("task")
plt.xticks(range(1, 11))  # 设置X轴显示哪些值，分开设好读
plt.xlim([0, 11])  # 设置x轴从2000开始到2020结束
plt.ylabel("acc")
plt.yticks(range(0, 1501, 150))  # 其实许多时候可以先看看默认的情况，不合适再改
plt.ylim([0, 1500])  # 设置y轴从0显示到2400

# 画柱状图
plt.bar(x, a, width=width, label="previous label on future sample count")
plt.bar(x + width, b, width=width, label="it label on future sample count")
plt.bar(x + width * 2, c, width=width, label="previous label on it sample count")
# 显示图例
plt.legend()
# 显示柱状图
plt.show()