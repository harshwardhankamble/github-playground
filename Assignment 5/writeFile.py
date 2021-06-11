try:
	while True:
		name = input("Name of Company:");
		founded = input("Established year: ");
		industry = input("Type of industry:")
		with open("Info.txt", "a") as f:
			str = "\nName: " + name + "\nFounded on: " + founded + "\nIndustry: " + industry;
			f.write(str);
		con = input("You want add more data(Y/N)");
		if con == "N" or con == "n":
			break;
except IOError:
	print("File not found...!");

print("---------------BSE------------");

try: 
	with open("Info.txt", "r") as f:
		print(f.read());
except IOError:
	print("File not found...!");