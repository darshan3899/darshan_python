#WAP to count no of 1 bits in a given number
#!/usr/bin/python
def count1(n):
	count=0
	while n!=0:
		count+=1
		n=n&(n-1)
	return count

def main():
	n=int(input("Enter a Number\n"))
	print(count1(n))


if __name__=='__main__':
	main()
