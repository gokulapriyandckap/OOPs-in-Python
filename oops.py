# creating class
#created the phone class
class phone:
    def make_call(self):
        print("Making Phone Call")

    def set_brand(self,brand):
        self.brand = brand

    def set_cost(self,cost):
        self.cost = cost

    def show_brand(self):
        print(self.brand)

    def show_cost(self):
        print(self.cost)

    def scrolling_instagram(self):
        print("Watch Videos and Chatting with Friends")

#instantiating the 'p1' Object
p1 = phone()

#instantiating the 'p2' Object
p2 = phone()


#invoking methods through object
p1.make_call()
p1.scrolling_instagram()


#setting the attribute values
p2.set_brand("Vivo")
p2.set_cost("100")

#returning the attribute values
p2.show_brand()
p2.show_cost()



#Creating class with Constructor
#note: init method acts as a constructor

class Employee:
    def __int__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of the Employee is",self.name)
        print("Age of the Employee is",self.age)
        print("Salary of the Employee is",self.salary)
        print("Gender of the Employee is",self.gender)


#instanting e1 object
e1 = Employee()

#setting the attribute values
e1.__int__("Gokulapriyan",19,50000,"Male")

#invoking the 'employee_details' method
e1.employee_details()



#Inheritance in Python
#Inheritance Example

#creating the base class
class Vehicle:
    def __int__(self,vehicleType,name,mileage,cost):
        self.vehicleType = vehicleType
        self.name = name
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("My vehicle Type is",self.vehicleType)
        print("My vehicle Name is",self.name)
        print("My vehicle mileage is",self.mileage)
        print("My vehicle cost is",self.cost)

#instating the object for the base class

v1 = Vehicle()

v1.__int__("Bike","Duke 39T", "30KMs","$500")

v1.show_details()



# creating the child class
class car(Vehicle):

    def show_car(self):
        print("This is A Car")



c1 = car()
c1.__int__("car","Ford","50kms","$1000")

# Instating the object for child class
c1.show_details()

#invoking the child class method
c1.show_car()


#Overdig and init method
#what is overriding in Python?
"""
    Method overriding in Python is when you have two methods with the same name that each perform different tasks.
This is an important feature of inheritance in Python. 
In method overriding, the child class can change its functions that are defined by its ancestral classes.
"""

#what is Super().
"""
The super() function is used to give access to methods and properties of a parent or sibling class. 
The super() function returns an object that represents the parent class.
"""

class bike(Vehicle):
    def __int__(self,mileage,cost,name,costAfterService):
        #over-riding the init method
        super().__int__(self,name,costAfterService)
        self.name = name
        self.costAfterService = costAfterService

    def bike_details(self):
        print("This is Bike")
        print("This Bike's name is",self.name)
        print("This Bike's Service's Cost is",self.costAfterService)

b1 = bike()

b1.__int__("tvs50","29km",5)

b1.bike_details()