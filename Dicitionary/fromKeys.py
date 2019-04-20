#WAP to implement your own fromkey which ensures if value is list assing single value to each of the keys
#!/usr/bin/python
def fromKeys(dict1,list1):
	keys=dict1.keys()
	result=dict()
	if type(list1)==list:
		i=0
		for x in keys:
			if i<len(list1):
				result[x]=list1[i]
				i+=1
				continue
			result[x]=None
	else:
		result=dict.fromkeys(dict1,list1)
	return result 
def main():
	dict1=eval(input("Enter a Dictionary:"))
	list1=eval(input("Enter List Values:"))
	print(fromKeys(dict1,list1))

if __name__=='__main__':
	main()
