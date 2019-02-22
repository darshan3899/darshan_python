#WAP recursive program to find factorial

def recursiveFactorial(a):
	if a==0 or a==1:
		return 1
	if a==2:
		return 2
	return(a*recursiveFactorial(a-1))

def main():
	a=int(input("Enter A Number\n"))
	print(recursiveFactorial(a))
	
if __name__=='__main__':
	main()
