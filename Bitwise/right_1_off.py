#WAP to accept a number from user and turn of right most 1 bit
#!/usr/bin/python
def rightMostOff(n):
	return n&(n-1)				#x=1
								#while (n&x)==0:
									#x=x<<1
	              				#return n&~x
def main():
	n=int(input("Enter Number\n"))
	print(rightMostOff(n))

if __name__=='__main__':
	main()
