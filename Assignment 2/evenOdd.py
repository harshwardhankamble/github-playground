while(True):
	inputVal = int(input("Enter the number: "));
	if inputVal % 2 == 0:
		print(inputVal, " is Even");
	else:
		print(inputVal, " is Odd");

	exitOrNot = input("You want exit (Y/N): ");
	if exitOrNot == "Y" or exitOrNot == "y":
		break;