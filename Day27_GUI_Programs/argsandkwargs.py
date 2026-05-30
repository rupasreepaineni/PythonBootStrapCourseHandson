#sending multiple args and adding them
"""1.Unlimited positional arg *args"""
# def add(*args):
#     print(args[0])
#     j = 0
#     for i in args:
#         j=j+i
#     print(j)


# add(1,2,3)
# add(1,2,3,10,40,60) # we can pass as many as we want

#Many Keyword args- **kwargs
def choose(k,**kwargs):
    print(type(kwargs))
    print(kwargs)
    # for key,value in kwargs.items():
    #     #print(key,value)
    k += kwargs["add"]  # 4+2
    print(k)
    k *= kwargs["multiply"]  # 6*6
    print(k)

choose(2,add=4,multiply =6)


# class Car():
#
#     def __init__(self, **kw):
#         self.make = kw("make")
#         self.model = kw("model")
#         print(car.make)
#         print(car.model)

# car = Car(make = "Nissan")
# ****basically, whatever we intiliaze in object/using inbuilt functions needs to get the value while declaring object
# but if we don't give values during object creation it runs through error,


# inorder to eradicate this we need to use get function, if no value is given it returns "NONE"
# ***The same way the inbuilt functions will be having multiple args
# whatever we want will only be used by assigning like get function
class Car():

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")
        self.seats = kw.get("seats")
        self.colour = kw.get("colour")


car = Car(make = "Nissan")
print(car.make)
print(car.model)



