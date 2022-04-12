#Dict Comp

d1={number:number*number for number in range(10)}
print(d1)
print(type(d1))
for x,y in d1.items():
    print (x,"---",y)