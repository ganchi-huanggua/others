import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 10))
plt.colorbar(ticks=np.arange(-1, 1, 0.2), label='digit value')
plt.show()