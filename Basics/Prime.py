#WAP to check if number is prime
#!/usr/bin/python
import math
def prime(n):
	count=0
	for i in range(1,int(math.sqrt(n)),2):
		if n%2!=0:
			if n%i==0:
				count+=1
	return count

def main():
	n=int(input("Enter a Number:"))
	cnt=prime(n)	
	if cnt==1:
		print("Prime Number")
	else:
		print("Not Prime")
	
if __name__=='__main__':
	main()
