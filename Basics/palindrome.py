#WAP to accept a number form user and check if it's palindrome
#!/usr/bin/python
def palindrome(a):
	temp=0
	rem=0
	n=a
	while n>0:
		rem=n%10
		temp=temp*10+rem
		n=n//10
	if (temp==a):
		print("Palindrome")
	else:
		print("Not Palindrome")
	
def main():
	a=int(input("Enter a Number:"))
	palindrome(a)
	
	
if __name__=='__main__':
	main()
	
