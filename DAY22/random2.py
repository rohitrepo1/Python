import time
from random import *
print("OTP")
for x in range(10):
    print(randint(1,5000000))
print()

print("SINGLE DIGIT")
for x in range(10):
    print(randrange(10))
print()


print("between number")
for x in range(2,9):
    print(randrange(10))
print()
print("USING STEP")
for x in range(2,10,1):
    print(randrange(10))
print()
print("RAMDOM even number")
for x in range(10):
    print(randrange(0,10,2))
print("ODD NUmbers ") 
for x1 in range(10):
    print(randrange(1,10,2))
      


