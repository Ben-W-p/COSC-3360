import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1, 1.1, 0.1)

y = np.arcsin(x)

y_deg = np.degrees(y)

plt.plot(x, y_deg)
plt.title('Plot of sin**-1')
plt.xlabel('Sine')
plt.ylabel('Angle (degrees)')
plt.show()