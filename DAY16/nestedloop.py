import time
print("testing nested for loop")
time.sleep(2)
for x in range(10):
    for z in range(x):
        print(x,"---",z)
        print()
print("EXAMPLE2")        
print("EOD") 

print("Nested Loop")
l1=[["A","B","C"],["C","D","E"]]
print(l1)
for l2 in l1:
    print(l2)
    for l3 in l2:
        print(l3)
print("EXAMPLE3")
print()
d1=[["A","B","C"],["C","D","E"]]
print(d1)
for d2 in d1:
    for d3 in d2:
        print(d3)
print("EXAMPLE4")
print() 
s1=[["A","B","C"],["C","D","E"]]
for s2 in s1:
    for s3 in s2:
     print(s3,end=" ")
print()
print("END") 


