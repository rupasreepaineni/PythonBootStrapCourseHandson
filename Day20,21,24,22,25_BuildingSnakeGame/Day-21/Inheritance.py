# Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes
# code reusability and establishes a natural hierarchical relationship between classes.


#**to use an attribute - objectname.attributename

class Animal:
    def __init__(self):
        self.eyes = 2
    def breathe(self):
        print("Inhale, Exhale")

class Dog(Animal): #in the braces just mention the parent class name, so that it inherits everything
    def __init__(self):
        super().__init__() #** this is the initialzation of the parent class,
        # so that we can access the parent class attributes and methods in the child class
        self.legs = 4
    def bark(self):
        print("Woof!")


    #enhancing the existing method
    def breathe(self):
        super().breathe() #** this is the method of the parent class,
        # so that we can access the parent class method in the child class
        print("Dog is breathing") #and we can add any extra whatever we want

# Create an instance of the Dog class
jimmy = Dog()
jimmy.bark() # by just creating child class instance we can access to the parent as well
jimmy.breathe()
print(jimmy.eyes)