from Lab2.myFunctions import addition, subtraction, multiplication, division

float1 = float(input("Enter a float: "))
float2 = float(input("Enter another float: "))

while True :
    operation = input("Enter an operation(+,-,*, or /): ")
    resultString  = f'{float1} {operation} { float2} = '
    if operation == "+":
        print (resultString + str(addition(float1, float2)))
        break
    if operation == "-":
        print (resultString + str(subtraction(float1, float2)))
        break
    if operation == "*":
        print (resultString + str(multiplication(float1, float2)))
        break
    if operation == "/":
        print (resultString + str(division(float1, float2)))
        break
    print("invalid operation")

