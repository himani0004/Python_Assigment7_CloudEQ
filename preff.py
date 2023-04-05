#class attribute or instance attribute which will be preffered first?
#class attribute will be preferred first.Beacuse it is shared by all objects + save memory.

class Employee:
    company = "cloudeq"
    profession= "software trainee"
    id = 51
    technology = "Python"
    #self#constructor
    def __init__(self,name1,cource1):
        self.name=name1
        self.cource=cource1
        self.salary=0
        self.designation=None
        self.surname = None

    #making function
    # def MyFunction (self,sall1,desig,surn):
    #     self.salary=sall1
    #     self.designation=desig
    #     self.surname = surn
    def display(self):
      print(self.name)
      print(self.cource)  
    


#here making three objects with different parameters

obj = Employee("riya","mca")
# print(obj.name)
# print(obj.cource)
obj.display()
print(obj.designation)
obj1 = Employee("himani","mba")
print(obj1.name)
obj1.salary=400
print(obj1.salary)

obj3=Employee("sharma",33)
obj3.designation = "software trainee"
print(obj3.designation)
obj3.surname = "vashisht"
print(obj3.surname)

 
#todays class 5/4/23


#class attribute
# himani = Employee()
# print(himani.profession)
# print(himani.id)
# print(himani.technology)
# Employee.company = "deloitte"
# print(Employee.company)

# #instance attribute
# himani.salary  = 500
# print(himani.salary)
# himani.Name = "Sharma"
# print(himani.Name)





#super method
# the method through which we can use the constructors ,attribute and methods of parent class.
#class methods
# these are inbuilt function in python ,these are bound to class rather than an object.