# always start with def keyword to define a function


#function without parameter
def wishes():
    print("Good Morning")
    print("Have a good day")
wishes()

#function with parameter(or input)
def fishes(name):
    print(f"Good Morning {name}")# if we wanted to print some statement without using cancatenation use f string
    print(f"Have a good day {name}!")
fishes("Angela")
# here name in function is called parameter and "Angela"(value which we pass) is called argument
#basically values are arguments and variable name are parameters
