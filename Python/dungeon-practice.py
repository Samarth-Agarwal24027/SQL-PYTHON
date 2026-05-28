party_power = 12
dungeons = []

while True:
    name = input("Enter Dungeon Name: ")
    while True:
        level_input = input("Enter the Dungeon level: ")
        try:
            level = int(level_input)
            if level > 0:
                break
            else:
                print("Enter a positive number. Try again.")
        except:
            print("Invalid Dungeon level. Try again: ")
    dungeons.append((name, level))
    if name == "Polaris":
        break

for name, level in dungeons:
    if level <= party_power:
        print("We can confidently explore " + name + "." )
    else:
        print("We can confidently explore " + name + ".")