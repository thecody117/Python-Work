repeat = "y"
#Asks what type of calculator to use.
print ("version 0.1")
while repeat.lower().strip() == 'y':
	math = input("What type do you want to do? add, multi, divide, or sub?")
	#Adds the numbers.
	if math == "add":
		num1 = int(input("What is the first number? "))
		num2 = int(input("Now the second number. "))
		print("The answer is", num1 + num2)
	elif math == "divide":
		num1 = int(input("What is the first number?"))
		num2 = int(input("Now the second number."))
		print("The answer is", num1 / num2)
	elif math == "sub":
		num1 = int(input("What is the first number?"))
		num2 = int(input("Now the second number."))
		print("The answer is", num1 - num2)
	elif math == "multi":
		num1 = int(input("What is the first number?"))
		num2 = int(input("Now the second number."))
		print("The answer is", num1 * num2)
	else:
		print ("not a supported function")
	repeat=input("Do you want to perform another calculation(yes or no)? ")