import time
print("---welcome to the test Services---")
username=input("Enter the username: ")
password=int(input("Enter the password : "))
if (username=="test" and password==12345):
    print(username,password,":Login Sucess")
else:
    print("username and password is invalid try again")
time.sleep(2)
print("EOA")    
print("--------------------------or operator----------------------------")
First_Name=input("Enter the First-name: ")
last_name=input("Enter the password: ")
password=input("enter the password: ")
confirm_password=("confirm the passowrd: ")
if (First_Name=="rohit" or  last_name=="suri")or(password=="1234" and confirm_password=="1234"):
    print("details are valid")
else:
    print("username is invalid")    
