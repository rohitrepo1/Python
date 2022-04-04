#seperator

import time
dd,mm,yy=29,3,2022
print(dd,mm,yy,sep="-")
print(dd,mm,yy,sep=":")


###End ###
#its an attribute which can be return inside the the Print statement 

for x in range(10):
    print(x, end="")
print() 
time.sleep(2)
print("EOD")

#read first mane is first name and last name 
fname=input("Enter the first name: ")
lname=input("Enter the first name: ")
print("my full name is: ",fname,lname)
print()
print("my full name is: ",fname,lname,end=" ")
print()
print("End of Application")
