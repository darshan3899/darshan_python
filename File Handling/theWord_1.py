#WAP to accept a file name from user and print those lines who have a word more than once
#!/usr/bin/python
def the(name,word):
	fd=open(name)
	line=fd.readline()
	while line!="":
		if str(line).count(word)>1:
			print(line)
		line=fd.readline()
def main():
	name=eval(input("Enter File Name:"))
	word=eval(input("Enter Word whose more than one occurance is required:"))
	the(name,word)

if __name__=='__main__':
	main()
