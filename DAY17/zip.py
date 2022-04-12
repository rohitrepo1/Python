#zip function is used to convert data structure  from one type to another , and it is sed to fetch  more than two values as per the application requirement. 
l1=[1,2,3,]
l2=(4,5,6,7)
print(l1)
l1=tuple(zip(l1,l2))
print(l1)

Product_info=['pid','pname','price']
Product_deails=[1001,"mobile",23000]
invoice=dict(zip(Product_info,Product_deails))
print(invoice) 

Employee_ID=[]
Employee_name=[]
Employee_Salary=[]
company=[]
while(True):
    a=int(input("Enter the Employee_ID"))
    Employee_ID.append(a)
    b=str(input("Enter the Employee_name"))
    Employee_name.append(b)
    c=float(input("Enter the employee_salary"))
    Employee_Salary.append(c)
    d=str(input("Enter the Company Name"))
    company.append(d)
    option=input("Do you want to insert another record:[YES|NO]:")
    if(option=="NO"):
         break
print("Employee_ID","Employee_name","Employee_Salary","company name")
print('------------------------------------------------------------')
for y1,y2,y3,y4 in zip(Employee_ID,Employee_name,Employee_Salary,company):
    print(y1,y2,y3,y4)
print('------------------------------------------------------------')

