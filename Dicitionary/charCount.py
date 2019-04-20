#WAP to accept a sentence from user and return a dictionary of count of each characters occuring in it
#!/usr/bin/pyhton
def charCount(sen):
	result=dict()
	for ch in sen:
		if result.get(ch)!=None:
			result[ch]+=1
		else:
			result[ch]=1
	return result
def main():
	sen=str(input("Enter a Sentence:"))
	print(sen)
	output=charCount(sen)
	
	for x in output:
		print(x,output[x])

if __name__=='__main__':
	main()
