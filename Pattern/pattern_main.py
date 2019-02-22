#WAP to print Patterns
#!usr/bin/python

def Menu():
	choice=0
	pattern_1="""
	1.
	*
	*	*
	*	*	*
	*	*	*	*
	"""
	print (pattern_1)
	pattern_2="""
	2.
			*
		*	*
	*	*	*	
	"""
	print (pattern_2)
	
	pattern_3="""
	3.
		*
	*	*	*
*	*	*	*	*
	"""
	print (pattern_3)

	pattern_4="""
	4.
		1
	2	1	2
3	2	1	2	3
	"""
	print (pattern_4)
	
	pattern_5="""
	5.
		A
	B	A	B
C	B	A	B	C
	"""
	print (pattern_5)
	pattern_6="""
	6.
	*	*	*	*	
	*	*	*	
	*	*
	*
	"""
	print (pattern_6)
	
	pattern_7="""
	7.
	****
	 ***
	  **
	   *
	"""
	print (pattern_7)

	pattern_8="""
	8.
		* 
	  * * * 
	* * * * * 
	* * * * * 
	  * * * 
		*
	"""
	print (pattern_8)
	

	pattern_9="""
	9.
		*
	*	*	*
*	*	*	*	*
	*	*	*	
		*
	"""
	print (pattern_9)
	
	pattern_10="""
	10.
*	*	*	*	*	*	*
*	*	*		*	*	*
*	*				*	*
*						*
	"""
	print (pattern_10)
	pattern_11="""
	11.
	1	2
	2	4	8
	3	6	12	24
	4	8	16	32	64
	"""
	print (pattern_11)
	pattern_12='''
	12.
	1 	3 
	2 	4 	6 
	3 	5	7 	9 
	4 	6 	8 	10 	12 
	5 	7 	9 	11 	13 	15	
	'''
	print (pattern_12)	
	
	pattern_13='''
	3	2	1	*	
	2	1	*	*
	1	*	*	*
'''
	print(pattern_13)
	print("14.Exit")
	choice=int(input("Enter Choice"))
	return choice
	
def PATTERN(choice,n):
	if choice==1:
		for i in range(n):
			for _ in range(i+1):
				print("*",end=" ")
			print("")	
	
	if choice==2:
		for i in range(1,n+1):
			for _ in range(1,n-i+1):
				print(" ",end="")
			for _ in range(1,i+1):
				print("*",end="")
			print("")
	
	if choice==3:
		for i in range(1,n+1):
			for _ in range(1,n-i+1):
				print(" ",end="")
			for _ in range(1,i*2):
				print("*",end="")
			print("")
			
	if choice==4:
		for i in range(1,n+1):
			a=i
			for _ in range(1,n-i+1):
				print(" ",end="")
			for j in range(1,i*2):
				print(a,end="")
				if j<i:
					a=a-1
				else:
					a=a+1
			print("")
			
	if choice==5:
		for i in range(1,n+1):
			a=i
			for _ in range(1,n-i+1):
				print(" ",end="")
			for j in range(1,i*2):
				print(chr(a+64),end="")
				if j<i:
					a=a-1
				else:
					a=a+1
			print("")			
			
	if choice==6:
		for i in range(n,0,-1):
			print("*",end="")
		print("")
		
	if choice==7:
		for i in range(n,0,-1):
			for _ in range(1,n-i+1):
				print(" ",end="")
			for _ in range (i):
				print("*",end="")
			print("")
	
	if choice==8:
		for i in range(1,n+1):
			for _ in range(1,n-i+1):
				print(" ",end=" ")
			for _ in range(1,i*2):
				print("*",end=" ")
			print("")
		for i in range(n,0,-1):
			for _ in range(1,n-i+1):
				print(" ",end=" ")
			for _ in range(1,i*2):
				print("*",end=" ")
			print("")	
			
	if choice==9:
		for i in range(1,n+1):
			for _ in range(1,n-i+1):
				print(" ",end="")
			for _ in range(1,i*2):
				print("*",end="")
			print("")
		for i in range(n-1,0,-1):
			for _ in range(1,n-i+1):
				print(" ",end="")
			for _ in range(i*2,1,-1):
				print("*",end="")
			print("")
			
	if choice==10:
		for _ in range(1,2*n):
			print("*",end=" ")
		print("")
		
		for i in range(1,2*n):
			for _ in range(1,n-i+1):
				print("*",end=" ")
			for _ in range(1,i*2):
				print(" ",end=" ")
			for _ in range(1,n-i+1):
				print("*",end=" ")
			print("")
			
	if choice==11:
		for i in range(1,n+1):
			k=i
			for _ in range(1,i+2):
				print(k,end=" ")
				k*=2
			print("")
		
	if choice==12:
		for i in range(1,n+1):
			k=i
			for _ in range(1,i+2):
				print(k,end=" ")
				k+=2
			print("")
	if choice==13:
		for i in range(1,n+1):
			for j in range(n-i+1,0,-1):
				print(j,end="")
			for _ in range(1,i+1):
				print("*",end="")
			print("")
def main():
	n=int(input("Enter Number of Rows\n"))
	choice=0
	choice=Menu()
	PATTERN(choice,n)

if __name__=='__main__':
	main()

