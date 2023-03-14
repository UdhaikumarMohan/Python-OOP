
class Cars:

# __init__ Method (Constructor)

    def __init__(self, Owner_Name, RegNo, Colour, Brand_Name):

# As usual the object itself passes as a argument by the name of self. 

# The Owner_Name inside the constructor is an argument and self.Owner name is an object variable. Both are not same.
# We can use any name as an argument, it is not compulsory that both argument and variable name should be same.
# Same things applies for other Arguments and variables.
        self.Owner_Name = Owner_Name
        self.RegNo = RegNo
        self.Colour = Colour
        self.Brand_Name = Brand_Name

# Declare Method.

    def Car_Details(self):

        return f"Register No. {self.RegNo} is a {self.Colour} colour {self.Brand_Name} owned by {self.Owner_Name}"
    
Car_1 = Cars("Agarvin", "A102", "White", "BMW")

Car_2 = Cars("Nithin", "L744", "Blue", "Audi")

# Instead of writing this,
# Car_1.Owner_Name = "Agarvin"
# Car_1.RegNo = "A102"
# We should creat __init__ method (Constructor), by passing Arguments in class, we can work with it.
# We can re use it any where.

print(Car_1.Car_Details())
print(Car_2.Car_Details())