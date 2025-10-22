catalog = {'Johnny': [120, 3.5], 'Mary': [71, 3.73], 'Jimmy': [15, 2.9], 'Crystal': ['103', 3.15]}


name = input("Enter a name to search: ").strip()
if name in catalog:
    credits, gpa = catalog[name]
    print(f"Name: {name}")
    print(f"Credits Earned: {credits}")
    print(f"GPA: {gpa}")
else:
    print(f"{name} Not Found")
