# if -else

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 120:
    print("you can have a fun ride")
    if age >=12 and age <=18:
        print("your ticket is $7")
        bill = 7
    elif age <=12:
        print("your ticket is $6")
        bill = 6
    elif age >=45 and age<=55:
        print("Ride is on us, Have fun!")
    else:
        print("your ticket is $12")
        bill = 12
    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        bill += 3
    else:
        bill = bill

    print(f" Your bill is {bill}")
else:
    print("You can not ride")