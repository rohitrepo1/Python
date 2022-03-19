import time
from unittest import result
x1=1+330j
z2=100j
print("the data type is:",x1)
print("the data type is:",type(x1))
print("real-imaginary")
print(x1.imag)
print("real-part")
print(x1.real)
print()
print(z2.real)
time.sleep(2)
result=x1+z2
print("the sum of complex data type is:",result)



