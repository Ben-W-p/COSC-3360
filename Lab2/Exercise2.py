import myFunctions
from Lab2.myFunctions import factorial

#finding e

n = 10 # iterations

e = 0

for i in range(0, n + 1):
    print(str(i) + ": " + str(factorial(i)))
    e += 1/(factorial(i))

print(f"Approximate value of e after {n} iterations: {e}")