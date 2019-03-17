#WAP to display Statistical Info of a File
#!/usr/bin/python
import os
def stats(name):
	stat_obj=os.stat(name)
	return stat_obj
def main():
	name=eval(input("Enter File Name:"))
	info=stats(name)
	print(info)

if __name__=='__main__':
	main()
