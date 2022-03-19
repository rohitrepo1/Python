##identifier is also  called variable used in the script###
#rules for declaring an identifier 
#===================================#
#1 only allowed character  are A-Z, a-z or 0-9
#2 only special character  is allowed that is "_"
#3 should not start from number or decimal numbers
#4 there is no lenght limit  for variable
#5 should not  start with reserved key words

#Example1
import time
ABC_abc_123=1200
print("the vaule is:",ABC_abc_123)
print()
print("the id is:",id(ABC_abc_123))
print()
time.sleep(3)
print("the data type is:",type(ABC_abc_123))
print()
print("End of Programe")
#Example2
print("start of Programe")
_=1500
print("the vaule is:",_)
print()
print("the id is:",id(_))
print("the data type is:",type(_))
### see the Screenshot#
#Example3
print()
print()
name="rohit"
NAME="rohit"
print("the vaule is:",name)
print("the vaule is :",id(name))
print("the vaule of id:",id(NAME))