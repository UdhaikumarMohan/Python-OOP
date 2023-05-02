
# Using operator_overloading we make operator to work for our convinience

class Addition:

    def __init__(self, Mark, Subject, Name):

        self.Name = Name
        self.Mark = Mark
        self.Subject = Subject

    def Method(self):

        print(f"\n {self.Name} scored {self.Mark} in {self.Subject}")

# Lets write method for operator overloading
    def __add__(self, other):

        return (self.Mark + other.Mark)
    
# String overloading

    def __str__(self):

        return f"This string belongs to Obj_1"
    
    def __repr__(self):

        return f"This string bleongs to Obj_2"

Obj_1 = Addition(75, "Maths", "Ravi")
Obj_2 = Addition(85, "Physics", "Karim")

Obj_1.Method()

print(Obj_1 + Obj_2)
print(Obj_1)
print(Obj_2.__repr__())