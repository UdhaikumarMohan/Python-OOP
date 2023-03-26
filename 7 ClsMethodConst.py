
# Built a constructor using classmethod.

class Surphy:

    def __init__(self, Contest_Name, Incharge, Time):
        self.Constest_Name = Contest_Name
        self.Incharge = Incharge
        self.Time = Time

    def Events(self):
        return f"\n{self.Constest_Name} will be conducted by {self.Incharge} at {self.Time}"


# create a Constructor using classmethod, this method will split the given value and give it back to the class as class variables.
# Class will pass it as object variables.

    @classmethod
    def class_contest(cls, Contest):

        # This method get an argument Constent which will work as a class variable.
        # Then it will splited using split function.
        # Split function stores it as list, and list elements should be passed as class variables, and it will be given to the object.

        # Contest = Contest.split('/')
        # return cls(Contest[0], Contest[1],Contest[2])

        # or return like this
        # Using variable length argument we can split the argument(Constant) into three arguments which will passed to class.
        
        return cls(*Contest.split('/'))
    

Contest_1 = Surphy("Quiz", "Udhai", "10 AM")
Contest_2 = Surphy("Poster_Presentation", "Rini", "12 PM")

# Create Object using classmethod class_contest
Contest_3 = Surphy.class_contest("Sci-Click/Abith/4 PM")
Contest_4 = Surphy.class_contest("Treasure Hunt/VijayKrishnan/5 PM")

print(Contest_1.Events())
print(Contest_2.Events())
print(Contest_3.Events())
print(Contest_4.Events())



