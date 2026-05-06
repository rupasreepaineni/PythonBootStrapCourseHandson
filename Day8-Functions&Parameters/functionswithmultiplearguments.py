#positional arRANGEMENT- Is far important in the functions with multiple args
#if we send the data to the function it'll be assigned to the respective arguments
#functional arguments
def wishes(name, location):
    print(f"GoodMorning {name}")
    print("Have a good day")
    print(f"How is it to be like in {location}")
    print("How is it to be like in " + location)
wishes("Angela", "India") #positional arguments, no need to specify takes as it is
wishes(location = "India" , name =  "Sardar")
#keyword arguments, we can specify the name of the parameter and assign the value to it, no need to follow the order of the parameters
#param = value;no need of "" either string or anything**
#Keyword Arguments