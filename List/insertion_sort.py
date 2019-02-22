#WAP to implement Insertion  Sort using list
#!/usr/bin/python
def insertionSort(arr):
	key=0
	n=len(arr)
	for i in range(n):
		key=arr[i]
		j=i-1
	
		while(j>=0 and arr[j]>key):
			arr[j+1]=arr[j]
			j=j-1
	arr[j+1]=key

def main():
	arr=eval(input("Enter Array[]:"))
	insertionSort(arr)
	print(arr)

if __name__=='__main__':
	main()
