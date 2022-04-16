from pickletools import string1
import time 
def Test_case():
    global str1
    c=0
    str1="This is A test Line"
    for x in str1:
        if x in ("AEIOUaeiou"):
            c+=1
            print("Vowels are:",x, end="   ")
    print("Number of vowles are:",c)

Test_case()
print()
print("End")