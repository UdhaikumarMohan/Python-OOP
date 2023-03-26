
# Handling Variables.


class Students:

# The variables given inside the class is called as Class variables.

    Degree = "B.Sc."
    Subject = "Physics"
    pass

# Creating instance (Object) named stud.

Stud_1 = Students()

# The variables given below is called as instance variable, which belongs to that particular object.

Stud_1.Name = "Udhai"
Stud_1.RollNum = "165208127"
Stud_1.Project = "Nano Powders"

# This print function return dictionary of the datas in the Stud_1 Object
print(Stud_1.__dict__)

# Now we are printing Class variable using student object.
print(Stud_1.Degree)

# Now we create a variable Name Degree for object. 
# The variable "Degree" in the Class(Students) and variable created for object is not same.
# Even though Class variable and object variable has the same name, both are different.
Stud_1.Degree = "M.Sc."

# We can see the Degree in class is not changed. Because we cannot change Class variable using object variable.

print(Stud_1.__dict__)

print(Students.__dict__)

Students.Degree = "B.Tech"

# Class variable can be changed by only using class.
print(Students.Degree)
