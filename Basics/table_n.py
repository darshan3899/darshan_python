#WAP to print the table of n numbers
#!/usr/bin/python
n=int(input("Enter a Number"))
for i in range(2,n+1):
	for j in range (1,11):
		print(i,'X',j,'=',(i*j))
	print("")
