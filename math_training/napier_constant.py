import matplotlib.pyplot as plt
import math
import numpy as np

e = math.e
print e

dx = 0.1
x = np.arange(-5, 5, dx)

y_2 = 2**x
y_e = e**x
y_3 = 3**x
y_de = (e**(x+dx) - e**x) / dx

#plt.plot(x, y_2)
plt.plot(x, y_e)
plt.plot(x, y_de)
#plt.plot(x, y_3)
plt.show()

