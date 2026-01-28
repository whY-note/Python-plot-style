import numpy as np
import matplotlib.pyplot as plt

from plot_colors import color_gradient_norm

num = 10

colors = color_gradient_norm((255, 255, 0), (255, 0, 255), num)

# parameters
a = 0.1
b = 0.2

theta = np.linspace(0, 8*np.pi, 2000)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='polar')

for i in range(1, 1 + num):
    # rose
    r = np.abs(a * i * np.sin(3*theta))
    ax.plot(theta, r, color = colors[i-1])
plt.savefig("./demo/rose.png")
plt.show()

