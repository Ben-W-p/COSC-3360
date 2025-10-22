import numpy as np

arr = np.zeros((3,2,2), dtype=float)

print("Enter 12 float values to fill a 3x2x2 array (depth, row, col).")
for d in range(3):
    for r in range(2):
        for c in range(2):
            while True:
                try:
                    arr[d, r, c] = float(input(f"Value for [{d},{r},{c}]: "))
                    break
                except ValueError:
                    print("Please enter a number.")

print("\nArray:")
print(arr)

print("\nModify an element:")
def read_index(name, limit):
    while True:
        try:
            i = int(input(f"{name} (0..{limit-1}): "))
            if 0 <= i < limit:
                return i
        except ValueError:
            pass
        print("Invalid.")

d = read_index("depth", 3)
r = read_index("row", 2)
c = read_index("col", 2)

while True:
    try:
        new_val = float(input("New value: "))
        break
    except ValueError:
        print("Please enter a number.")

arr[d, r, c] = new_val
print("\nUpdated array:")
print(arr)
