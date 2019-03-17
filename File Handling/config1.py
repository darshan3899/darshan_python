#WAP to accept a config file from user and create a dictionary of configurations defined in it
#extract the section and create the dictionary of each section
#!/usr/bin/python
def printLine(name):
	result_dict={}
	config_split=[]
	fd=open(name)
	line=fd.readline()
	while line!="":
		if not str(line).startswith("#") and str(line)!="\n" and ("=" in line or ":" in line):
			print(line[:-1])
			line=line[:-1]
			if "=" in line:
				config_split=line.split("=")
			elif ":" in line:
				config_split=line.split(":")
			if "#" in config_split[1]:
				config_split[1]=config_split[1].split("#")[0]
				
			result_dict[config_split[0]]=config_split[1]
		line=fd.readline()
	print (result_dict)


def main():
	name=eval(input("Enter Name of Config File:"))
	printLine(name)
if __name__=='__main__':
	main()
