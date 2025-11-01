import numpy as np
import matplotlib.pyplot as plt

x = np.array([1., 2., 3., 4., 5.], dtype=float)
y = np.array([1., 2., 4., 4., 6.], dtype=float)

X = np.vstack([np.ones_like(x), x]).T
a, b = np.linalg.inv(X.T @ X) @ (X.T @ y)

xs = np.linspace(x.min()-0.5, x.max()+0.5, 200)
y_best = a + b*xs
y2 = 0.5 + xs
y3 = 1.2 * xs

plt.scatter(x, y, label="data")
plt.plot(xs, y_best, label="best-fit")
plt.plot(xs, y2, label="y2 = 0.5 + x")
plt.plot(xs, y3, label="y3 = 1.2x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Least Squares Regression Lines")
plt.legend()
plt.tight_layout()
plt.show()
