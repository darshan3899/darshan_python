#WAP to accept three nos and print the minimum
#!usr/bin/python
a,b,c=eval(input("Enter 3 Numbers"))
if a<b and a<c:
	print(a)
elif b<c:
	print(b)
else:
	print(c)
