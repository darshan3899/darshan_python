#WAP to accept a string from user and perform verbing operation on it (length>=3--add "ing" to its end--if ending in "ing" it should be replaced with "ly"--length<3 leave unchanged)
#!/usr/bin/python
def verb(s):
	if len(s)>=3:
		if s.endswith("ing"):
			s=s[:-3]+"ly"
		else:
			s+="ing"
	return s
s=str(input("Enter a String"))
print(verb(s))

