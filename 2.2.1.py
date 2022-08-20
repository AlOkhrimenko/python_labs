import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0, 1.5, 0.01)
# Первая серия
x_1 = [1.17, 1.41 ,0.92, 0.69, 0.55]
y_1 = [4.25, 5.28, 3.61, 2.87, 2.33]
p_1 = np.polyfit(x_1, y_1, deg=1, cov=False)
# Вторая серия
x_2 = [1.29, 1.015, 0.68, 0.51, 0.185]
y_2 = [7.27, 6.22, 4.4, 3.54, 1.47]
p_2 = np.polyfit(x_2, y_2, deg=1, cov=False)

plt.xlabel(r'$N, Вт$')
plt.ylabel(r'$\Delta T(N), K$')
plt.title(r'$Зависимость\; изменения\; температуры\; \Delta T(N)\; от\; мощности\; N.$')

#plt.plot(a, p_1[0]*a + p_1[1])
#plt.errorbar(x_1, y_1, fmt = 'o', ms= 4 )

plt.plot(a, p_2[0]*a + p_2[1])
plt.errorbar(x_2, y_2, fmt = 'o', ms= 4 )

plt.grid(True)
plt.show()
print (p_1[0], p_2[0])
cp = ( ( (1/p_1[0]) - (1/p_2[0]) ) * 1000 )/ 0.11
print (cp)
alpha1 = (1/p_1[0]) - (cp*0.23*0.001)
alpha2 = (1/p_2[0]) - (cp*0.12*0.001)
#print ( alpha1*1000/0.23, alpha2*1000/0.12)
print(alpha1, alpha2)