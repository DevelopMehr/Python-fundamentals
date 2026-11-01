# OOPS - Object Oriented Programming 

# Method is a function in class just simple same with diff names

# Using oops - creating students records

# Class - blueprint or template
# __init__ method - constructor, value initialize - fix
# self parameter - reference of connection build btw class and object - fix


class Student:
    def __init__(self,name, grade):    # method
        self.name = name               # attribute(properties)
        self.grade = grade
    def Student_details(self):  # method
        print(f"{self.name} is in class {self.grade}")


#  object instance of class
student1 = Student('Rahul', 11)
# # print(student1.name, student1.grade)

student1.Student_details()

# modify object property
print(student1.name)
student1.name = 'Haider'
print(student1.name)

# delete object property
print(student1.__dict__)
student1.grade = 21
print(student1.__dict__)



# 4 Features in OOPS
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# ABSTRACTION - Hiding unncessary details from users through class, methods


class Student:
    def __init__(self,name, grade):    # method - Abstraction
        self.name = name               # attribute(properties)
        self.grade = grade
    def Student_details(self):  # method
        print(f"{self.name} is in class {self.grade+2}")     # hidden from users


#  object instance of class
student1 = Student('Rahul', 11)
student1.Student_details()


#Encapsulation - Restrict access to certain attributes or methods to protect data and enforce controlled
#  access. or make private


class Student:
    def __init__(self,name, grade):    # method - Encapsulation
        self.name = name               # attribute(properties)
        self.__grade = grade          #   Double underscore limits access
    def get_grade(self):
        return self.__grade            # To access   
  
    def Student_details(self):  # method
        print(f"{self.name} is in class {self.grade}")


 object instance of class
student1 = Student('Rahul', 11)

print(student1.__grade)   # error
print(student1.grade)    # error
print(student1.get_grade())


# Inheritance - Allow one class(child) to reuse the prop and methods of another class(parent).

# Parent Class 
class Student:
    def __init__(self,name, grade):    # method
        self.name = name               # attribute(properties)
        self.grade = grade
    def Student_details(self):  # method
        print(f"{self.name} is in class {self.grade}")


# #  object instance of class
# student1 = Student('Rahul', 11)

# Child Class
class GraduateStudent(Student): # GraduateStudent child class inherit prop and methods from Student parent class.
    def __init__(self, name, grade, stream):  # old parameter from parent class and new parameters in child class.
        super().__init__(name, grade)      # Call parent class init
        self.stream = stream     # new attribute in child class

# Object
Grad_student1 = GraduateStudent('Hoor', 12, 'PSL')         
print(Grad_student1.stream)


# Polymorphism - Allows methods in difft classes to have same name but difft behaviour depending on objects.
 

class Student:
    def __init__(self,name, grade):    # method
        self.name = name               # attribute(properties)
        self.grade = grade
    def Student_details(self):  # method
        print(f"{self.name} is in class {self.grade}")


# #  object instance of class
student1 = Student('Rahul', 11)

class GraduateStudent(Student):
    def __init__(self, name, grade, stream):  
        super().__init__(name, grade)   
        self.stream = stream   
    def Student_details(self):   # method
        print(f"Hoor is  in class {self.grade} with stream of {self.stream}")      

# Object - student class
student1 = Student('Rahul', 11)

# object -  GraduateStudent class
Grad_student1 = GraduateStudent('Hoor', 12, 'PSL')         

student1.Student_details()
Grad_student1.Student_details()
