import myFunctions

def seperator(n):
    print("")
    print(f"-----------------------------------{n}-----------------------------------")

seperator(1)
float1 = float(input("Enter a float: "))
float2 = float(input("Enter another float: "))

while True :
    operation = input("Enter an operation(+,-,*, or /): ")
    resultString  = f'{float1} {operation} { float2} = '
    if operation == "+":
        print (resultString + str(myFunctions.addition(float1, float2)))
        break
    if operation == "-":
        print (resultString + str(myFunctions.subtraction(float1, float2)))
        break
    if operation == "*":
        print (resultString + str(myFunctions.multiplication(float1, float2)))
        break
    if operation == "/":
        print (resultString + str(myFunctions.division(float1, float2)))
        break
    print("invalid operation")

seperator(2)
n = 10 # iterations
e = 0
for i in range(0, n + 1):
    e += 1/(myFunctions.factorial(i))
print(f"Approximate value of e after {n} iterations: {e}")

seperator(3)
print(f"Min of no elements is: {myFunctions.minimum()}")
print(f"Min of 8 is: {myFunctions.minimum(8)}")
print(f"Min of 8, 2 is: {myFunctions.minimum(8, 2)}")
print(f"Min of 8, 2, and 10 is: {myFunctions.minimum(8, 2, 10)}")

seperator(4)
myStr = input("Enter a string: ")
print("Upper case Characters are: ")
print(f"The # of uppercase letters in the string is: {myFunctions.upperCaseCharacters(myStr)}")

seperator(6)
li = [9, 3, 0, -4, 8, 7, 10, -1, 5]
start = int(input("Enter start index: "))
stop = int(input("Enter stop index: "))
step = int(input("Enter step: "))
print("Sliced list:", li[start:stop:step])

seperator(7)
tu1 = (9, 3, 0, -4, 8, 7, 10, -1, 5)
val = int(input("Enter a value to count and find index: "))
print("Count of", val, "=", myFunctions.my_count(tu1, val))
print("Index of", val, "=", myFunctions.my_index(tu1, val))