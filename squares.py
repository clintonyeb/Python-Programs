import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 20)

y = x ** 2

line,  = plt.plot(x, y, 'ro')
plt.title('A plot of the square of first 100 numbers')
plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.axes([1, 20, 1, 400])
plt.setp(line, color='g', linewidth=2.0)
plt.show()
