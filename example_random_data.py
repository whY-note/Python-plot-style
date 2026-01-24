import matplotlib.pyplot as plt
import numpy as np
from plot_colors import color_gradient_norm

rows, cols = 10,50
bias = 5

data_row = np.random.randn(cols)
data = data_row
for i in range(1,rows):
    data = np.vstack((data, data_row+ i*bias))
print(data.shape)

colors = color_gradient_norm((255, 0, 0), (0, 0, 255), rows)

plt.figure()
for i in range(rows):
    plt.plot(data[i,:], color = colors[i])
plt.show()