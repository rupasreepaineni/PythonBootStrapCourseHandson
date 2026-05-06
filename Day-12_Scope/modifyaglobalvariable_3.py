#it's a bp to avoid same global variable name as local scope variable
#All the constants will be maintained with uppercase inorder to avoid confusion,
# and also to make it clear that it's a constant variable and not a local variable
number = 10#for conditional statements the scope is till the end of the program**
if number > 5:
    number = 6
    print(f"it's ok to print {number}")

print(f"it's ok to print {number}")

#here global variable can't be modified,
# inside a function even the name of the variable is same, the scope will be till the end of function
hand = 2
def high():
    hand = 3
    print(f"it's ok to print {hand}")#the scope of variable if we update also it's only upto the function

high()
print(f"it's ok to print {hand}")#here it refers to the global variable and print 2
#because of the scope variable is global




#here we see how to update the global variable inside a function,
# we can't modify global variable directly but we can return the value and update it outside the function

hand = 2
def high(hand):
    hands = 4
    print(f"it's ok to print {hands}")
    return hand + 1

hand = high(hand)
print(f"it's ok to print {hand}")