

class Employee:

# Self is something that referes the object which call the Method

    def Working(self):

        # Here the self refers the name of the object which using this particular method.

        # For more uderstanding:

        # We consider that this method is used by ID_1 object.

        # To get a Name variable from that object we should use ID_1.Name, but instead of using ID_1.Name 
        # we should use self.Name. Because ID_1 passes itself as Argument by the name of self.

        return f"The Emplyoee name is {self.Name}, working for {self.Publisher}, in {self.Team} as {self.Designation}"
    
        pass

# Create object for class employee.

ID_1 = Employee()

ID_1.Name = "Chandran"
ID_1.Publisher = "Springer"
ID_1.Team = "German"
ID_1.Designation = "PRE"

ID_2 = Employee()

ID_2.Name = "Ramesh"
ID_2.Publisher = "Springer"
ID_2.Team = "German"
ID_2.Designation = "Copy Editing"

# Invoke the method

print(ID_1.Working())
print(ID_2.Working())