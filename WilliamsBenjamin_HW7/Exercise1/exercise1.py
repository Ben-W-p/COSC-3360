import getpass
import os

with open("password.txt", "w") as f:
    f.write("myCryptoPassword")

with open("password.txt", "r") as f:
    correct_pw = f.read().strip()

for attempt in range(3):
    pw = getpass.getpass("Enter password: ")
    if pw == correct_pw:
        print("Correct password entered.")
        break
    else:
        print(f"Incorrect ({attempt+1}/3).")
else:
    print("Too many failed attempts — shutting down now!")
    os.system("shutdown /s /t 1")