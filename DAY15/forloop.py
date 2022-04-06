from cmath import log10
import time
for x in range(15):
    print("#",end=" ")
print()
print()
for z in "INFORMATICA":
    print(z)
print() 
#list
for a in [100,200,300,400,500]:
    print(a)
print() 
#tuple
for b in (100,200,300,400,500):
    print(b)
print() 
l=[1,2,3,4,5,6]
for l2 in l:
    print(l)
    print()
    print(l2)
print
d=[1,2,3,4,5,6,7,8,9,12,13,14,15]
for x in d:
    if x%2==0:
        print("evennumber",x)
    else:
        print("ODDNUMBER",x)    
print()
#remove deplicate 
d2=[10,20,10,30,40,30,50,50]
result=[]
print("Removing duplicate")   
for i in d2:
    if i not in result:
        result.append(i)
print(result)



