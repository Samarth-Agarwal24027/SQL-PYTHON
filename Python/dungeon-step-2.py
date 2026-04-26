#dungeon-program.py

#step-1

name = input("Enter the dungeon name: ")
party_power = 12
level = int(input("Enter the dungeon level: "))

if level <= party_power:
    print ("We can confidently explore " + name + ".")
else:
    print ("We cannot confidently explore " + name + ".")

