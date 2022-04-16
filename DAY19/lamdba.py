import time

from pyrsistent import b
s1=lambda x:x*x
print()
print(s1(5))
print()
print(s1(7))
print()
s2=lambda a,b,c:a if a>b and a>c else b if b>c else c 
print(s2(12,23,123))
print()
print(s2(345,12,43))