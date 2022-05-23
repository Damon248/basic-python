class Employee :
    def getsalary (self):       # NOTE: here, self is just a paramerer so u can also change its name but, dont do that bcz its ideal
        print("salary is 50k")

steve = Employee()
steve.getsalary() # Employee.getsalary(steve)   

# so, the when we call the function it will pass an argument in this case the argyment is steve,
#  but in defination of function it doesnt require any value thats why it will throw an error so, 
# for solving that eror we are passing an argument which is SELF 