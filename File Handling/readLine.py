#WAP to accept a file name from user and print it line by line
#!/usr/bin/python
def readLineByLine(name):
	fd=open(name)
	if fd!=None:
		line=fd.readline()
		while line!="":
			print(line)
			line=fd.readline()
	
def main():
	name=eval(input("Enter File Name:"))	
	readLineByLine(name)
	

if __name__=='__main__':
	main()
