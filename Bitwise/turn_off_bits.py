#WAP to accept a number from user and bit position and number of bits to turn off from given number turn-off LSB->MSB
#!/usr/bin/python
def turnOffBits(n,bit,noBit):
	x=(1<<(noBit)-1)
	x=x<<(bit-noBit)
	x=~x
	return(n&x)	
	
def main():
	n=int(input("Enter a Number\n"))
	bit=int(input("Enter bit to Turn Off\n"))
	noBit=int(input("Enter Number of Bits to Turn Off\n"))
	print(turnOffBits(n,bit,noBit))
if __name__=='__main__':
	main()
	
