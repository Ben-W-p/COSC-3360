numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2]

def myFind(lst, target):
    listIndex = []
    for i, v in enumerate(lst):
        if v == target:
            listIndex.append(i)
    return listIndex

user_in = int(input("Enter a number to find: "))

result = myFind(numbers, user_in)
print("Original list:", numbers)
print(f"Indices where {user_in} occurs:", result if result else "Not found")
