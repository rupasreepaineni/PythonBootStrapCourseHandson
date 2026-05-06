# TODO-1 : RANDOMLY CHOOSE A WORD FROM THE LIST

#TODO-2 : ASK THE USER TO GUESS A LETTER AND CHECK IF THE LETTER IS IN THE WORD

#TODO-3 : Check if the user has guessed all the letters in the word and if so, print a congratulatory message

word_list = ["ardvark", "baboon", "camel"]

import random

choice = random.choice(word_list)
print (choice)
choice_length = len(choice)
print(f"The word has {choice_length} letters.")

user_input = input("Guess a letter: ").lower()

for letter in choice: #extracr the letter in the word one by one
    if letter == user_input:
        print("You guessed a letter in the word!")
    else:
        print("Sorry, that letter is not in the word.")
