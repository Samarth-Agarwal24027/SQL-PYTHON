party_power = 12
dungeon = []
while True:
    name = input("Enter the Dungeon Name: ")
    while True:
        try:
            level = int(input("Enter the Dungeon Level: "))
            if level > 0:
                break
            else:
                print("Enter a positive number. Try again.")
        except:
            print("Invalid input. Try again.")
    dungeon.append((name, level))
    if name == "Polaris":
        break
    for name, level in dungeon:
        if level <= party_power:
            print("We can confidently explore " + name + ".")
        else:
            print("We cannot confidently explore " + ".")