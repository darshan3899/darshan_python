#WAP to reverse string  using recursion
#!/usr/bin/python
def reverseString(l):
	if len(l)==0:
		return l
	x=reverseString(l[1:])
	return x+l[0]

def main():
	l=str(input("Enter String:"))
	print(reverseString(l))
if __name__=='__main__':
	main()
