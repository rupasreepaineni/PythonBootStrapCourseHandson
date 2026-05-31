THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizUi:
    def __init__(self,quiz_brain:QuizBrain): #we want know from where it is coming
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        #scorelabel
        self.score_label = Label(text="Score: 0", fg="white", bg = THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        #canvas
        self.canvas = Canvas( width = 300, height = 250,bg="white")
        self.questions= self.canvas.create_text(120,125,width = 230, text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
#it's important to give the placement of width and height of the canvas to place the text in the center
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        #true button
        true_image = PhotoImage(file = "images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,command = self.true_pressed)
        self.true_button.grid(row=2, column=0)
        #false button
        false_image = PhotoImage(file = "images/false.png")
        self.false_button = Button(image = false_image, highlightthickness=0,command = self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white") # this will change the background color of canvas to white for the next question
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question() #going to that function and fetching the question text
            self.canvas.itemconfig(self.questions, text=q_text)
        else:
            self.canvas.itemconfig(self.questions, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled") # this will disable the true button
            self.false_button.config(state="disabled") # this will disable the false button


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        # above two lines can be rewritten as self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question) # this will call the get_next_question after 1000ms
#first change the background color of canvas to green or red based on the answer and then after 1 second ,
# call the get_next_question,
# function to fetch the next question and change the background color back to white,
#then screen will be ready for the next question and canvas needs to refreshed means
# change the background color back to white, so that it is ready for the next question