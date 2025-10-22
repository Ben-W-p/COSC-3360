# Exercise4.py
import pandas as pd

# Same base DataFrame
df = pd.DataFrame({
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}, index=["Test1", "Test2", "Test3"])

print("Initial DataFrame:")
print(df)

by = input("\nEnter label to sort by (a column name like 'Wally' if axis=0, or a row name like 'Test1' if axis=1): ")
axis = int(input("Enter axis (0 = rows sort by a column; 1 = columns sort by a row): "))
ascending = input("Ascending (true/false): ").strip().lower() == "true"

sorted_df = df.sort_values(by=by, axis=axis, ascending=ascending)

print("\nSorted DataFrame:")
print(sorted_df)
