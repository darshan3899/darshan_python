'''WAP to print
3	2	1	*	
2	1	*	*
1	*	*	*
'''
#!/usr/bin/python
def pattern15(n):
	for i in range(1,n+1):
		for j in range(n-i+1,0,-1):
			print(j,end="")
		for _ in range(1,i+1):
			print("*",end="")
		print("")

def main():
	n=int(input("Enter a Number\n"))
	pattern15(n)

if __name__=='__main__':
	main()
