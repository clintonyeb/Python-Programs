import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=80)
data = np.linspace(-np.pi, np.pi, 256, endpoint=True)

a, b = np.cos(data), np.sin(data)
plt.plot(data, a, color="blue", linewidth=2.0, linestyle="-", label="cosine")
plt.plot(data, b, color="green", linewidth=2.0, linestyle="-", label="sine")
plt.legend(loc="upper left")
plt.xlim(a.min() * 1.1, a.max() * 1.1)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.ylim(b.min() * 1.1, b.max() * 1.1)
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color="blue")
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy = (t, np.cos(t)),
             xycoords='data',
             xytext = (-90, -50),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()
