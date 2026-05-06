
#scope of a function, conditional statements
#local scope is only applicable to function but not to the conditional statements


number = 10


if number > 5:
    print(f"it's ok to print {number}")

print(f"it's ok to print {number}")

def high():# variable scope is applicable here
    num = 9
    if num > 5:
        print(f"it's ok to print {num}")
high()
#print(f"it's ok to print {num}") here the scope error will come like name error
