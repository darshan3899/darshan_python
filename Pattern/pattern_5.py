'''
WAP to print
		A
	B	A	B
C	B	A	B	C
'''
#!/usr/bin/python
def pattern5(n):
	for i in range(1,n+1):
		a=i
		for _ in range(1,n-i+1):
			print(" ",end=" ")
		for j in range(1,i*2):
			print(chr(a+64),end=" ")
			if j<i:				
				a=a-1
			else:
				a=a+1
		print("")
	


def main():
	n=int(input("Enter Number of Rows\n"))
	pattern5(n)


if __name__=='__main__':
	main()
	
