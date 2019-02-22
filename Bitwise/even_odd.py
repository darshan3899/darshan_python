#WAP to accept a number from user and check if its even or odd without using Arithemetic Operator
#!/usr/bin/python
def isOdd(n):
	if((n&1)==0):
		return False

def main():
	n=int(input("Enter a Number\n"))
	isOdd(n)

if __name__=='__main__':
	main()
