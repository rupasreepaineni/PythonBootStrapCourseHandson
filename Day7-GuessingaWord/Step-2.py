

import random
from logging import PlaceHolder

word_list = ["ardvark", "baboon", "camel"]
choice = random.choice(word_list)
print (choice)
choice_length = len(choice)
print(f"The word has {choice_length} letters.")
#TODO-1 CREATE A PLACEHOLDER WITH THE SAME NUMBER OF BLANKS AS THE LETTERS IN THE CHOSEN WORD
place_holder = ""
for i in range(choice_length):
    place_holder += "_"
print(place_holder)


#TODO-2 : ASK THE USER TO GUESS A LETTER AND CHECK IF THE LETTER IS IN THE WORD and place in it

user_input = input("Guess a letter: ").lower()
display =""
for letter in choice: #extracr the letter in the word one by one

    if letter == user_input:
        display += letter
    else:
        display += "_"
print(display)