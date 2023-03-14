from Demo_Class import Computer

Object_1 = Computer()
Object_2 = Computer()
Object_3 = Computer()

Object_4 = Computer()
Object_5 = Computer()
Object_6 = Computer()

Object_7 = Computer()

# This is the one of the type to call methods (We don't usualy use it in the most of the times.)

# Computer.Config(Object_1)
# print("")
# Computer.Config(Object_2)
# print("")
# Computer.Info(Object_3)

# This one is the most popular way to call the method by using object itself.
Object_1.Info()
print("")           #This print is given for just to produce an empty lines.
Object_2.Config()
print("")
Object_3.Info()
print("")

# Print Attributes form the Computer Class.

print(Object_4.Attribute_1)
print("") 
print(Object_5.Atrribute_2)
print("") 
print(Object_6.Attribute_3)
print("") 

Object_7.Attribute_3 = "Super Nova"

print (Object_7.Attribute_3)

