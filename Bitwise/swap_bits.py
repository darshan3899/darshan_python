#WAP to accept two nos from user,accept no of bits and position and swap corresponding bits of both the numbers
#!/usr/bin/python

#1512	10111101000
#1234	10011010010
#pos=7	bits=4
def swapBits(x,y,pos,bits):
	mask=(1<<bits)-1			#000000001111
	mask=mask<<(pos-bits)		#000011110000
	
	x_part=x&mask				#000011010000
	y_part=y&mask				#000010100000
	
	x=x&~mask
	y=y&~mask
	
	x=x|y_part
	y=y|x_part
	return x,y

def main():
	x=int(input("Enter x\n"))
	y=int(input("Enter y\n"))
	pos=int(input("Enter Position\n"))
	bits=int(input("Enter Bits\n"))
	X,Y=swapBits(x,y,pos,bits)
	print("x=",X)
	print("y=",Y)
if __name__=='__main__':
	main()

