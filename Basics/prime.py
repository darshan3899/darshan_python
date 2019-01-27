#WAP to check if number is prime
#!/usr/bin/python
def prime(n):
	count=0
	for i in range(1,n+1):
		if n%2!=0:
			if n%i==0:
				count+=1
	if count==2:
		print("Prime Number")
	else:
		print("Not Prime") 

def main():
	n=int(input("Enter a Number:"))
	prime(n)	
	
if __name__=='__main__':
	main()
