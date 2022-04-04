import time
from sys import argv
print(argv)
print(type(argv))
sum=0
for x in argv[1:]:
    x1=int(x)
    sum=sum+x1
print("the Sum is :",sum)    