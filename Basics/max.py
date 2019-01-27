#WAP to print maximum of three numbers
#!usr/bin/python
a,b,c=eval(input("Enter 3 Nos "))
if a>b and a>c:
	print(a)
elif b>c:
	print(b)
else:
	print(c)
