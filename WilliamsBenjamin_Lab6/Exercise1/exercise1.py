import numpy as np

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

arr = np.zeros((2, 4), dtype=int)

print("Enter 4 integer grades for FALL:")
for j in range(4):
    arr[0, j] = int(input(f"  Fall grade #{j+1}: "))

print("Enter 4 integer grades for SPRING:")
for j in range(4):
    arr[1, j] = int(input(f"  Spring grade #{j+1}: "))

s = pd.Series({'Fall': arr[0, :], 'Spring': arr[1, :]})
print("\nSeries (by semester):")
print(s)

sem = input("\nEnter semester to plot (Fall/Spring): ")
lw = float(input("Enter line width: "))
color = input("Enter line color: ")

y = s[sem]
x = np.arange(4)

plt.plot(x, y, color=color, linewidth=lw, marker='o', label=sem)
plt.title(f"{sem} Grades")
plt.xlabel("Index")
plt.ylabel("Grade")
plt.legend()
plt.xticks(range(4))
plt.grid(True)
plt.show()
