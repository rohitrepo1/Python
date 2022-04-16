import time 
print("namefull Function")
def test_number_square(number):
    return number*number
number=[2,3,4,5,6,76,97] 
l1=list(map(test_number_square,number))
print("the Square root of the number in the list is ::",l1) 
print("===================================================")
print("using nameless Function")
number=[1,2,3,4,5,6,6]
l2=list(map(lambda x:x*x, number))
print(l2)
