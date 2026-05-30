

import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#STEP7
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    #letter_pass = [random.choice(letters) for char in range(random.randint(8, 10))]
    #as we're importing random we can remove the "random.randint(8, 10))" random from this
    letter_pass = [choice(letters) for char in range(randint(8, 10))]
    symbol_pass= [choice(symbols) for char in range(randint(2, 14))]
    number_pass = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letter_pass + symbol_pass + number_pass

    shuffle(password_list)
    print(password_list)
    password = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")
    #ENTRY PASSWORD
    Password.insert(0,password)
    #pyperclip - helps in copy and pasting the clipboard functions
    pyperclip.copy(password)

#---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Step3:- to get input for entry functions we use .get()
    website = Website_input.get()
    email = Email_label.get()
    password = Password.get()
    new_data = {website: { "email": email, "password" : password}}

    #STEP 6
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        #Modification-1
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                data = json.dump(new_data, data_file, indent=4)
                data.update(new_data)

        else:
            # update the data with existing data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            Website_input.delete(0, END)
            Email_label.delete(0, END)
            Password.delete(0, END)


# ----------------------------  Ftehing password from JSON file while clicking on search ------------------------------- #

def find_password():
    search_name = Website_input.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
            if search_name in data:
                email = data[search_name]["email"]
                password = data[search_name]["password"]
                messagebox.showinfo(search_name, f"Email: {email}\n Password: {password}")
            else:
                messagebox.showerror("Error", f"No details for {search_name} exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx =50,pady= 50)

#STEP2: Creating labels,Entry and buttons
Website_label = Label(text= "Website:")
Website_label.grid(column = 0, row = 1)
Website_input = Entry(width = 30)
Website_input.focus() #helps to have a cursor at that particular one
Website_input.grid(column = 2, row = 1,columnspan = 2)

Email_label = Label(text= "Email/Username:")
Email_label.grid(column = 0, row = 2)
Email_label = Entry(width = 30)
Email_label.insert(0,"angela@gmail.com") #helps to have a dummy one
Email_label.grid(column = 2, row = 2,columnspan = 2)
#Label and entry for password
Password = Label(text= "Password:")
Password.grid(column = 0, row = 3)
Password = Entry(width = 21)
Password.grid(column = 2, row = 3,columnspan = 2)

#Generate password button
Generate_password = Button(text= "Generate_password",command= password_generator)
Generate_password.grid(column = 4, row = 3)
#Add button
Add = Button(text= "Add",command=save)
Add.grid(column = 1, row = 4,columnspan = 4)
#Generate search button
Search = Button(text= "Search",width = 10 ,command= find_password)
Search.grid(column = 4, row = 1)


#STEP1:Adding the image
#created canvas and made logo image visible on to the screen
Lock_Image = PhotoImage(file="logo.png") # photoimage a class from tkinter which helps to read the image
canvas = Canvas(width=200,height=200) #this width ad height can be fteched from the image dimensions
#it's like normal canvas, which helps to draw the things, highlightthickness this makes square invisible around tomato
canvas.create_image(100,100,image = Lock_Image) #placing image at center,half of canvas height
canvas.grid(column=2, row=0)


window.mainloop()