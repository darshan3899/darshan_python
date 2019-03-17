#WAP to accept a filename from user and print the content in reverse order
#!/usr/bin/python
def reverse(fd):
	line=fd.readline()
	if line=="":
		return
	reverse(fd)
	print(line)
	
def main():
	name=eval(input("Enter File Name:"))
	fd=open(name)
	reverse(fd)
if __name__=='__main__':
	main()
