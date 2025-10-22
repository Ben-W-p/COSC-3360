import matplotlib.pyplot as plt

COSC1310grades = {"HW1": 35, "HW2": 49, "HW3": 74, "HW4": 67, "HW5": 75}
COSC3360grades = {"HW1": 89, "HW2": 93, "HW3": 74, "HW4": 82, "HW5": 93}

x1, y1 = list(COSC1310grades.keys()), list(COSC1310grades.values())
x2, y2 = list(COSC3360grades.keys()), list(COSC3360grades.values())

plt.plot(x1, y1, label="COSC1310", color='red', linewidth='2')
plt.plot(x2, y2, label="COSC3360", color='blue', linewidth='2')
plt.ylim(0, 100)
plt.xlabel("Assignments")
plt.ylabel("Grades")
plt.title("Grades Comparison")
plt.legend()
plt.show()
