#WAP to accept a string form user and check if it's palindrome
#!/usr/bin/python
def palindrome(s):
	if s==s[::-1]:
		print("String is Palindrome")
	else:
		print("String is not Palindrome")	

def main():
	s=str(input("Enter a String:"))
	palindrome(s)
	
if __name__=='__main__':
	main()	
	



