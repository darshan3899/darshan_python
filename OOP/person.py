
class Person:
	def __init__(self,name,address,dob):
		self.__name=name
		self.__address=address
		self.__dob=dob

	#getter methods
	def getName(self):
		return self.__name

	def getAddress(self):
		return self.__address

	def getDOB(self):
		return self.__dob
		
	#setter methods
	def updateAddress(self,address):
		self.__address=address
