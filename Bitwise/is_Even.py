#WAP to accept a number from user and check if its even or odd without using Arithemetic Operator
#!/usr/bin/python
def isEven(n):
	if((n&1)==0):
		return True
	else:
		return False

def main():
	n=int(input("Enter A Number\n"))
	print(isEven(n))

if __name__=='__main__':
	main()
