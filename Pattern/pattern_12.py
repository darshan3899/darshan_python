'''
WAP to print
*	*	*	*	*	*	*
*	*	*		*	*	*
*	*				*	*
*						*
*	*				*	*
*	*	*		*	*	*
*	*	*	*	*	*	*
'''
#!/usr/bin/python
def pattern11(n):
	for _ in range(1,2*n):
		print("*",end=" ")
	print("")	
	
	for i in range(1,2*n):
		for _ in range(1,n-i+1):
			print("*",end=" ")
		for _ in range(1,i*2):
			print(" ",end=" ")
		for _ in range(1,n-i+1):
			print("*",end=" ")
		print("")
		
	for i in range(n,)
		
			
def main():
	n=int(input("Enter Number of Rows\n"))
	pattern11(n)
	
if __name__=='__main__':
	main()
