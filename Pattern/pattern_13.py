'''
WAP to print
1	2
2	4	8
3	6	12	24
4	8	16	32	64
'''
def pattern13(n):
	for i in range(1,n+1):
		k=i
		for _ in range(1,i+2):
			print(k,end=" ")
			k*=2
		print("")

def main():
	n=int(input("Enter Number of Rows\n"))
	pattern13(n)

if __name__=='__main__':
	main()
