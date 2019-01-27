#WAP to Check if string is rotation of another
#!/usr/bin/python
def rotation(s,s1):
	if len(s1)==len(s):
		print(s1 in s+s)
	else:
		print("False")
		
s=str(input("Enter The String"))
s1=str(input("Enter Rotation to Check"))
rotation(s,s1)

