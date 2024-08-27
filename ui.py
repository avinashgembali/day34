from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f"score:0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
                                150,
                                125,
                                # this width is for to fit the question
                                width=280,
                                text="something ... ",
                                fill=THEME_COLOR,
                                font=("Arial", 20, "italic")
                            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, height=100, width=100, highlightthickness=0, command=self.right_button_click)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, height=100, width=100, highlightthickness=0, command=self.wrong_button_click)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="end of the quiz!!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def right_button_click(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def wrong_button_click(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
