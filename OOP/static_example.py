#static method
#!/usr/bin/python

class Demo:
		@staticmethod		#decorator
		def InvokeStatic():
			print("static method invoked")

		@classmethod
		def InvokeClassMethod(cls):
			print("Invoked Class Method",type(cls),id(cls))
		def ObjectMethod(self):
			print("Inside Object Method")

def main():
	obj=Demo()
	print("id(Demo):",id(Demo)) 
	Demo.InvokeStatic()
	Demo.InvokeClassMethod()
	obj.ObjectMethod()

if __name__=='__main__':
	main()