def name(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name+ l_name  #
final = name(input("what's your first name?"),input("what's your last name?"),) # storing the output in a variable
print(final)

#when we enter empty string there should be a valid message which can be printed through return statement
def name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Please enter a valid name" #here we're returning proper message
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name+ l_name
final = name(input("what's your first name?"),input("what's your last name?"),) # storing the output in a variable
print(final)