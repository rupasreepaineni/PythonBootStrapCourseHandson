from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(100, 100)
my_label =  Label(window, text = "Mile to Km Converter")
window.config(padx=40,pady=40)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles* 1.689
    km_output.config(text = f"{km}")


miles_input = Entry(width = 7)
miles_input.grid(row=0,column=1)

miles = Label(text= "Miles")
miles.grid(row=0,column=2)

is_equal_to = Label(window, text = "is equal to")
is_equal_to.grid(row=1,column=0)


km_output = Label(text = "0")
km_output.grid(row=1,column=1)

km = Label( text = "km")
km.grid(row=2,column=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2,column=1)


window.mainloop()