import numpy as np
import matplotlib.pyplot as plt

x = np.array([1., 2., 3., 4., 5.], dtype=float)
y = np.array([1., 2., 4., 4., 6.], dtype=float)

X = np.vstack([np.ones_like(x), x]).T
a, b = np.linalg.inv(X.T @ X) @ (X.T @ y)

x_pred = 2.5
y_pred = float(a + b*x_pred)
print(f"Best-fit model: y = {a:.4f} + {b:.4f} x;  Prediction at x=2.5 -> y={y_pred:.4f}")

xs = np.linspace(x.min()-0.5, x.max()+0.5, 200)
y_best = a + b*xs

plt.scatter(x, y, label="data")
plt.plot(xs, y_best, label="best-fit")
plt.scatter([x_pred], [y_pred], marker="o", label=f"prediction (x=2.5, y={y_pred:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Least Squares Regression Line and Predicted Value")
plt.legend()
plt.tight_layout()
plt.show()
