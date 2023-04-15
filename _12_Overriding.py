
# Overriding

# Python always prefers instance variables first. It will consider class variable when only instance does'nt contains the variable.

"""
Parent_Class allows Child_Class to use its constructor.
But it does not allow when Child_Class contains its own constructor.
At that time Child_Cass only allowed to use class variables of the Parent_Class.
We cannot call instance variable from Parent_Class constructor, When Child_Class contains its own constructor.

If we want to use Parent_Class constructor when Child_Class has its own constructor, we have to use super().__init__().
It just like copying the variables from the constructor of the Parent_Class.

Now in Child_Class_3 we used super() after the object variable (self.Variable), as we said before super() is just like copying the Parent_Class constructor,
it also contains self.Variable. By writing super after the self.Variable, it will override by the self.Variable of the Parent_Class.

"""

class Parent_Class:

    Variable = "This is a Parent_Class Variable"

    def __init__(self):
        
        self.Variable = "This is Parent_Constructor Variable"

        self.A = "An another constructor variable."

class Child_Class_1(Parent_Class):

    Variable = "This is a Child_Class_1 Variable"

    def __init__(self):

        super().__init__()
        self.Variable = "This is Child_Constructor Variable"


class Child_Class_2(Parent_Class):

    Variable = "This is a Child_Class_1 Variable"

    def __init__(self):

        self.Variable = "This variable will be override by super().__init__()"
        super().__init__()

Object_1 = Parent_Class()

Object_2 = Child_Class_1()

Object_3 = Child_Class_2()

print(Object_1.Variable)
print(Object_2.Variable)
print(Object_2.A)
print(Object_3.Variable)