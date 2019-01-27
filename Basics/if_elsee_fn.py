#WAP to accept no of donuts.If no of donuts is greater than 10 print-No of Donuts is many....Else print-No of donuts is (count)
#!/usr/bin/python
def donut(a):
	if a>10:
		print("Number of Donuts:MANY")
	else:
		print("Number of Donuts:",a)

a=int(input("Enter Number of Donuts"))	
donut(a)
