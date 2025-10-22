import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}, index=["Test1", "Test2", "Test3"])

plt.boxplot(df.values)
plt.xticks(range(1, len(df.columns) + 1), df.columns)
plt.title("Student Grade Distributions")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.grid(True, axis='y')
plt.show()
