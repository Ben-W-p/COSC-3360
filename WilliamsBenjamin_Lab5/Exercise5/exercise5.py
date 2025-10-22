class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def getName(self):
        return self.name
    def getID(self):
        return self.ID
nameList = []
IDList = []
for i in range(2):
    print(f"Enter information for student {i+1}")
    nameList.append(input('Student Name: '))
    IDList.append(input('Student ID: '))
Student1 = Student(nameList[0], IDList[0])
Student2 = Student(nameList[1], IDList[1])
print('------------------------')
print("Student1: ")
print(f"ID: {Student1.getID()}")
print(f"Name: {Student1.getName()}")
print('------------------------')
print("Student2: ")
print(f"ID: {Student2.getID()}")
print(f"Name: {Student2.getName()}")
