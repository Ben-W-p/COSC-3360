import pandas as pd

grades_dict = {
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}
grades = pd.DataFrame(grades_dict)
grades.index = ["Test1", "Test2", "Test3"]

print("Original DataFrame:\n", grades, "\n")

axis = int(input("Enter axis (0 for rows, 1 for columns): "))
by = input("Enter the name to sort by (student name or test label): ")
ascending = input("Sort ascending? (True/False): ").strip().capitalize() == "True"

sorted_grades = grades.sort_values(by=by, axis=axis, ascending=ascending)

print("\nSorted DataFrame:\n", sorted_grades)
