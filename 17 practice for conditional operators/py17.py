# a=int(input("enter your age: "))
# if(a>=18):
#     print("you are allowed !")
# else:
#     print("oops! you are underage!!! ")

from ast import If

# program to find reatest from four numbers 

n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
n3=int(input("enter third number: "))
n4=int(input("enter fourth number: "))

# logic 1 
if(n1>n2 and n1>n3 and n1>n4):
    print(n1," is greatest")
elif(n2>n1 and n2>n3 and n2>n4):
    print(n2," is greatest")
elif(n3>n1 and n3>n3 and n3>n4):
    print(n3," is greatest")
else:
    print(n4," is greatest")

# logic 2
if(n1>n2):
    b1=n1
else:
    b1=n2
if(n3>n4):
    b2=n3
else:
    b2=n4
if(b1>b2):
    print(b1," is greatest")
else:
    print(b2," is greatest")

