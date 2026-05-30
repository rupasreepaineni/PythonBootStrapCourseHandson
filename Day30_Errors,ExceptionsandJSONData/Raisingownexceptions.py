# we can raise errors whatever we wanted to in the finally block and normal way we can do raise
#Raising errors in Type1: In final block
# try:
#     file = open("handson.txt")
#     # a_dict = {"key":"value"}
#     # print(a_dict["dhgfhjf"])
# # except : # this eradicates complete error
# #     file = open("handson.txt", "w")
# #     file.write("something")
# except FileNotFoundError: #this works only file errors
#     file = open("handson.txt", "w")
#     file.write("something")
# finally:
#     raise TypeError('This exception was raised')

#Raising error in general way
height = int(input("Enter your height:"))
weight = float(input("Enter your weight:"))

if height > 3:
    raise ValueError("Your height is too big")

bmi = weight/height**2
print(f"Your BMI is {bmi}")

