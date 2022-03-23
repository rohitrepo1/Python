#python supports slice operator , the main objective of slice operator is to make  pieces of the string  as per the business login based on the condition 
#***str1[begin:end-1:step]***#
#Slice operator  with positive index
import time
print("EXAMPLE1")
str1="Learn Python"
print(str1)
print()
print("type of data is:",type(str1))
print("===slice operator with positive index===")
print(str1[1:])
#############################################
print(str1[:5])
print("===slice operator with negtive Index===")
str2="Test Python"
print()
print("---using the slice operator with Negative Index---")
print(str2[-1:-3:-8])