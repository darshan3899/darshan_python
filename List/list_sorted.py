#WAP to accept a list of integers from user and check if its sorted or not
#!/usr/bin/python
def isSorted(l):
	i=0
	while i+1 < len(l):
		if(l[i]>l[i+1]):
			return False
		i+=1
	return True
def main():
	l=eval(input("Enter List:"))
	print(isSorted(l))
if __name__=='__main__':
	main()

