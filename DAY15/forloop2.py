import time 
s=input("Enter the String")
c=0
for x in s:
    if x in ('aeiouAEIOU'):
        c+=1
        print (x)
print("the number of VOWELS:",c) 
