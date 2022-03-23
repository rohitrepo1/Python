#insertion
import time
test=eval(input("Enter the list:" ))
print()
print(test)
print("the data type is:",type(test))
for demo in test:
    time.sleep(2)
    print(demo)
print() 
time.sleep(2)
print("=====END=====")
test2=[10,20,30,40,50]
print(test2)
print(type(test2))
test2[1]=100
test2[2]=200
test2[4]=400
print(test2)
print("*******END*****")
