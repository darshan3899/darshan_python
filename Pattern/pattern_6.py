'''
WAP to print
****
***
**
*
'''
#!/usr/bin/python
def pattern6(n):
	for i in range(n,0,-1):
		for _ in range(i):
			print("*",end="")
		print("")

def main():
	n=int(input("Enter Number of Rows"))
	pattern6(n)

if __name__=='__main__':
	main()

