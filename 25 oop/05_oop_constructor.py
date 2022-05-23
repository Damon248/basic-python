class Employee :
    def __init__(self,name,salary,company) :
        self.name = name
        self.salary = salary
        self.company = company
        print("employee is created")

    def getInfo(self):
        print (f"employee name:{self.name}\nemployee salary:{self.salary}\nemployee company:{self.company}")

steve = Employee("steve",500,"google")
steve.getInfo()