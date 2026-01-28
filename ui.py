from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizze")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label =  Label(text="score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canva=Canvas(width=300,height=250,bg="white")

        self.question_text =self.canva.create_text(150,125,width=280,text="some Question text", font=("Arial", 20, "italic"),fill=THEME_COLOR)
        self.canva.grid(row=1,column=0,columnspan=2,pady=50)
        cross_img = PhotoImage(file="images/false.png")
        self.unknown_button =Button(image=cross_img,highlightthickness=0,command=self.check_pressed)
        self.unknown_button.grid(row=2,column=0)
        check_img = PhotoImage(file="images/true.png")
        self.known_button=Button(image=check_img,highlightthickness=0,command=self.wrong_pressed)
        self.known_button.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text, text=q_text)
        else:
            self.canva.itemconfig(self.question_text,text="you reach the end of the quiz")
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")
    def check_pressed(self):
         self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
         is_right = self.quiz.check_answer("False")
         self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000,self.get_next_question)

