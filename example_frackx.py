import numpy as np
import matplotlib.pyplot as plt

from plot_colors import color_gradient_norm

num = 10
def frac_kx(x, k:int):
    '''
    $$
    y = k/x
    $$
    '''
    return k/x
 
x = np.linspace(0.01,1,100)

for k in range(1, 1+num):
    if k==1:
        data = frac_kx(x,k)
    else:
        data = np.vstack((data, frac_kx(x,k)))
print(data.shape)

colors = color_gradient_norm((255, 0, 0), (0, 0, 255), num)

plt.figure()
for i in range(num):
    plt.plot(data[i,:], color = colors[i], label = f"{i+1}/x")
plt.legend()
plt.show()
