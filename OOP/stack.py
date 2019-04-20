class Stack:
	def __init__(self,size):							#self->reference to calling object
		print("Stack Constructed of Size %d"%size)
		self.__stack=[]									#.__stack->__ makes the variable private
		self.__size=size
	
	def __del__(self):
		del self.__stack
		print("Stack Destructed")

	def push(self,data):
		status="FAILED"
		if not self.isFull():
			self.__stack.append(data)
			status="SUCCESS"
		return status

	def pop(self):
		status="FAILED"
		data=-1
		if not self.isEmpty():
			data=self.__stack.pop()
			status="SUCCESS"
		return data,status

	def isFull(self):
		return(len(self.__stack)==(self.__size))

	def isEmpty(self):
		return self.__stack==[]

def main():
	st=Stack(10)
	#print(st.size)					#error because size is private
	print(st._Stack__size)			#prints size (accessing private data out of class)
	st.push(200) 
	#print("object dictionary",st.__dict__)			#print object dictionary
	#print("class dictionary",Stack.__dict__)		#print class dictionary
	print(st.pop())
if __name__=='__main__':
	main()