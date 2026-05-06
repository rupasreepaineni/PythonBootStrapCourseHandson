import random
user_choice = int (input("Type 0 for Rock, Type 1 for paper and Type 3 for Scissors"))

computer_choice= random.randint(0,2)
a = ["Rock","Paper","Scissors"]
print(computer_choice)
if user_choice == 0 and computer_choice == 2:
    print("You won")
elif user_choice > computer_choice :
    print("You won")
elif user_choice < computer_choice :
    print("Computer won")
elif user_choice == computer_choice:
    print("it's a draw")
else:
    print("Invalid")

