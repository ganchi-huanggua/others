import matplotlib.pyplot as plt 
import matplotlib 
import numpy as np  
from matplotlib import cm
  
# start_color = "#000000"
# end_color = "#FF0000"

# num_steps = 10

# start_rgb = matplotlib.colors.hex2color(start_color)
# end_rgb = matplotlib.colors.hex2color(end_color)

# gradient_rgb = np.linspace(start_rgb, end_rgb, num_steps)

# fig = plt.figure()
# fig1 = fig.add_subplot(121)
# fig1.imshow(gradient_rgb, aspect="auto", cmap=plt.get_cmap('rainbow'))
# fig1.axis('off')
# plt.show()

labeled_samples_count = np.full(10, 250)
in_task_unlabeled_samples_conut = np.full(10, 2500)
out_of_task_unlabeled_samples_count = np.arange(0, 2500, 250)

x = np.arange(1, 11)

# 有a/b/c三种类型的数据，n设置为3
total_width, n = 0.8, 3
# 每种类型的柱状图宽度
width = total_width / n


x = x - 0.5 * (total_width - width)
plt.title("data distribution")

# 重新设置x轴的坐标
plt.xlabel("task")
plt.xticks(range(1, 11))  # 设置X轴显示哪些值，分开设好读
plt.xlim([0, 11])  # 设置x轴从2000开始到2020结束
plt.ylabel("acc")
plt.yticks(range(0, 2501, 250))  # 其实许多时候可以先看看默认的情况，不合适再改
plt.ylim([0, 2500])  # 设置y轴从0显示到2400

# 画柱状图
plt.bar(x, labeled_samples_count, width=width, label="labeled_samples_count")
plt.bar(x + width, in_task_unlabeled_samples_conut, width=width, label="in_task_unlabeled_samples_conut")
plt.bar(x + 2 * width, out_of_task_unlabeled_samples_count, width=width, label="out_of_task_unlabeled_samples_count")

plt.colorbar()

# 显示柱状图
plt.show()

# x = np.linspace(0, 10, 1000)
# I = np.sin(x) * np.cos(x[:, np.newaxis])
# speckles = (np.random.random(I.shape) < 0.01)
# I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))
# plt.figure(figsize=(10, 3.5))
 
# plt.subplot(121)
# plt.imshow(I, cmap='RdBu')
# plt.colorbar(label='noisy points')
 
# plt.subplot(122)
# plt.imshow(I, cmap='RdBu')
# plt.colorbar(extend='both', label='noisy points extend')
# plt.clim(-1, 1)
# plt.show()