# program to find factorial of a number 

n=int (input("enter a number: "))
factorial=1
for i in range (1,n+1):
    factorial=factorial*i
print(f"factorial of given number is {factorial} ")