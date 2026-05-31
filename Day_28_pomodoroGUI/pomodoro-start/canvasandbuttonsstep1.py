from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50,bg=YELLOW)

my_label = Label(text = "Timer",fg=GREEN,font= (FONT_NAME,30,"bold"),bg= YELLOW) #making font
# (it takes input as a tuple) bigger, background to yellow
my_label.grid(column = 1, row =0)

#created canvas and made tomato image visible on to the screen
tomato = PhotoImage(file="tomato.png") # photoimage a class from tkinter which helps to read the image
canvas = Canvas(width=210,height=230,bg=YELLOW,highlightthickness=0) #this width ad height can be fteched from the image dimensions
#it's like normal canvas, which helps to draw the things, highlightthickness this makes square invisible around tomato
canvas.create_image(103,120,image = tomato) #placing image at center,half of canvas height
canvas.create_text(110,140,text="00:00",fill = "white", font= (FONT_NAME,35,"bold")) #placing text inside the tomato
canvas.grid(column=1, row=1)

#working on the buttons
#This makes the middle column expand, pushing Start left and Reset right
window.columnconfigure(1, weight=1)

Start_button =Button(text="Start",highlightthickness =0)
Start_button.grid(column =0,row = 2)
Reset_button =Button(text="Reset",highlightthickness =0)
Reset_button.grid(column =2,row = 2)

check_mark = Label(text = "✔",fg = GREEN,bg = YELLOW, font= (30))
check_mark.grid(column = 1,row = 3)


window.mainloop()
