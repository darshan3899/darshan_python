#WAP to print fibonacci series upto n terms
def fibonacci(n):
	n1,n2=1,1
	print(n1)
	print(n2)
	n3=0
	while n3<=n:
		print(n3)
		n1=n2
		n2=n3
		n3=n1+n2
def main():
	n=int(input("Enter n\n"))
	fibonacci(n)

if __name__=='__main__':
	main()
	
