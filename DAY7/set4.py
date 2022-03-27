import time
#set is a dynamic or growable wich means we can increase or decrease the value of set as per the application requirement using 
#>add(): it is used to add object as a single point of time 
#> remove():it is used to remove single object at a single point of time 
s1=set()
print(s1)
print("----adding----")
s1.add(1001)
s1.add("Mobile")
s1.add(1600)
s1.add('samsung')
print(s1)
print("---removing----")
s1.remove(1600)
s1.remove("Mobile")
print(s1)