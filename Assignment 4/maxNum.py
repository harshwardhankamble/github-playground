first = int(input("Enter first number:"));
sec = int(input("Enter second number:"));
third = int(input("Enter third number:"));

if  first > sec:
	if first > third:
		print(first);
	else:
		print(third);
else:
	if sec > third:
		print(sec);
	else:
		print(third);