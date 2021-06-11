s1 = input("Enter first string: ");
s2 = input("Enter second string: ");

s3 = s1[0: int(int(len(s1))/2)] + s2 + s1[int(int(len(s1))/2): int(int(len(s1))-1)]

print(s3);