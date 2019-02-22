#WAP to accept two nos from user,accept no of bits and two diffrent positions and swap corresponding bits of both the numbers
#!/usr/bin/python
def swapBits(x,y,pos_x,pos_y,bits):
	mask_x=(1<<bits)-1
	mask_x=mask_x<<(pos_x-bits)
	mask_y=(1<<bits)-1
	mask_y=mask_y<<(pos_y-bits)
	
	x_part=x&mask_x
	y_part=y&mask_y
	
	if(pos_x>pos_y):
		x_part=x_part>>(pos_x-pos_y)
		y_part=y_part<<(pos_x-pos_y)
	else:
		x_part=x_part<<(pos_y-pos_x)
		y_part=y_part<<(pos_y-pos_x)
	
	x=x&~mask_x
	y=y&~mask_y
	
	x=x|y_part
	y=y|x_part
	
	return x,y

def main():
	x=int(input("Enter x\n"))
	y=int(input("Enter y\n"))
	pos_x=int(input("Enter Position of x\n"))
	pos_y=int(input("Enter Position of y\n"))
	bits=int(input("Enter Bits\n"))
	X,Y=swapBits(x,y,pos_x,pos_y,bits)
	print("x=",X)
	print("y=",Y)
if __name__=='__main__':
	main()

