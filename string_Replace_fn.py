#WAP to accept a string from user and repalce the occurance of first letter with *
#!/usr/bin/python
def str_replace(s):
	print(s[0]+s[1:].replace(s[0],"*"))
	
s=str(input("Enter a String"))
str_replace(s)

