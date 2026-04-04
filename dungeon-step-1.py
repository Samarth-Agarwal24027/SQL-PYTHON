#dungeon-program.py

#step-1
party_power = 12
level = int(input("Enter the dungeon level: "))

if level <= party_power:
    print ("We can confidently explore.")
else:
    print ("We cannot confidently explore.")

