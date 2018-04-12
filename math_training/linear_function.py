import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
print x


y = 2 * x + 1
print y

plt.plot(x, y)
plt.show()

