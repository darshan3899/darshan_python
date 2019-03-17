#WAP to accept a file name from user and print those lines who have less than or equal to 80 charaters also print line numbers which have more than 80 characters stating that lines have more than standard count of characters
#!/usr/bin/python
def linesLessThan80(name):
	fd=open(name)
	line_number=1
	line_numbers=[]
	line=fd.readline()
	while line!="":
		if len(line)<=80:
			print(line)
		else:
			line_numbers.append(line_number)
		line_number+=1		
		line=fd.readline()
	print("Line Numbers with charachters more than 80:",line_numbers)

def main():
	name=eval(input("Enter File Name:"))
	linesLessThan80(name)

if __name__=='__main__':
	main()
