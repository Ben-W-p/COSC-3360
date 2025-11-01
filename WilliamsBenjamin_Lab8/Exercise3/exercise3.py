import numpy as np

x = np.array([1., 2., 3., 4., 5.], dtype=float)
y = np.array([1., 2., 4., 4., 6.], dtype=float)

X = np.vstack([np.ones_like(x), x]).T
a, b = np.linalg.inv(X.T @ X) @ (X.T @ y)

def sse(y_true, y_pred):
    return float(np.sum((y_true - y_pred)**2))

y_best = a + b*x
y2 = 0.5 + x
y3 = 1.2 * x

sse_best = sse(y, y_best)
sse_y2 = sse(y, y2)
sse_y3 = sse(y, y3)

print(f"SSE (best-fit) = {sse_best:.6f}")
print(f"SSE (y2 = 0.5 + x) = {sse_y2:.6f}")
print(f"SSE (y3 = 1.2x) = {sse_y3:.6f}")
