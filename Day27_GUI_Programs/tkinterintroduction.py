from tkinter import *
#Tkinter is the standard GUI (Graphical User Interface) library for Python.
# It provides a way to create windows, buttons, text boxes, and menus that
# users can interact with using a mouse and keyboard, rather than just using a command-line interface.

window = Tk()
window.title("My First GUI Program")
window.minsize(400,400)



#Label
my_label = Label(text="My First GUI Program",font=("Arial",20))
# ****basically, whatever we intiliaze in object/using inbuilt functions needs to get the value while declaring object
# but if we don't give values during object creation it runs through error,
# inorder to eradicate this we need to use get function, if no value is given it returns "NONE"
# ***The same way the inbuilt functions will be having multiple args
# whatever we want will only be used by assigning like get function



my_label.pack() #it's like a layout helps to keep the text/paste into the window,
# turtle.write() is as same as Label+pack
# my_label.pack(expand = True)
# my_label.pack(side = "left")
#changing/updating the label
my_label["text"] = "Updated screen"
my_label.config(text="This is my label")



def button_click():
    print("button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    #this helps to get change the text after button gets clicked



#ENTRY
input = Entry(width = 30)
input.pack()


#creating the button
button = Button(window,text="Click me", command=button_click)
button.pack()#it's like a layout helps to keep the text/paste into the window,







window.mainloop()
#this is similiar to screen.exitonclick(), which helps to listen to keyboard interactions