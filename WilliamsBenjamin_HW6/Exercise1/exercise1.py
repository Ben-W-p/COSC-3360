import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

grades = []

while True:
    g = float(input('Grade: '))
    if g < 0:
        break
    grades.append(g)
    
gradesArray= np.array(grades)

indicies = [i for i in range(1, len(gradesArray) + 1)]

df = pd.Series(gradesArray, index=indicies)

print('Mean: ', df.mean())
print('STD: ', df.std())
print('Max: ', df.max())
print('Min: ', df.min())
print('25% Percentiles: ', df.quantile(0.25))

plt.bar(df.index, df.values, color='gray')
plt.plot(df.index, df.values, color='red')
plt.scatter(df.index, df.values, color='blue')


plt.xlabel('Index')
plt.ylabel('Grade')

plt.show()