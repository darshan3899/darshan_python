#WAP to ADD,SUBTRACT,MULTIPLY,DIDIDE
#!/usr/bin/python

def add(a,b):
	return a+b+10
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b
	
def main():
	a,b=eval(input("Enter 2 Numbers:"))
	print("ADDITION:",add(a,b))
	print("SUBTRACTION:",subtract(a,b))
	print("MULTIPLICATION:",multiply(a,b))
	print("DIVISION:",divide(a,b))

if __name__=='__main__':
	main()
	


	
