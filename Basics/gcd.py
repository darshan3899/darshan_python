#WAP to find GCD of two numbers
#!/usr/bin/python
def GCD(a,b):
	while(a!=b):
		if a>b:
			a=a-b
		else:
			b=b-a
	return a

def main():
	a=int(input("Enter Number 1\n"))
	b=int(input("Enter Number 2\n"))
	print("GCD=",GCD(a,b))
	
if __name__=='__main__':
	main()
	
