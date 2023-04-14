
# Public, Private and Protected

# Public ==> Normal Variables or Functions.

# Private ==> Used only inside the class and cannot be accessed by objects or classes inheritance (use __(double underscore))

# Protected ==> Almost same as public (use _(single underscore))

class Access:

# The __class_Var is a private class variable.

    __class_Var = 10

# __Method is a private method.

    def __Method(self):

        print("Hello World")

    def print_private(self):

        print(self.__class_Var)
        self.__Method

Object = Access()

# Private variables or methods cannot be used or modified outside the class.

# Object.__Method()
# print(Object.__class_Var)
# print(Access.__class_Var)

Object.print_private()