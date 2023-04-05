
# In Multilevel Inheritance. Class_3 inherits form Class_2 and Class_2 inherits from Class_1

class Class_1:

    def __init__(self, Name, Age):

        self.Name, self.Age = Name, Age

    def First_Method(self):

        print(f"His Name is {self.Name}, he is {self.Age} years old.")

class Class_2(Class_1):

    def __init__(self, Name, Age, Address):
        
        self.Name, self.Age, self.Address = Name, Age, Address
    
    def Second_Method(self):

        print (f"{self.Name} is a {self.Age} years old and he is coming from {self.Address}")


class Class_3(Class_2):
    
    def __init__(self, Name, Age, Address, Company):

        self.Name, self.Age, self.Address, self.Company = Name, Age, Address, Company

    def Third_Method(self):

        print(f"{self.Name} is a {self.Age} years old from {self.Address}. He works for {self.Company}.")
    pass

Person = Class_3("Udhai", "27", "Trichy", "Straive")

# The object person belongs to class_3. But we can call the methods of class_1 and class_2.

Person.Third_Method()

Person.Second_Method()

Person.First_Method()

