#WAP to print string in reverse order using recursion
#!/usr/bin/python
def reverseString(l):
	if len(l)==0:
		return
	reverseString(l[1:])
	print(l[0])

def main():
	l=str(input("Enter String:"))
	reverseString(l)
if __name__=='__main__':
	main()
