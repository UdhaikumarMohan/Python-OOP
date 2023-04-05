
# Inheritance is used to access the functions and methods of the parent class.

# Three types of Inheritance: Single-Level-Inheritance, Multiple-Inheritance, Multilevel-Inheritance.

# First work with Single-Level-Inheritance

# Create a Parent class.

class Parent_class():

    def __init__(self, Name, Address):

        self.Name = Name
        self.Address = Address

# Method for parent class

    def parent_class_record(self):

        print(f"{self.Name} is coming from {self.Address}")

# Now we want to use the properties and method of the parent class in the child class.
# So we create a child class which inherits from the parent class.
# By giving name of the parent class inside the round brackets in child class ensures that the Child class is inherits from the parent class.

class Child_class_1(Parent_class):
    pass


# Let's create an other child class but this time with its own consturctor.

class Child_class_2(Parent_class):
    
    def __init__(self, Name, Address, Designation):

        self.Name = Name
        self.Address = Address
        self.Designation = Designation

    def child_class_record(self):
                
        print(f"{self.Name} is coming from {self.Address} and he works as {self.Designation}")

# Object for parent class.

obj_1 = Parent_class("Udhai", "Trichy")
obj_1.parent_class_record()

# Object for child class 1:
# We are doing nothing in the child class but it still works by using functions in the parent class.
# obj_2 belongs to the child class, but we are calling a method from the parent class. But it still works because of the inheritance

obj_2 = Child_class_1("Ramesh", "Madurai")
obj_2.parent_class_record()

# Object for child class 2:
# obj_3 works with the method from the child_class_2. 
# Becaue, although child_class_2 inherits from the parent class, it got its own constructors.
# So it will give first preference to its own constructors.

obj_3 = Child_class_2("Chandran", "Trichy", "PRE")
obj_3.child_class_record()

# In case of obj_4 it has 3 arguments, but we are calling method form the parent class.
# So it will use constructor from the parent class, instead of its own.

obj_4 = Child_class_2("Nancy", "Trichy", "PRE")
obj_4.parent_class_record()





