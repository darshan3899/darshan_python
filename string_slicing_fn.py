#WAP to accept strin gfrom user and return a string having first 2 and last 2 characters of i/p string
#!/usr/bin/python
def slice(s):
	s=s[:2]+s[-2:]
	return s
s=str(input("Enter a String"))
print(slice(s))
