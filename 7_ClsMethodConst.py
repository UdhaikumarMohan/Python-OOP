# Built a constructor using classmethod.

class Surphy():

    def __init__(self, *Args):
        self.Contest_Name, self.Incharge, self.Time = Args
        
    def Method_Contest_Name(self):
        return self.Contest_Name
    
    def Method_Incharge(self):
        return self.Incharge
    
    def Method_Time(self):
        return self.Time

    def Events(self):
        return f"\n{self.Method_Contest_Name()} will be conducted by {self.Method_Incharge()} at {self.Method_Time()}"


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
   
def call_surphy(obj):

    if not isinstance(obj, Surphy):
        print("\n This object does not belong to this class.")

    else:
        print(obj.Events())

def main():
    
    Contest_1 = Surphy("Quiz", "Udhai", "10 AM")
    call_surphy(Contest_1)

    Contest_2 = Surphy("Poster_Presentation", "Rini", "12 PM")
    call_surphy(Contest_2)

    # Create Object using classmethod class_contest

    Contest_3 = Surphy.class_contest("Sci-Click/Abith/4 PM")
    call_surphy(Contest_3)

    Contest_4 = Surphy.class_contest("Treasure Hunt/VijayKrishnan/5 PM")
    call_surphy(Contest_4)

if __name__ =="__main__": main()

