print("Welcome to the pizza delivery service!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
     bill += 15
elif size == 'M':
        bill += 20
elif size == "L":
        bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    elif size == "M" or size == "L":
        bill +=3
    else:
        print("you have ot selected any herbs, proceed further")
elif add_pepperoni == 'N':
    bill = bill
if extra_cheese == "Y":
    bill +=1
elif extra_cheese == "N":
    bill =bill
else:
    print("you've not selected any cheese option, proceed further")
print(f" your final bill is : $ {bill}")