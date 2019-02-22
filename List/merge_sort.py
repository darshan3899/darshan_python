#WAP to accept Two lists form user sort them and merge the sorted lists element by element preserving the sort order
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

def mergeSort(l1,l2):
	bubbleSort(l1)
	bubbleSort(l2)
	l3=[]
	i,j=0,0
	while(i<len(l1) and j<len(l2)):
		if(l1[i]<l2[j]):
			l3.append(l1[i])
			i+=1
		elif(l2[j]<l1[i]):
			l3.append(l2[j])
			j+=1
		elif(l1[i]==l2[j]):
			l3.append(l1[i])
			i+=1
			
	if(i<len(l1)):
		#l3.append(l1[i])
		#i+=1
		l3.extend(l1[i:])
		
	if(j<len(l2)):
		#l3.append(l2[j])
		#j+=1
		l3.extend(l2[j:])
	return l3
			
def main():
	l1,l2=eval(input("Enter Lists:"))
	print(mergeSort(l1,l2))

if __name__=='__main__':
	main()
