#WAP to Add 2,3,4,5 numbers
#!/usr/bin/python
def Add(a,b,c=0,d=0,e=0):
	return a+b+c+d+e


def main():
	print(Add(10,20,30,40))
	print(Add(10,20))
	print(Add(10,20,50))
	print(Add(10,20,30,40,50))
	

if __name__=='__main__':
	main()
