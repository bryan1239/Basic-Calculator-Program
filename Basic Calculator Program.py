First_num = int(input("Enter first value: "))
Second_num = int(input("Enter second value: "))
Operator = input("Enter opertaion{/,*,+,-}: ")


if (Operator == "/"):
	if Second_num == 0:
		print ("Oops! Cannot divide by zero")
	else:
		output = First_num / Second_num
		print (f"{First_num} / {Second_num} = {output}")

elif (Operator == "*"):
	output = First_num * Second_num
	print (f"{First_num} * {Second_num} = {output}")

elif (Operator == "+"):
	output = First_num + Second_num
	print (f"{First_num} + {Second_num} = {output}")

elif (Operator == "-"):
	output = First_num - Second_num
	print (f"{First_num} - {Second_num} = {output}")

else:
	print ("Your operation doesn't exist")
