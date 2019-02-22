#WAP to remove all occurances of given data from list
#!/usr/bin/python
def remove(a,rem):
	while rem in a:
		a.remove(rem)
def main():
	a=eval(input("Enter List:"))
	rem=eval(input("Enter Value to remove\n"))
	(remove(a,rem))
	print(a)
if __name__=='__main__':
	main()
