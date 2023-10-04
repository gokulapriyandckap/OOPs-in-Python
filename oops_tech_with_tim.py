# OOPS in Python.
# print(type('gokul'))
# def hello():
#    print("Hello")
# print(type(hello))

# Everything in Python that we work with is actually an object of some kind of class.
# Whenever you create something in python you are really creating an object which is an instance of a specific class.

# Methods is essentially just a function that goes inside of a class.

                                       # Class.
# class Dog:
#    def __init__(self,name,age):
#       self.name = name
#       self.age = age
#       print(f"Name: {name.capitalize()} and Age: {age}")
#    def bark(self):
#       print("Bark")
#    def add_one(self,x):
#       print(x+1)
#
#    def get_name(self):
#       print(self.name.capitalize())
#
#    def get_age(self):
#       print(self.age)
#
#    def set_age(self,age):
#       self.age = age
#       print(age)


# d1 = Dog("gokul",19) # object
# print(type(d1))

# d1.bark()
# d1.add_one(1)

# d2 = Dog("jeeva",23)

# print(d1.name)
# print(d2.name)

# d1.get_name()
# d1.set_age(23)
# d2.get_name()


                                    # Mulitiple Classes.
# class student:
#    def __init__(self,name,age,grade):
#       self.name = name
#       self.age = age
#       self.grade = grade # 0 - 100
#
#    def get_grade(self):
#       return self.grade
#
# class course:
#    def __init__(self,name,max_students):
#       self.name = name
#       self.max_students = max_students
#       self.students = []
#
#    def add_students(self,student):
#       if len(self.students) < self.max_students:
#          self.students.append(student)
#          return True
#       return 'Students Limit Filled'
#
#    def get_average_grade(self):
#       value = 0
#       for student in self.students:
#          value += student.get_grade()
#
#       print(value / len(self.students))
#
#
# s1 = student("Gokul",19,90)
# s2 = student("Jeeva",25,70)
# s3 = student("Dhanush",20,65)
#
# course = course("Data Science", 2)
# course.add_students(s1)
# course.add_students(s2)
# print(course.add_students(s3))
# course.get_average_grade()


                                             # Inheritance.
# class pet:
#    def __init__(self,name,age):
#       self.name = name
#       self.age = age
#    def show(self):
#       print(f"I am {self.name} and My age is {self.age}")
#
#    def speak(self):
#       print("I don't know What I say")
#
#
# class cat(pet):
#
#    def __init__(self,name,age,color):
#       super().__init__(name,age)
#       self.color = color
#
#    def speak(self):
#       print("Meow")
#
#    def show(self):
#       print(f"I am {self.name} , My age is {self.age} and  I'm {self.color} color")
#
#
#
# class dog(pet):
#    def speak(self):
#       print("Bow")
#
#
# pet = pet("Gokul",19)
# pet.speak()
# cat = cat("Pussy",17,"White")
# cat.show()
# cat.speak()
# dog = dog("Jhonny",20)
# dog.speak()


"""The @classmethod decorator in Python is used to define a method that is bound to the class rather than the instance of the class.
It is often used in class-level operations or to create alternative constructors."""

                                                # Class Methods.

# class person:
#    no_of_people = 0
#
#    def __init__(self,name):
#       self.name = name
#       person.add_people()


   # @classmethod # This method doesn't access any sepcific instance, it only access these class attributes or anything  to the class itself.
   # def no_of_people_(cls):
   #    return cls.no_of_people

#    @classmethod
#    def add_people(cls):
#       cls.no_of_people += 1
#
# p1 = person("gokul")
# p2 = person("jeeva")
# print(person.no_of_people_())


                                        # Static Method.

"""A static method in a Python class is a method that belongs to the class rather than an instance of the class. It doesn't have access to the instance or its attributes and doesn't modify the class or instance state.
You define a static method using the @staticmethod decorator."""

# class Math:
#     @staticmethod
#     def add5(x):
#         return x + 5
#
# print(Math.add5(0))
