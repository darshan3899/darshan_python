#WAP to accept two strings from user and swap their first two charcters  Ex-Dog Dinner----->Dig Donner
#!usr/bin/python
s1=str(input("Enter a String"))
s2=str(input("Enter a String"))
s1_part=s1[:2]
s2_part=s2[:2]
s1=s2_part+s1[2:]
s2=s1_part+s2[2:]
print (s1)
print (s2)
