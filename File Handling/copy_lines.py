#WAP to accept a filename from user and number of lines to copy to another file using command line arguments
#!/usr/bin/python
import sys

def copyLines(inputFile,outputFile,Number):	
	count=1	
	inputfd=open(inputFile)
	outputfd=open(outputFile,"w")
	line=inputfd.readline()
	while line!="":
		if(Number < count):
			break
		else:	
			outputfd.write(line)
			line=inputfd.readline()
			count+=1			
	inputfd.close()
	outputfd.close()
def main():
	if(len(sys.argv)!=4):
		print("Enter Valid Number of Arguments")
	else:
		print(sys.argv)
		copyLines(sys.argv[1],sys.argv[2],int(sys.argv[3]))

if __name__=='__main__':
	main()
