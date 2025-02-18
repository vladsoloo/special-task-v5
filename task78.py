import numpy as np


a = 0
b = 2*np.pi


N = 1000


h = (b - a) / N


x = np.linspace(a, b, N+1)
y = np.sin(x)


area = h * np.sum(y[:-1])

print(f"Приблизительная площадь одной арки синусоиды: {area}")
