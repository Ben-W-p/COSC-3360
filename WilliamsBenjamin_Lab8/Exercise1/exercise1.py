import numpy as np
import matplotlib.pyplot as plt

x = np.array([1., 2., 3., 4., 5.], dtype=float)
y = np.array([1., 2., 4., 4., 6.], dtype=float)

X = np.vstack([np.ones_like(x), x]).T
beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
a, b = float(beta[0]), float(beta[1])

xs = np.linspace(x.min()-0.5, x.max()+0.5, 200)
ys = a + b*xs

print(f"Best-fit model: y = {a:.4f} + {b:.4f} x")

plt.scatter(x, y, label="data")
plt.plot(xs, ys, label="best-fit")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Least Squares Regression Line")
plt.legend()
plt.tight_layout()
plt.show()
