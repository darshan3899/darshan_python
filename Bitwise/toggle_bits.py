#WAP to accept bit position and no of bits to toggle from given position 
#!/usr/bin/python
def toggleBits(n,pos,bits):
	x=(1<<bits)-1
	x=x<<(pos-bits)
	return n^x
	
def main():
	n=int(input("Enter A Number\n"))
	pos=int(input("Enter Bit Position\n"))
	bits=int(input("Enter Number of Bits\n"))
	print(toggleBits(n,pos,bits))

if __name__=='__main__':
	main()
