#WAP to accept a file name from user and smallest and longest line from it
#!/usr/bin/python
def	smallLong(name):
	fd=open(name)
	line=fd.readline()
	small_=line
	long_=line
	while line!="":
		line=fd.readline()
		if line =="\n" or line =="":
			continue
		if len(line)>len(long_):
			long_=line
		elif len(line)<len(small_):
			small_=line
	return(long_,small_)
def main():
	name=eval(input("Enter File Name:"))	
	a=smallLong(name)
	print(a)
if __name__=='__main__':
	main()
