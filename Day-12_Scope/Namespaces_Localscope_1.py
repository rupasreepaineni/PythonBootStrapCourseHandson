#errors- nameerror- something that is not defined(eg:variable name )
#Global variable- variable that is defined outside of a function and can be accessed anywhere in the code
#Local variable- variable that is defined inside a function and can only be accessed within that function
#this local and global is applicable for the functions as well(function inside a function)

name = "Her"

def he():
    name = "She"
    print(f"{name} is the best thing happened to him")

he()
print(f"{name} is the best thing happened to him")


def oy():
    def greet():
        name = "You"
        print(f"{name} are the best thing happened to him")
    greet() #here we can call/use the function inside the oy function,outside it won't work

oy()#this function will call the greet function and
#print the statement  *if you call only the greet function