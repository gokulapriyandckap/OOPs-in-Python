# Python Object Oriented Programming.

# Why OOPs?
    #They allow us to group our data and functions in a way  that's easy to reuse.
    # Methods in class is a function that associated with a class.
    # class is a blueprint of creating instances.

# Attributes:
"""Definition: Attributes are variables that store data. They represent the characteristics or properties of an object.
Purpose: Attributes describe the state of an object, providing information about its characteristics.
Access: Attributes are accessed using dot notation (e.g., object.attribute).
Example: In a Car class, color and model could be attributes.
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
"""

# Methods:
"""Definition: Methods are functions that are associated with an object. They define the behavior of the object.
Purpose: Methods perform actions or operations on the object, and they can also modify the object's state (attributes).
Access: Methods are called using dot notation (e.g., object.method()).
Example: In a Car class, start_engine and drive could be methods. 
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start_engine(self):
        print("Engine started")

    def drive(self):
        print(f"{self.color} {self.model} is now moving")
 """

# example of Class.
class Employee:
    raise_amount = 1.04
    def __init__(self,first_name,second_name,email,pay):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.pay = pay

    def fullName(self):
        return "{} {}".format(self.first_name,self.second_name)

    def appraisal(self):
        self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee("Gokul","Peace","gokul@gmail.com",50000)

#print(emp_1.email,emp_1.first_name) # The names, email are all attributes of our class.
#print(emp_1.fullName())
#print(Employee.fullName(emp_1)) # we can print also like this

# print(emp_1.__dict__) # convert the parameters and arguments in dictionary.
print(Employee.__dict__)