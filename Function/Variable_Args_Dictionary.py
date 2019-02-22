#WAP to use VARIABLE ARGS DICTIONARY
#!/usr/bin/python
def VariableArgsDictionary(a,b,*args,**kwargs):
	print(a,b)
	print(type(args),type(kwargs))
	for x in args:
		print(x)
	for x in kwargs:
		print(x,kwargs[x])

def main():
	VariableArgsDictionary(10,20,1,2,3,4,5,6,7,name="DARSHAN",hobby="T")

if __name__=='__main__':
	main()
