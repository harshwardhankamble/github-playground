import csv 
Details = ['Name', 'Class', 'Passout Year', 'Subject']  
rows = [ ['Harsh', '2nd', '2023', 'Physics'],
  ['John', '3rd', '2022', 'M2'],  
  ['Mayur', '4th', '2021', 'ML'],
  ['Adinath', '4th', '2021', 'C++'],
  ['Aditya', '4th', '2021', 'FDS']] 
try:
	with open('student.csv', 'w') as f: 
	    write = csv.writer(f) 
	    write.writerow(Details) 
	    write.writerows(rows) 
except IOError:
	print("File not found...!");
finally:
	print("Data written successfully...!")