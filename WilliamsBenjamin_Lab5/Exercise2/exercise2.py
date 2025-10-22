import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 10, 120)

y = np.tan(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.title('x vs tan(x)')
plt.show()