students = [];

try:
	file = open("Student.txt", "r");
	flag = 1;
	while True:
		line = file.readline();

		if not line:
			break;
		arr = line.split(",");
		students.append(arr);

	file.close();
except IOError:
	print("File not found...!");

for data in students:
	print(data);