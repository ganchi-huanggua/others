import matplotlib.pyplot as plt  
import numpy as np  
import pandas as pd

# 数据  
data = pd.read_csv("result.csv", header=None)
x = np.linspace(1, 7, 7)  
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
ax.plot(x, y1, 'r-o', label='multi-test')
ax.plot(x, y2, 'r-x', label='multi-pse')
ax.plot(x, y3, 'b-o', label='once-test')  
ax.plot(x, y4, 'b-x', label='once-pse')
ax.set_ylabel('test or pseudo label acc')
ax.set_yticks(range(0, 101, 20))
ax.set_ylim([0, 100])
ax.set_xticklabels([" ", "iter: 0\ntask: 0\ninit unlabeled data: 4758\n\n", "iter: 1", "iter: 2", "iter: 3", "iter: 4", "iter: 0\ntask: 1\ninit unlabeled data: 4761", "iter: 1"])
ax.legend(bbox_to_anchor=(0.1, 0.25))  


ax.set_title('l2p self training')  
  
# 创建第二个Y轴  
ax2 = ax.twinx()  
ax2.grid(which="both", linestyle=":", linewidth=1, color='y', alpha=1)
ax2.set_ylabel('pseudo labeled data count') 
ax2.set_yticks(range(0, 5001, 1000))
ax2.set_ylim([0, 5000])
ax2.plot(x, y5, 'r-v', label='multi-labeled') 
ax2.plot(x, y6, 'b-v', label='once-labeled')
    
# 显示图例  
ax.legend()  
ax2.legend(bbox_to_anchor=(0.5, 0.25))  
  
# 显示图形  
plt.show()