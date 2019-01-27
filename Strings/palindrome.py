#WAP to accept a string form user and check if it's palindrome
#!/usr/bin/python
s=str(input("Enter a String:"))
if s==s[::-1]:
	print("String is Palindrome")
else:
	print("String is not Palindrome")
