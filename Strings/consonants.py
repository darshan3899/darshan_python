#WAP to accept string from user and print count of consonants in it
#!/usr/bin/python
def consonantsCount(s):
	count=0
	for i in s:
		if i in "aeiouAEIOU":
			continue
		count+=1
	return count


def main():
	s=str(input("Enter A String\n"))
	print(consonantsCount(s))
	
if __name__=='__main__':
	main()
