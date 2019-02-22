#WAP to check if number is multiple of 512 without arithematic
def check512multiple(n):
	if((n&511)==0):
		return True
	else:
		return False

def main():
	n=int(input("Enter a Number\n"))
	print(check512multiple(n))

if __name__=='__main__':
	main()
