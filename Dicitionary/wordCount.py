#WAP to accept a paragraph from user and return a dictionary of count of words
#!/usr/bin/python
def wordCount(para):
	result=dict()
	for ch in para.split():
		if result.get(ch)!=None:
			result[ch]+=1
		else:
			result[ch]=1
	return result
def main():
	para=str(input("Enter a Paragraph:"))
	output=wordCount(para)
	for x in output:
		print(x,output[x])
if __name__=='__main__':
	main()
