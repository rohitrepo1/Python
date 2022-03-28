import time
a=[1,2,3,4,5,6]
a2=bytearray(a)
print(type(a2))
print(a2)
time.sleep
print()
print("EOA")
print(*a2)

#example2
e=[100,200,150,50,250]
e2=bytearray(e)
print(e2)
print(*e2)
print("---After Mutable operation---")
e2[0]=10
e2[1]=1
e2[2]=2
print(*e2)
print(type(e2))
time.sleep
print("EOA")

