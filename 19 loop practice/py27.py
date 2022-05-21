# program to check prime numbers 

n=int(input("enter a number: "))
c=0
for i in range (2,n+1) :
    if (n%i==0) :
        c=c+1
    
if c==1 :
    print("given number is a prime number")
else :
    print("given number is not a prime number")

 
 
 
 
