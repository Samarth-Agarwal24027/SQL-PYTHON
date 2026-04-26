# dungeon-program.py

#variable defination
party_power = 12

# declare a list to capture dungeon name & level
dungeons = []

while True:
    # variable to capture dungeon name as input
    name = input("Enter the dungeon name: ")

    while True:
        # variable to capture dungeon level as input
        level_input = input("Enter the dungeon level: ")

        try:
            # convert input value to int
            level = int(level_input)

            # check if dungeon level is a positive number or not
            if level > 0:
                break
            else:
                print("Enter a positive number. Try again.")

        except:
            # capture invallid entries like string or specialll charaters
            print("Invalid dungeon level. Try again.")

    # append the list to capture dungeon name & level
    dungeons.append((name, level))

    # check for name "Polaris" only
    if name == "Polaris":
        break

# check dungeon name & level at each iteration
for name, level in dungeons:
    if level <= party_power:
        print("We can confidently explore", name + ".")
    else:
        print("We cannot confidently explore", name + ".")