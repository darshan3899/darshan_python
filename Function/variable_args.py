#WAP to ADD using variable number of arguments
#!/usr/bin/python
def Add(*args):
	print(type(args))
	print(args)
	result=0
	for i in args:
		result+=i
	return result
	
def main():
	print(Add(1,2))
	print(Add(1,2,3))
	print(Add(1,2,3,4))
	print(Add(1,2,3,4,5))

if __name__=='__main__':
	main()
