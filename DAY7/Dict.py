#python supports  dict data type. if yo want to represent one or more  that one object as key value pair 
import time
d1={}
print(d1)
print(type(d1))
d2=dict()
print(d2)
print(type(d2))

####

#example2
d3={"Name":"Samsungs10","Price":100}
print(d3)
print(type(d3))
print("---updating the dict---")
d3["company"]='samsung'
d3["year"]=2022
print(d3)
print("mgf yes is :",d3["year"])
print("The Brand is  :",d3["company"])

#example3
print(d3)
for x in d3.values():
    print(x)
print() 
for y in d3.keys():
    print(y)
print()    
for z in d3.items():
    print(z)
print()    
print("key","---""values")
for x,y in d3.items():
    print(x,"---",y)
print("EOA")    


