'''
WAP to print
****
 ***
  **
   *
'''
#!/usr/bin/python
def pattern7(n):
	for i in range(n,0,-1):
		for _  in range(1,n-i+1):
			print(" ",end="")
		for _ in range(i):
			print("*",end="")
		print("")
	


def main():
	n=int(input("Enter a Number\n"))
	pattern7(n)

if __name__=='__main__':
	main()
