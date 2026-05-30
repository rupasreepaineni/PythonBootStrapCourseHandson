from tkinter import *

window = Tk()
window.title("Grid Example")
window.minsize(400, 400)
window.config(padx=400,pady=400)

my_label = Label(text = "My Learning screen")
my_label.grid(row = 0, column = 0)

def button_click():
    print("Button clicked")
    new_text = my_input.get()
    my_label.config(text = new_text)

#ENTRY
my_input = Entry(width = 30)
my_input.grid(row = 4, column = 4)

#creating the button
button = Button(window,text="Button", command=button_click)
button.grid(row = 1, column = 1)#it's like a layout helps to keep the text/paste into the window,
button.config(padx=100,pady=200)

new_button =  Button(window,text="New Button")
new_button.grid(row = 0, column = 2)

window.mainloop()