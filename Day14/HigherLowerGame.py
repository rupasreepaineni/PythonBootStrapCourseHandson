#import gamedata or below line directly we can use data
from gamedata import data
from log import high,vs
import random
print(high)

#TODO: Create a higher lower game that compares the followers of two accounts and ask the user to guess who has more followers, if the user is correct then add 1 to the score and repeat the process, if the user is wrong then game over and show the score
#TODO:1 Ftech the data from each dict and format [It's in a function-format data]
#TODO:2 pick one item randomly from the data and call it A
#TODO:3 pick one item randomly from the data and call it B
#TODO:4 then guess and compare the one with more followers, ask the user input
#TODO:5 if the guess is correct[user input], then add 1 to the score and repeat the process[Checkanswer]
#TODO:6 if the guess is wrong, then game over and show the score, Loop should be stopped or iterated[use while loop]
#TODO:7 #we've to swap the winner to A and pick other item as B
score = 0
"""Function that picks data randomly and returns the formatted string"""
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f" {name}, a {description}, from {country}."

"""function that compares the follower count of two accounts and returns the correct answer"""
def check_answer( account_A, account_B,user_guess):
    if account_A["follower_count"] > account_B["follower_count"]:
        return user_guess == "a"
    else:
        return user_guess == "b"

account_B = random.choice(data)
should_continue = True

while should_continue:
    #pick one item randomly from the data and call it A
    account_A = account_B

    #we've to swap the winner to A and pick other item as B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Compare B: {format_data(account_B)}")
    #then guess and compare the one with more followers, ask the user input
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(account_A, account_B, guess)
    # if the guess is correct, then add 1 to the score and repeat the process

    if is_correct:
        score += 1
        print(f"You're right!, Final score: {score}")
        should_continue = True
    else:
        should_continue = False
        print(f"Sorry, that's wrong.Final score: {score}")

















#if the guess is wrong, then game over and show the score













#print("Compare A:", *gamedata.data[0].values(), sep=",") -
# this just prints entire value from a separated column
# here we're just fteching the values whatever we want-
# print(gamedata.data[1]["name"], gamedata.data[1]["description"], gamedata.data[1]["country"])