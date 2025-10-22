import numpy as np
import matplotlib.pyplot as plt

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

xmin = read_float("xmin: ")
xmax = read_float("xmax: ")
step = read_float("step (>0): ")
if step == 0:
    raise SystemExit("Step must be non-zero.")

x = np.arange(xmin, xmax+step, step)

expr = input("Enter expression in x (e.g., 'abs(x)', 'np.sin(x)', 'x**2 + 3'): ")

allowed_names = {'np': np, 'x': x}
y = eval(expr)

plt.plot(x, y, label=f"y = {expr}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("User-defined function")
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
