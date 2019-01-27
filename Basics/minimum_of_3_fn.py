#WAP to accept three nos and print the minimum
#!/usr/bin/python
def min(a,b,c):
	if a<b and a<c:
		print(a)
	elif b<c:
		print(b)
	else:
		print(c)
	
a,b,c=eval(input("Enter 3 Numbers"))
min(a,b,c)
