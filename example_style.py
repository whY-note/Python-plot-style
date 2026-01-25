from plot_style import apply_style

import numpy as np
import matplotlib.pyplot as plt

apply_style("Simple")

num = 6

def frac_kx(x, k:int):
    '''
    $$
    y = ln(kx)
    $$
    '''
    return np.log(k*x)

x = np.linspace(0.01,2,100)

for k in range(1, 1+num):
    if k==1:
        data = frac_kx(x,k)
    else:
        data = np.vstack((data, frac_kx(x,k)))
print(data.shape)

for i in range(num):
    plt.plot(x, data[i,:], label = f"$\ln({i+1}x)$")
plt.legend(loc="lower right")
plt.savefig("demo/simple_style.png")
plt.show()