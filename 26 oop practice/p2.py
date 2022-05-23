# create a class calculator capable of finding square, cube and sq. root of a number 
class calculator :
    def __init__(self,num) :
        self.num = n
    def getSquare(self):
        print(f"squre of {self.num} is: {self.num**2}")
    def getCube(self):
        print(f"cube of {self.num} is: {self.num**3}")
    def getSquareRoot(self):
        print(f"squre root of {self.num} is: {self.num**0.5}")
    @staticmethod
    def greet():
        print("hello, dear user !")

greeter = calculator
greeter.greet()
n=int(input("enter the number: "))
num_1=calculator(n)
num_1.getSquare()
num_1.getCube()
num_1.getSquareRoot()

