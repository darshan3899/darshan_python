'''
WAP to implement Student Management System (implement a class student):name,address,dob,course,div,list of marks	Write getter and setter methods 
1.Add Student
2.Susupend Student
3.Update Address
4.Update Marks
5.Print all student details & their %
USE INHERITANCE
'''
#!/usr/bin/python
from person import Person

class Student(Person):
	auto_roll_no=1	#class attribute
	
	#constructor
	def __init__(self,name,address,dob,course,div):		
		Person.__init__(self,name,address,dob)		#constructor of base class invoked
		self.__name=name
		self.__address=address
		self.__dob=dob
		self.__course=course
		self.__div=div
		self.__roll_no=Student.auto_roll_no
		Student.auto_roll_no=Student.auto_roll_no+1
		self.__marks=dict()
 
	#getter methods
	def getName(self):
		return Person.getName(self)

	def getAddress(self):
		return Person.getAddress(self)

	def getDOB(self):
		return Person.getDOB(self)

	def getCourse(self):
		return self.__course	

	def getDivision(self):
		return self.__div

	def getRollNo(self):
		return self.__roll_no

	def getMarks(self):
		return self.__marks

	#setter methods
	def updateAddress(self,address):
		Person.updateAddress(self,address)

	def updateMarks(self,subject,marks):
		self.__marks[subject]=marks

	def updateCourse(self,course):
		self.__course=course

	def updateDiv(self,div):
		self.__div=div

	#repr method
	def __repr__(self):
		return "Name:"+self.getName()+"\nAddress:"+self.getAddress()+"\nDOB:"+self.getDOB()+"\nCourse:"+self.__course+"\nDiv:"+self.__div+"\nRoll No:"+str(self.__roll_no)


class StudentManager:
	def __init__(self,noOfStudents):
		self.__noOfStudents=noOfStudents
		self.__enrolledStudents=dict()
		self.__suspendedStudents=dict()

	def enrollStudent(self,name,address,dob,course,div):
		st=Student(name,address,dob,course,div)
		self.__enrolledStudents[st.getRollNo()]=st

	def suspendStudent(self,roll_no):
		if roll_no in self.__suspendedStudents:
			pass
		elif roll_no in self.__enrolledStudents:
			st=self.__enrolledStudents.pop(roll_no)
			#del self.enrolledStudents[roll_no]
			self.__suspendedStudents[roll_no]=st
		else:
			return False
		return True

	def getEnrolledStudents(self):
		return self.__enrolledStudents

	def getSusupendedStudents(self):
		return self.__suspendedStudents

	#def GetStudentsDetails(self,roll_no):

	def UpdateMarks(self,roll_no,subject,marks):
		if roll_no in self.__enrolledStudents:
			self.__enrolledStudents[roll_no].updateMarks(subject,marks)
			return True
		return False
	
	def GetMarks(self,roll_no):
		return self.__enrolledStudents[roll_no].getMarks()
	
	def UpdateDiv(self,roll_no,div):
		if roll_no in self.__enrolledStudents:
			self.__enrolledStudents[roll_no].updateDiv(div)
			return True
		return False

	def GetDiv(self,roll_no):
		return self.__enrolledStudents[roll_no].getDivision()

	def UpdateCourse(self,roll_no,course):
		if roll_no in self.__enrolledStudents:
			self.__enrolledStudents[roll_no].updateCourse(course)
			return True
		return False

	def GetCourse(self,roll_no):
		return self.__enrolledStudents[roll_no].getCourse()

	def UpdateAddress(self,roll_no,address):
		if roll_no in self.__enrolledStudents:
			self.__enrolledStudents[roll_no].updateAddress(address)
			return True
		return False

	def GetAddress(self,roll_no):
		return self.__enrolledStudents[roll_no].getAddress()

def StudentManagmentSystem():
	n=int(input("Enter Number of Students:"))
	sm=StudentManager(n)
	choice=0
	ch1=0
	while choice!=7:
		choice=Menu()
		if choice==1:
			print("-----Enrolling New Student-----")
			name=eval(input("Enter Name:"))
			address=eval(input("Enter Address:"))
			dob=eval(input("Enter DOB:"))
			course=eval(input("Enter Course:"))
			div=eval(input("Enter Division:"))
			sm.enrollStudent(name,address,dob,course,div)
			print()
		elif choice==2:
			print("-----Suspending Student-----")
			roll_no=int(input("Enter Roll No to Suspend:"))
			sm.suspendStudent(roll_no)
			print()
		elif choice==3:
			print("-----All Students-----")
			students=sm.getEnrolledStudents()
			for st in students:
				print(students[st])	
				print()
			students=sm.getSusupendedStudents()
			for st in students:
				print(students[st])	
				print()
			print()
		elif choice==4:
			print("-----Enrolled Students-----")
			students=sm.getEnrolledStudents()
			for st in students:
				print(students[st])	
				print()
			print()
		elif choice==5:
			print("-----Suspended Students-----")
			students=sm.getSusupendedStudents()
			for st in students:
				print(students[st])	
				print()
			print()
		elif choice==6:
			while(ch1!=5):
				print("	1.Update Address")
				print("	2.Update Division")
				print("	3.Update Course")
				print("	4.Update Marks")
				print("	5.Exit")
				ch1=int(input("Enter Choice:"))
				if ch1==1:
					print("UPDATE ADDRESS")
					roll_no=int(input("Enter Roll No:"))
					address=eval(input("Enter Updated Address:"))
					sm.UpdateAddress(roll_no,address)
				elif ch1==2:
					print("UPDATE DIVISION")
					roll_no=int(input("Enter Roll No:"))
					div=eval(input("Enter Updated Division:"))
					sm.UpdateDiv(roll_no,div)
				elif ch1==3:
					print("UPDATE COURSE")
					roll_no=int(input("Enter Roll No:"))
					course=eval(input("Enter Updated Division:"))
					sm.UpdateDiv(roll_no,course)

def Menu():
	choice=0
	ch1=0
	print("1.Enroll Student")
	print("2.Suspend Student")
	print("3.Print All Students")
	print("4.Print Enrolled Students")
	print("5.Print Suspended Students")
	print("6.Update Student Details")
	print("7.Exit")
	choice=int(input("Enter Choice:"))
	return choice

def main():
	StudentManagmentSystem()

if __name__=='__main__':
	main()
