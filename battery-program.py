# battery-test

voltages = []

while True:
	user = input("Enter your input: ")

	try:
		# convert to float
		user = float(user)

	except:
		print("Not robot compliant!")
		continue

	if (user < 0):
		break

	voltages.append(user)
	#if (user >= 1.2):
		#print("Beep")
	#else:
		#print("Boop")


for v in voltages:
	if v >= 1.2:
		print("Beep")
	else:
		print("Boop")