'''WAP to print
		*
	*	*	*
*	*	*	*	*
'''
#!/usr/bin/python
def pattern3(n):
	for i in range(1,n+1):
		for _ in range(1,n-i+1):
			print("",end=" ")
		for _ in range(1,i*2):
			print("*",end="")
		print("")
	


def main():
	n=int(input("Enter a Number\n"))
	pattern3(n)

if __name__=='__main__':
	main()
	
