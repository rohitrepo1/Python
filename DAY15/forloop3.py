import time
number=int(input("Enter the Number : "))
for x in range(1,11):
    time.sleep(1)
    print("%dX%d= %d"%(number,x,number*x))
print()    

