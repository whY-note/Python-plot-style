import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

points = np.column_stack([x, y])          # (N, 2)
segments = np.stack([points[:-1], points[1:]], axis=1)
# segments.shape == (N-1, 2, 2)

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

values = np.linspace(0, 1, len(segments))

lc = LineCollection(
    segments,
    cmap="magma",
    array=values,     # 核心！
    linewidth=2
)
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
plt.show()


