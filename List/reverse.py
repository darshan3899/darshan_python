#WAP to accept a list form user and print it in reverse order using recursion
#!/usr/bin/python
def reverseList(l):
	if len(l)==0:
		return
	reverseList(l[1:])
	print(l[0])

def main():
	l=eval(input("Enter List:"))
	reverseList(l)
if __name__=='__main__':
	main()
