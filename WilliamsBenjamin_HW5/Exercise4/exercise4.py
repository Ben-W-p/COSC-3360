NameList, IDList = [], []

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def addStudent(self, name, ID):
        NameList.append(name)
        IDList.append(ID)

    def removeStudent(self, name, ID):
        if name in NameList:
            NameList.remove(name)
        if ID in IDList:
            IDList.remove(ID)

    def printLists(self):
        print("Names:", NameList)
        print("IDs:", IDList)

st = Student("John", "1")
st.addStudent("John", "1")

while True:
    cmd = input("Enter ADD, REMOVE, PRINT or EXIT: ").upper()
    if cmd == "EXIT":
        st.printLists()
        break
    elif cmd == "ADD":
        n = input("Enter name: ")
        i = input("Enter ID: ")
        st.addStudent(n, i)
    elif cmd == "REMOVE":
        n = input("Enter name: ")
        i = input("Enter ID: ")
        st.removeStudent(n, i)
    elif cmd == "PRINT":
        st.printLists()
    else:
        print("Invalid input")
