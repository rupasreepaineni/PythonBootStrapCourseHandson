from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0 #helps with iteration of 25 work/5 min break counts
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    #1. time reset =00:00,time_label = timer, reset_check_marks as well
    canvas.itemconfig(timer_text,text="00:00")
    my_label.config(text = "Timer")
    check_mark.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        count_down(long_sec)
        my_label.config(text = "Break",fg = RED)
    elif reps % 2 ==0:
        count_down(short_sec)
        my_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #print(count)
    count_min = math.floor(count/60)
    count_sec = count% 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    # we've to keep the timer into the tomato and to do that we need to tap into canvas with,itemconfig method
    #the item name we want to tap into,and the text we want to add
    if count>0:
        global timer
        timer = window.after(1000,count_down,count - 1)
        # this takes input as a function and works on keyword arguments
    else: # this for the check mark addition for every work rep
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+= "✔"
            check_mark.config(text = marks )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50,bg=YELLOW)

my_label = Label(text = "Timer",font= (FONT_NAME,30,"bold"),bg= YELLOW) #making font
# (it takes input as a tuple) bigger, background to yellow
my_label.grid(column = 1, row =0)

#created canvas and made tomato image visible on to the screen
tomato = PhotoImage(file="tomato.png") # photoimage a class from tkinter which helps to read the image
canvas = Canvas(width=210,height=230,bg=YELLOW,highlightthickness=0) #this width ad height can be fteched from the image dimensions
#it's like normal canvas, which helps to draw the things, highlightthickness this makes square invisible around tomato
canvas.create_image(103,120,image = tomato) #placing image at center,half of canvas height
timer_text = canvas.create_text(110,140,text="00:00",fill = "white", font= (FONT_NAME,35,"bold")) #placing text inside the tomato
canvas.grid(column=1, row=1)


#working on the buttons
#This makes the middle column expand, pushing Start left and Reset right
window.columnconfigure(1, weight=1)

Start_button =Button(text="Start",highlightthickness =0,command = start_timer)
Start_button.grid(column =0,row = 2)
Reset_button =Button(text="Reset",highlightthickness =0,command = reset_timer)
Reset_button.grid(column =2,row = 2)

check_mark = Label(fg = GREEN,bg = YELLOW, font= (30))
check_mark.grid(column = 1,row = 3)


window.mainloop()
