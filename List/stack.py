#WAP to perform stack opertions on list
#!/usr/bin/python
def push(list1,add):
	return(list1.append(add))
	
def pop(list1):
	list1.pop()
	return list1
	
def peep(list1):
	return list1[-1]

def isFull(list1):
	return len(list1)==10
	
def isEmpty(list1):
	return list1==[]
		
def main():
	list1=eval(input("Enter List:"))
	ch=1
	while ch!=0:
		print("1.Push\n2.Pop\n3.Peep\n4.Is Full\n5.Is Empty")
		ch=int(input("Enter Choice:"))
		if ch==1:
			add=eval(input("Enter Number to PUSH:"))
			push(list1,add)
			print(list1)
		if ch==2:
			pop(list1)
			print(list1)

		if ch==3:
			print(peep(list1))
			
		if ch==4:
			print(isFull(list1))
		
		if ch==5:
			print(isEmpty(list1))

if __name__=='__main__':
	main()
