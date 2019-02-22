#WAP to find GCD of two numbers
#!/usr/bin/python
def GCDRecursive(a,b):
	if a==b:
		return a
	if(a>b):
		return GCDRecursive(a-b,b)
	return GCDRecursive(a,b-a)

def main():
	a=int(input("Enter Number 1\n"))
	b=int(input("Enter Number 2\n"))
	print("GCD=",GCDRecursive(a,b))
if __name__=='__main__':
	main()
	
