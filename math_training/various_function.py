import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 15, 0.1)

# y_2 = x^2 - 10x + 10
y_2 = x**2 - 10*x + 10

# y_3 = x^3 - 10x^2 - 10x + ff
y_3 = x**3 - 10*x**2 - 10 * x + 10


#plt.plot(x, y_2)
#plt.plot(x, y_3)

plt.show()
