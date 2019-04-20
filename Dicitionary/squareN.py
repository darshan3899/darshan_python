#WAP to accept number form user and return a dictionary of squares from 1 to n
#!/usr/bin/python
def square(n):
	result=dict()
	for x in range(1,n+1):
		result[x]=x*x
	return result
	
def main():
	n=int(input("Enter a Number:"))
	out=square(n)
	for x in out:
		print(x,out[x])

if __name__=='__main__':
	main()
