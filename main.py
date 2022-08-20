import numpy as np
import matplotlib.pyplot as plt

plt.xlabel(r'$h, мм$')
plt.ylabel(r'$Q, мм^3/с$')
plt.title(r'$Зависимость\;расхода\; Q(h)\; от\; расстояния\; h.$')


c = np.arange(0, 0.2, 0.001)
x = [0.0169, 0.0499, 0.0819, 0.1128, 0.1429, 0.1576]
y = [0.127, 0.144, 0.186, 0.1957, 0.202, 0.218]
p, v = np.polyfit(x, y, deg=1, cov=True)
plt.plot(c, p[0] * c + p[1])
plt.errorbar(x, y, yerr = [0.010, 0.020, 0.006, 0.0060, 0.003, 0.010], fmt='o', ms=4)

plt.grid(True)
plt.show()
print(p[0], v[0][0] ** (1 / 2))