'''
WAP to print
1 3 
2 4 6 
3 5 7 9 
4 6 8 10 12 
5 7 9 11 13 15
'''
def pattern14(n):
	for i in range(1,n+1):
		k=i
		for _ in range(1,i+2):
			print(k,end=" ")
			k+=2
		print("")

def main():
	n=int(input("Enter Number of Rows\n"))
	pattern14(n)

if __name__=='__main__':
	main()
