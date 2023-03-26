
# Class Methods ==> Is used to work with the class variables.

class Students:

    School = "BHHSS"

# @classmethod is the decorator which used to declare method as class method
# (Says, Hey this method is going to do some work in class, use class name while calling this method)
# (You can call with object name also, if you do so, it will access the object's class. 
# Python will take care of it. Check class Employee, object Emp_3)

    @classmethod
    def info(cls):
        return cls.School
    
print(Students.info())


"""As previous demos class variables cannot change class vaiable using object name.
But sometime there is a requirement, which wants to change class variables using objects.
For that purpose we use @classmethod decorator."""

class Employee:

    Designation = "CE"

    def __init__(self, Name, Age):

        self.Name = Name
        self.Age = Age

    def Emp_details(self):

        print (f"Name: {self.Name}, Age: {self.Age}, Designation: {self.Designation}")

## Class method is a decorator which is used to change class variable using object variable.
## cls is an Argument which referes the class of the object we are using.
## It is same like self but for the class
## By calling this method using object name. It will change the Class variable.

    @classmethod
    def Change_Designation(cls, New_Designation):

        cls.Designation = New_Designation

#In this object we have not give designation, so it will take designation form the class

Emp_1 = Employee("Udhai", 27,)
Emp_1.Emp_details()

# Here we assigned Designation as a object variable. So the method will consider object variable first
Emp_2 = Employee("Chandran", 35)
Emp_2.Designation = "PRE"
Emp_2.Emp_details()

# As usual we are assigning instance to the class and providing argument for __init__ method.
Emp_3 = Employee("Ramesh", 28)
# By calling Change_Designation with object, we are changing Designation in the class variable
# So the class variable changes when the particular object is called.
# Instead of doing this we just assing object vaiable like we did in object Emp_2.
# But the advantage of using this method is we don't create new variables instead of that we use exisisting class variable as object variable with different value.
Emp_3.Change_Designation("LE")
Emp_3.Emp_details()

Emp_4 = Employee("Nancy", 26)
Emp_4.Designation = "CE"
Emp_4.Emp_details()

