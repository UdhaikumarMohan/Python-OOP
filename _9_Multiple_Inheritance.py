
# Multiple Inheritance: Class inherits from the different classes.

# Multiple Inheritance checks for constructors and class variables in the order.

class Main_Class_1:

    Company = "Straive"

    def __init__(self, Name, Age, Address):

        self.Name = Name
        self.Age = Age
        self.Address = Address
    def print_class_1(self):

        print(self.Name, self.Age, self.Address)

class Main_Class_2:

    Company = "SPS"

    def __init__(self, Name, Address):

        self.Name, self.Address = Name, Address

    def print_class_2(self):

        print(self.Name, self.Address)

class Sub_Class(Main_Class_1, Main_Class_2):

    Company = "Root"

    def __init__(self, Name, Age, Address, Designation):

        self.Name, self.Age, self.Address, self.Designation = Name, Age, Address, Designation

    def Sub_Class_method(self):
         print(self.Name, self.Age, self.Address, self.Designation)


Object_1 = Sub_Class("Udhai", 27, "Trichy", "CE" )

# Here the object is created for the Sub_Class, so it will use the constructor and class variables of Sub_Class.
# If Sub_Class does'nt contains any class variables or constructor, it will try to use the First Mentioned class in the inheritance.
# In this case Main_Class_1 mentioned first, so it will use the constructor and class variable from the Main_Class_1 if it is not available in the Sub_Class.
# If Main_Class_1 does'nt contains those things then only it will move to Main_Class_2.

Object_1.print_class_1()
Object_1.print_class_2()
Object_1.Sub_Class_method()

print(Object_1.Company)
