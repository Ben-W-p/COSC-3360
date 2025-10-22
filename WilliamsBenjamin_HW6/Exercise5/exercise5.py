import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

grades_dict = {
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}

df = pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])

plt.plot(df.columns, df.loc['Test1', :], 'ro--', label='Test1')

plt.plot(df.columns, df.loc['Test2', :], 'g*--', label='Test2')

plt.plot(df.columns, df.loc['Test3', :], 'b^-', label='Test3')

plt.ylim(0, 100)
plt.legend()
plt.xlabel('Student Name')
plt.ylabel('Grade')
plt.show()