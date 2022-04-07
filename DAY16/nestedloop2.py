import time 
pid=[]
product=[]
price=[]
company=[]
n=int(input("Enter the number of row: "))
for x in range(n):
    a=int(input("Enter the PID: "))
    pid.append(a)
    b=str(input("Enter the Product: "))
    product.append(b)
    c=float(input("Enter the Price: "))
    price.append(c)
    d=str(input("Enter the Company: "))
    company.append(d)
print()
for x1,x2,x3,x4 in zip(pid,product,price,company):
    print(x1,x2,x3,x4)
