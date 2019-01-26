#WAP to accept a string from user and repalce the occurance of first letter with *
#!usr/bin/python
s=str(input())
print(s[0]+s[1:].replace(s[0],"*"))
