try:
	with open("Sample.txt", "r") as f:
		print(f.read());
except IOError:
	print("File not found...!")