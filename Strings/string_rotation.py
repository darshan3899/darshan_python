#WAP to Check if string is rotation of another
#!/usr/bin/python
s=str(input("Enter The String"))
s1=str(input("Enter Rotation to Check"))
if len(s1)==len(s):
	print(s1 in s+s)
else:
	print("False")

