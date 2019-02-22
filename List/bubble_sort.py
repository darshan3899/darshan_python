#WAP to implement Bubble Sort using list
#!/usr/bin/python
def bubbleSort(arr):
	temp=0
	n=len(arr)
	for i in range(0,n):
		#already_sorted=True
		for j in range(0,n-i-1):
			if arr[j]>arr[j+1]:
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp
				#already_sorted=False
	return arr
def main():
	arr=eval(input("Enter Array[]:"))
	bubbleSort(arr)
	print(arr)

if __name__=='__main__':
	main()
