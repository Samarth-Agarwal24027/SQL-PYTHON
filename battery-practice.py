name = input("Enter the Dungeon name: ")
party_power = 12
level = int(input("Enter the Dungeon level: "))
if level <= party_power:
	print("We can confidently explore  " + name + ".")
else:
	print("We cannot confidently explore " + name + ".")