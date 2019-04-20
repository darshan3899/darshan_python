"""
Write a simple BankAccount class. Account number
should be auto-generated. Implement withdraw and
deposit methods for the same. Write a menu driven
program to perform account operations
"""
#!/usr/bin/python
class BankAccount:
	auto_acc_no=1	#class attribute
	
	def __init__(self,name,balance=0):
		self.name=name;
		self.balance=balance
		self.acc_no=BankAccount.auto_acc_no
		BankAccount.auto_acc_no=BankAccount.auto_acc_no+1
		
	def withdraw(self,amount):
		if self.balance<amount:
			return -1
		else:
			self.balance=self.balance-amount
		return self.balance
		
	def deposit(self,amount):
		self.balance=self.balance+amount
		
	'''
	#overloaded method for deposit()
	def __add__(self,amount):
		self.balance=self.balance+amount
	'''
	
	'''
	#overloaded method for withdraw()
	def __sub__(self,amount):
		return self.withdraw(amount) # BanckAccount.withdraw(self, amount)
	'''
	
	#def __getitem__(self,amount):
		
def Menu():
	choice=0
	print("1.Deposit\n2.Withdraw\n3.Account Details\n4.Exit")
	choice=int(input("Enter Choice:"))
	return choice	


def main():
	name=eval(input("Enter Name:"))
	bal=int(input("Enter Initial Amount:"))
	choice=0
	choice=Menu()
	c1=BankAccount(name,bal)
	while choice!=4:
		if choice==1:
			amount=int(input("Enter The Amount:"))
			c1.deposit(amount)
		if choice==2:
			amount=int(input("Enter The Amount:"))
			c1.withdraw(amount)
		if choice==3:
			print(c1.name)
			print(c1.acc_no)
			print(c1.balance)
		

if __name__=='__main__':
	main()
