import numpy as np
import pandas as pd

arr = np.zeros((2, 4), dtype=int)
print("Enter 4 integer grades for FALL:")
for j in range(4):
    arr[0, j] = int(input(f"  Fall grade #{j+1}: "))

print("Enter 4 integer grades for SPRING:")
for j in range(4):
    arr[1, j] = int(input(f"  Spring grade #{j+1}: "))

flat = arr.flatten().copy()
ser = pd.Series(flat, name="AllGrades")

print("\nSeries:")
print(ser)

print("\nDescribe():")
print(ser.describe())
