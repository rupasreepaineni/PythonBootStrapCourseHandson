from tkinter import *

window = Tk()
window.title("Layout Managers")
window.minsize(400,400)

my_label = Label(text = "Pack Place and Grid manager", font= ("Arial" , 15))
#my_label.pack(side = "right")
# my_label.place(x=60,y=30)
my_label.grid(column = 0, row = 0)

def button_click():
    print("button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#ENTRY
my_input = Entry(width = 30)
my_input.grid(row = 2, column = 2)

#creating the button
button = Button(window,text="Click me", command=button_click)
button.grid(row = 3, column = 5)#it's like a layout helps to keep the text/paste into the window,


window.mainloop()

