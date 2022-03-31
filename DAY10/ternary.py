import time

x=int(input("Enter  the Number value: "))
y=int(input("Enter the number second value: "))
z=int(input("Enter the third Value: "))
res=x if x>y and x>z else y if y>z else z
print("the large number is ", res)
####
print("read the 6 number from the key baordfind out the max number ")
a=int(input("Enter  the Number value: "))
b=int(input("Enter the number second value: "))
c=int(input("Enter the third Value: "))
d=int(input("Enter  the Number value: "))
e=int(input("Enter the number second value: "))
f=int(input("Enter the third Value: "))

res2= a if a>b and a>c and a>d and  a>e else e if e>f else f 
print(res2)
