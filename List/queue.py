#WAP to implement queue using list
#!/usr/bin/python
def enqueue(list1,add):
	return(list1.append(add))
	
def dequeue(list1):
	return(list1.pop(0))

def isFull(list1):
	return list1==10
	
def isEmpty(list1):
	return list1==[]


def main():
	list1=eval(input("Enter List:"))
	ch=1
	while ch!=0:
		print("1.Enqueue\n2.Dequeue\n3.Is Full\n4.Is Empty")
		ch=int(input("Enter Choice:"))
		if ch==1:
			add=eval(input("Enter Number to Add:"))
			enqueue(list1,add)
			print(list1)
			
		if ch==2:
			dequeue(list1)
			print(list1)
			
		if ch==3:
			print(isFull(list1))
			
		if ch==4:
			print(isEmpty(list1))
if __name__=='__main__':
	main()
