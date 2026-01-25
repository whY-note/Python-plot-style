import numpy as np
import matplotlib.pyplot as plt

from plot_colors import color_gradient_norm

num = 5
def gauss(x, mu=0, sigma=1):
    return 1/(np.sqrt(2 * np.pi) * sigma) *np.exp(-(x-mu)**2/(2*sigma**2))
 
x = np.linspace(-20,20,1000)

for k in range(1, 1+num):
    if k==1:
        data = gauss(x,mu=0,sigma=k)
    else:
        data = np.vstack((data, gauss(x,mu=0, sigma=k)))
print(data.shape)

colors = color_gradient_norm((128, 240, 128), (0, 0, 235), num)

plt.figure()
for i in range(num):
    plt.plot(x, data[i,:], color = colors[i], label = "$\sigma=$"+str(i+1))
plt.legend()
plt.savefig("demo/gauss.png")
plt.show()
