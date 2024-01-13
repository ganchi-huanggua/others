import matplotlib.pyplot as plt  
import numpy as np  
import pandas as pd

# 数据  
data = pd.read_csv("result.csv", header=None)
x = np.linspace(1, 10, 10)  
y1 = data.iloc[0]  
y2 = data.iloc[1]
y3 = data.iloc[2]
y4 = data.iloc[3]
y5 = data.iloc[4]
y6 = data.iloc[5]


  
# 创建figure和axes对象  
fig, ax = plt.subplots()  
ax.grid(which="both", linestyle=":", linewidth=1, color='y', alpha=1)

# 绘制第一组线
ax.plot(x, y1, 'r-o', label='l2p')
ax.plot(x, y2, 'g-x', label='l2p pseudo labeled')
ax.plot(x, y3, 'b-v', label='l2p self-training')  
ax.set_ylabel('5% labeled')
ax.set_yticks(range(0, 101, 10))
ax.set_ylim([0, 100])
# ax.set_xticklabels([" ", "iter: 0\ntask: 0\ninit unlabeled data: 4758\n\n", "iter: 1", "iter: 2", "iter: 3", "iter: 4", "iter: 0\ntask: 1\ninit unlabeled data: 4761", "iter: 1"])
ax.set_xticks(range(1, 11, 1))
ax.set_xlim([0, 11])
ax.legend(bbox_to_anchor=(0.1, 0.25))  


ax.set_title('l2p and semi-supervised')  
  
# 创建第二个Y轴  
ax2 = ax.twinx()  
ax2.grid(which="both", linestyle=":", linewidth=1, color='y', alpha=1)
ax2.set_ylabel('1% labeled') 
ax2.set_yticks(range(0, 101, 10))
ax2.set_ylim([0, 100])
<<<<<<< HEAD
ax2.plot(x, y4, 'r-o', linestyle='--') 
ax2.plot(x, y5, 'g-x', linestyle='--')
ax2.plot(x, y6, 'b-v', linestyle='--')
=======
ax2.plot(x, y4, 'r-o', linestyle='-') 
ax2.plot(x, y5, 'g-x', linestyle='-')
ax2.plot(x, y6, 'b-v', linestyle='-')
>>>>>>> 6c10f116f1412badefcf90c845e48da763c56573
    
# 显示图例  
ax.legend(bbox_to_anchor=(0.5, 0.25))  
# ax2.legend(bbox_to_anchor=(0.5, 0.25))  
  
# 显示图形  
plt.show()