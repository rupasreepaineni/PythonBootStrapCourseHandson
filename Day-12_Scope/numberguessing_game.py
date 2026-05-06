import random
computer_num = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
print(computer_num)

def finding_number(attempts):
    our_num = int(input("Make a guess:"))
    while attempts > 0:
        if our_num == computer_num:
            print(f"You got it! The answer was {our_num}.")
            return our_num
        if attempts == 0:
            print("You lost and You've run out of guesses, you lose.")
        elif our_num > computer_num:
            attempts -= 1
            print("Too high.")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
            our_num = int(input("Make a guess:"))
        else:
            attempts -= 1
            print("Too low.")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
            our_num = int(input("Make a guess:"))



if difficulty == "easy":
    attempts = 10
    finding_number(attempts)
else:
    attempts = 5
    finding_number(attempts)




