#WAP to check if number is multiple of 8 without arithematic
def check8multiple(n):
	if((n&7)==0):
		return True
	else:
		return False

def main():
	n=int(input("Enter a Number\n"))
	print(check8multiple(n))

if __name__=='__main__':
	main()
