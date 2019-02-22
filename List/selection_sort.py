#WAP to accept a list of numbers and sort 
#!/usr/bin/python
def selectionSort(l):
	n=len(l)
	temp=0
	for i in range(0,n):				#SELECTION SORT
		for j in range(i+1,n):
			if(l[i]>l[j]):
				temp=l[i]
				l[i]=l[j]
				l[j]=temp
	return l

def main():
	l=eval(input("Enter List:"))
	print(selectionSort(l))

if __name__=='__main__':
	main()
