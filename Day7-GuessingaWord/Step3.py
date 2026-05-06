import random
word_list = ["large", "big", "camel"]
choice = random.choice(word_list)
print (choice)
choice_length = len(choice)
print(f"The word has {choice_length} letters.")
place_holder = ""
for i in range(choice_length):
    place_holder += "_"
print(place_holder)
#TODO-1: USE A WHILE LOOP TO CONTINUE ASKING THE USER TO GUESS A LETTER UNTIL THEY HAVE GUESSED ALL THE LETTERS IN THE WORD
game_over = False
correct_letters = []

while not game_over:
    user_input = input("Guess a letter: ").lower()
    display = ""
    #todo-2: INCLUDE WHILE LOOP TO CONTINUE ASKING THE USER TO GUESS A LETTER UNTIL THEY HAVE GUESSED ALL THE LETTERS IN THE WORD

    for letter in choice:  # extract the letter in the word one by one
        if letter == user_input:
            display += letter
            correct_letters.append(letter) # we can use user_input as well
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("Congratulations! You guessed the word!")
