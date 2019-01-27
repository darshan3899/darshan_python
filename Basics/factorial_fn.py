#WAP to accept a number form user and find it's factorial usnig function
def factorial(a):
	fact=1;
	for i in range (1,a+1):
		fact=fact*i;
	return fact

a=int(input("Enetr a Number "))
print (factorial(a))
