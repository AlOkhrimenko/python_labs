import numpy as np
import matplotlib.pyplot as plt

a = np.arange(8, 60, 0.1)
x = [25.7, 34.6, 38.5, 50.2, 57.8]
y = [20.9, 35.8, 38.7, 60.0, 66.4]
p, v = np.polyfit(x, y, deg=1, cov=True)
plt.xlabel(r'$h, мм$')
plt.ylabel(r'$Q, мм^3/с$')
plt.title(r'$Зависимость\;расхода\; Q(h)\; от\; расстояния\; h.$')
plt.plot(a, p[0]*a + p[1])
plt.errorbar(x, y, yerr = [0.2, 0.6, 0.7, 1.8, 2.2], fmt = 'o', ms= 4 )
plt.grid(True)


print(v[0])
plt.show()
#print(p[1])
#print(p[0])