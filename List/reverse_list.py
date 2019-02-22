#WAP to reverse list using recursion
#!/usr/bin/python
def reverseList(l):
	if len(l)==0:
		if type(l)==str:
			return l
		return list()
	x=reverseList(l[1:])
	if type(l)==str:
		return x+l[0]
	x.append(l[0])
	return x

def main():
	l=eval(input("Enter List:"))
	print(reverseList(l))
if __name__=='__main__':
	main()
