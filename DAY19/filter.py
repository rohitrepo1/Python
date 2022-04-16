import time
print("using filter")
print("using namefull function")
def test_Odd_Number(number):
    if(number%2==1):
        return True
    else:
        return False
number=[101,102,103,104,105,106,97]
l1=list(filter(test_Odd_Number,number))
print(l1)

print("=================================================")
print("using nameless-function")
number=[1,2,3,4,5,6,7,8,9,0]
l2=list(filter(lambda x:x%2==1,number))
print(l2)
print("End of application")