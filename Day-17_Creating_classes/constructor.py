
class User_Add:
    pass

user_a = User_Add() #here we're creating object of the class User_Add
user_a.id = 1
user_a.name = "John"
print(user_a.name )

class With_Constructor:
    def __init__(self ,id ,username):
        print("This is the constructor method")
        self.id = id
        self.username = username

#**while creating object of the class ,
# **we've to pass the attributes which are defined in the constructor method
user_b = With_Constructor(3 ,"Levis") #here we're creating object of the class With_Constructor
#user_b(3,"Levis") #here we're calling the constructor method of the class With_Constructor
# ,we can't use this

print(user_b.id)
