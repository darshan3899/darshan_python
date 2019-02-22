#WAP to Multiply 2,3,4,5 numbers
#!/usr/bin/python
def Mul(a,b,c=1,d=1,e=1):
 	return a*b*c*d*e
 	
def main():
	print(Mul(10,5))
	print(Mul(10,5,20))
	print(Mul(10,5,2,3))
	print(Mul(10,5,4,6,2))

if __name__=='__main__':
	main()
