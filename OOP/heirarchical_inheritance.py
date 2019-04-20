#WAP to demonstrate Heirarchical Inheritance
#!/usr/bin/python
import inspect
class A(object):						#class A(object):	inheriting with object->then 2.7 works like 3.x
	def m(self):
		print("Inside A's m()")
	def k(self):
		print("Inside A's k()")

class B(A):
	def l(self):
		pint("Inside B's l()")

class C(A):
	def n(self):
		print("Inside C's n()")
	def m(self):
		print("Inside C's m()")

class D(B,C):
	def __call__(self):
		print("Invoked")


def main():
	print(inspect.getmro(D))
	obj=D()
	obj.n()
	obj.m()
	obj()
if __name__=='__main__':
	main()

'''
OUTPUT
without class(object)

3.x
darshan@darshan:~/Python/Class/OOP$ python3 heirarchical_inheritance.py
Inside C's n()
Inside C's m()

2.7
darshan@darshan:~/Python/Class/OOP$ python heirarchical_inheritance.py
Inside C's n()
Inside A's m()

'''