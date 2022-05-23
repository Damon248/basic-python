# what if we dont want to use self ? 
# for that we can use static method 

class Employee :
    @staticmethod
    def getsalary():
        print("salary is 60k")
    @staticmethod
    def greet():
        print("hello sir ! how are you ?")

steve = Employee()
steve.getsalary()   # now, this will not throw an error 
steve.greet()