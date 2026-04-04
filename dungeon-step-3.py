party_power = 12

name = input("Enter the dungeon name: ")

while True:
    #level_input = input("Enter the dungeon level: ")
    
    try:
        level = int(input("Enter the dungeon level: "))
        
        if level > 0:
            break
        else:
            print("Enter a positive number. Try again.")
            
    except:
        print("Invalid dungeon level. Try again.")

if level <= party_power:
    print("We can confidently explore", name + ".")
else:
    print("We cannot confidently explore", name + ".")