"""
2. Write code to read a file of petrol prices in Maharashtra, Goa & Karnataka:

Jan 2015 81 67 84
Feb 2015 79 66 82
Mar 2015 78 65 81
Apr 2015 77 64 80
...
Output the average petrol price for each state to an output file named
petrol_avg_out.txt.
"""
#!/usr/bin/python
def Prices(name):
	m_price=0
	g_price=0
	k_price=0
	count=0
	fd_read=open(name)
	line=fd_read.readline()
	while line!="":
		line=line[:-1]
		line=line.split()
		m_price+=int(line[2])
		g_price+=int(line[3])
		k_price+=int(line[4])
		count+=1
		line=fd_read.readline()
	return(m_price,g_price,k_price,count)
def main():
	name=eval(input("Enter File Name with Prices:"))
	m_Price,g_Price,k_Price,Count=Prices(name)
	
	fd_write=open("petrol_avg_out.txt","w")
	m_avg=m_Price//Count
	k_avg=k_Price//Count
	g_avg=g_Price//Count
	fd_write.write(str("Maharastra:"+str(m_avg)+" "))
	fd_write.write(str("Karnataka:"+str(k_avg)+" "))
	fd_write.write(str("Goa:"+str(g_avg)+" "))
	fd_write.close()
	
if __name__=='__main__':
	main()
	
