#WAP to print fibonacci series upto n
def fibonacci(n):
	n1,n2=1,1
	print(n1,n2)
	n-=2
	while n!=0:
		n3=n1+n2
		print(n3)
		n1=n2
		n2=n3
		n-=1
	
def main():
	n=int(input("Enter n\n"))
	fibonacci(n)

if __name__=='__main__':
	main()
	
