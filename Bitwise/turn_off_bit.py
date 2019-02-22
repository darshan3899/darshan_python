#WAP to accept a number from user and bit position to turn off from given number turn-off LSB->MSB
#!/usr/bin/python
def turnOffBit(n,bit):
	x=1
	x=x<<(bit-1)
	x=~x
	return(n&x)

def main():
	n=int(input("Enter a Number\n"))
	bit=int(input("Enter bit to Turn Off\n"))
	print(turnOffBit(n,bit))

if __name__=='__main__':
	main()
