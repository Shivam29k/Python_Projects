from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizaler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_lable.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_txt = self.canvas.create_text(
            150,
            125,  
            text="this is the question", 
            font=('arial', 20, 'italic'),
            width= 290
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.true_pressed)
        self.false_btn.grid(row=2, column=0)
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.false_pessed)
        self.true_btn.grid(row=2, column=1)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_lable.config(text=f"Score: {self.quiz.score}")
        print(self.quiz.question_number)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=q_text)
        else: 
            score = f"Final Score is : {self.quiz.score}/10"
            self.canvas.itemconfig(self.question_txt, text=score)
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))        

    def false_pessed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

