# create a class programmer for storing information of few progarmmers working at microsoft 
class Programmer :
    company = "microsoft"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def getInfo(self):
        print(f"name of {self.company} programmer: {self.name}")
        print(f"age of {self.company} programmer: {self.age}")
        print(f"salary of {self.company} programmer: {self.salary}\n")

programmer_1 = Programmer("steve","26",50000)
programmer_2 = Programmer("natasha","24",70000)
programmer_1.getInfo()
programmer_2.getInfo()