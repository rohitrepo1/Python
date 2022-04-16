import time 
d1={"PID":1001,"pname":"laptop","company":"DELL","price":54000}
def test():
    for a,b in d1.items():
        print(a,"---",b)
def test2():        
    for s1,s2 in d1.items():
        print(s1,"---",s2)
def test3():        
    for z,y in d1.items():
        print(z,"---",y)
test()
print("=====") 
test2()
print("----")
test3()       
print()                