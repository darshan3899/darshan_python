#WAP to accept a sentence from user and replace the not bad construct (if found) with good
#!/usr/bin/python
def notBad(s):
	result=""
	not_index=s.find("not")
	if not_index!=-1:
		bad_index=s.find("bad")
		if bad_index!=-1 and bad_index>not_index:
			result=s[:not_index]
			result+="good"
			result+=s[bad_index+3:]
	return(result)

s=str(input("Enter a String "))
print(notBad(s))

