#WAP to calulate length of string recursively
#!/usr/bin/python	
def length(s):
	if s=="":
		return 0
	return 1+length(s[1:])
def main():
	s=str(input("Enter String\n"))
	print(length(s))
if __name__=='__main__':
	main()
