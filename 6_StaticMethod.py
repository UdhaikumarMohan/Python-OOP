
# Static method is a method wich does not manipulate Class or Instance variables.
# It uses staticmethod decorators

class Store:

    Store_Name = "AB Electronics"

    def __init__(self, Brand, Price):

        self.Brand = Brand
        self.Price = Price

    #declare instance method
    def product_details(self):

        return f"This is a {self.Brand} Headset, price {self.Price} from {self.Store_Name}"

    #declare classmethod
    @classmethod
    def update_Store_Name(cls, Name):
        cls.Store_Name = Name
        return cls.Store_Name
    
    #declare staticmethod
    @staticmethod
    def Moto():
        return f"For the best mobile accessories"
    
Headset = Store("Boat", 500)

# Calling Instance Method
print(Headset.product_details())

# Calling Class Method
print(Store.update_Store_Name("AB Mobiles and Accesories"))
#or
print(Headset.update_Store_Name("AB Mobiles and Accesories"))
#or
Headset.update_Store_Name("AB Mobiles and Accesories")
print(Headset.product_details())

# Calling Static Method
print(Headset.Moto())


