#WAP to accept a filename from user and number of lines to copy to another file using command line arguments
#!/usr/bin/python
import argparse
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
	print(sys.argv)
	parser=argparse.ArgumentParser()
	parser.add_argument("-i",type=str,help="Input/Source File Name=",required=True)
	parser.add_argument("-d",type=str,help="Destinantion File Name=",required=True)
	parser.add_argument("-n",type=int,help="Number of Lines to copy,default 0(complete file)",required=True)
	args=parser.parse_args()
	print (args)
	copyLines(args.i,args.d,args.n)

if __name__=='__main__':
	main()
