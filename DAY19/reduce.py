import time
from functools import *
total_Salary=[3000,40000,5000,5400,4300,21000]
l1=reduce(lambda x,y:x+y,total_Salary)
print("total salary",l1)