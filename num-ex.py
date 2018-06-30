import numpy as np

d = np.array([2, 3, 4, 5, 5, 23, 3, 43, 43])
print(type(d))


def linspace(s, e, n):
    f = (e - s) / n
    while (s < e):
        print(s)
        s += f
