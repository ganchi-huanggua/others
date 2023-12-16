import numpy as np
from sklearn.metrics import confusion_matrix 
import seaborn as sns  
import matplotlib.pyplot as plt  

# ground_truth = []
# predict = []
start = 0
end = 10
for i in range(start, end):
    data = np.loadtxt("output" + str(i) + ".csv")
    # ground_truth.append(data[0 : int(data.shape[0] / 2)]) 
    # predict.append(data[int(data.shape[0] / 2) :])
    # ground_truth = np.concatenate(ground_truth)
    # predict = np.concatenate(predict)
    ground_truth = data[0 : int(data.shape[0] / 2)]
    predict = data[int(data.shape[0] / 2) :]
    acc = np.sum(ground_truth == predict) / ground_truth.shape[0]
    cm = confusion_matrix(ground_truth, predict)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("labelled ratio = 0.01, pred acc=" + str(acc)) 
    plt.xlabel('predicted')  
    plt.ylabel('ground_true')
    plt.show()