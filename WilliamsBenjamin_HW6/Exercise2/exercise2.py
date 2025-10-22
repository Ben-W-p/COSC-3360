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

A = []
B = []
C = []
D = []
F = []

def classify_grade(grade):
    if grade >= 90:
        return A
    elif grade >= 80:
        return B
    elif grade >= 70:
        return C
    elif grade >= 60:
        return D
    else:
        return F
    

for val in df.values:
    classify_grade(val).append(val)    
    
explode = (0, 0, 0, 0, 0.1)
plt.pie([len(A), len(B), len(C), len(D), len(F)], 
        labels = ['A', 'B', 'C', 'D', 'F'], 
        autopct='%1.1f%%', startangle=90, 
        explode=explode, shadow=True)
