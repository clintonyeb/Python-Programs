import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

np.randome.seed(19732232)
mu = 100
sigma = 15
x = mu + sigma * np.random.randn(438)

num_bins = 50

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, num_bins, normed=1)

y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
