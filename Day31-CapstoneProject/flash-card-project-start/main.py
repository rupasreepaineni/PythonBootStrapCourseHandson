from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}
#---------------------------Reading CSV file---------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    words = data.to_dict(orient="records")
    # this helps to have the data in the form of list of dictionaries,
    # where each dictionary is a row in the csv file and the keys are the column names
else:
    words = data.to_dict(orient="records")


#STEP2: creating a card and showing the front of the card, with the help of canvas and images
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer) # to add extra time
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(back_img, image = card_front_img) #flipping from back image to front image, on the same canvas
    flip_timer = window.after(3000, func=flip_card)  # after 3 seconds it will call the next_card function


#STEP 4: after 3 seconds, the card will flip and show the English word,
# and also change the background image to back of the card
def flip_card():
    canvas.itemconfig(card_title, text="English",fill = "white")
    canvas.itemconfig(card_word, text=current_card['English'], fill ="white")
    canvas.itemconfig(back_img, image=card_back_img)  # to change the image to back of the card
    # , the first input has to be the image canvas size

#STEP5:#here if it clicks correct word then it has to remove that word from the list of words to learn, and then save the
# remaining words in a csv file, so that next time when we run the program it will show only the remaining words
#pass this function to known button
def is_known():
    words.remove(current_card) #removing the current record from the list of words to learn
    data = pandas.DataFrame(words) #creating a dataframe from the remaining words
    data.to_csv("data/words_to_learn.csv", index=False) #saving the remaining words to a csv file, index false is to avoid adding an extra column for index
    next_card()




#---------------------------STEP1: UI SETUP---------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
# photoimage a class from tkinter which helps to read the image
card_back_img = PhotoImage(file="./images/card_back.png")
#for fromt img
back_img = canvas.create_image(400,263,image = card_front_img) #placing image at center,half of canvas height
#for fromt img

canvas.grid(column=0, row=0,columnspan=2)  #if we mention/use grid it's important to use row and column
#column span helps to adjust the view of check and cross buttons
card_title = canvas.create_text(400,150, text= "Title", font=("Ariel", 40, "italic")) #title
card_word = canvas.create_text(400,263, text= "Word", font=("Ariel", 60, "bold")) #Italian word

#STEP 3: adding buttons, importing images for buttons
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image = cross_image,highlightthickness=0,command = next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image = check_image,highlightthickness=0,command = is_known)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()

