def name(f_name,l_name):
     """this is a doc string which can be reflected across that is written after function declaration """
     f_name = f_name.title()
     l_name = l_name.title()
     return f_name+l_name
final = name(input("what's your first name?"),input("what's your last name?")) # storing the output in a variable
print(final)