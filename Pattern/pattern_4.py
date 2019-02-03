'''WAP to print 
		1
	2	1	2
3	2	1	2	3
'''
#!/usr/bin/python
def pattern4(n):
	for i in range(1,n+1):
		a=i
		for _ in range(1,n-i+1):
			print(" ",end=" ")
		for j in range(1,i*2):
			print(a,end=" ")
			if j<i:
				a=a-1
			else:
				a=a+1
		print("")

def main():
	n=int(input("Enter Rows\n"))
	pattern4(n)

if __name__=='__main__':
	main()
