import numpy as np

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

def factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n * factorial(n - 1)

def minimum(a = None, b = None, c = None):
    array = np.array([])
    if a is not None:
        min_of_numbers = a
        array = np.append(array, a)
    if b is not None:
        min_of_numbers = b
        array = np.append(array, b)
    if c is not None:
        min_of_numbers = c
        array = np.append(array, c)
    if array.size == 0:
        return "No numbers provided"
    else:
        for i in range(0, len(array)):
            if array[i] < min_of_numbers:
                min_of_numbers = array[i]
    return min_of_numbers

def upperCaseCharacters(string):
    upperCount = 0
    for char in string:
        if  ord(char) >= 65 and ord(char) <= 90:
            upperCount+=1
            print(char)
    return upperCount

def my_count(tup, value):
    cnt = 0
    for x in tup:
        if x == value:
            cnt += 1
    return cnt

def my_index(tup, value):
    for i in range(len(tup)):
        if tup[i] == value:
            return i
    return -1

