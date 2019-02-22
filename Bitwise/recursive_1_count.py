#WAP to count no of one bits recursively
#!/usr/bin/python
def count_one(n):
	if n==0:
		return 0
	return 1+count_one(n&(n-1))
def main():
	n=int(input("Enter Number\n"))
	print(count_one(n))
if __name__=='__main__':
	main()
