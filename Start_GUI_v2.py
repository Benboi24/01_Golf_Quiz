from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get user to start game
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set intial amount of games to zero
        self.number_amount = IntVar()
        self.number_amount.set(0)

        # Golf Quiz Heading (row 0)
        self.start_frame_label = Label(self.start_frame, text="Golf Quiz Game",
                                       font="Arial 19 bold")
        self.start_frame_label.grid(row=0)

        # Initial Instructions, Question instructions (row 1 & 2)
        self.quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text=" Welcome to the Golf Quiz Game. "
                                               " Each question will be randomly "
                                               " generated. Try answer as many "
                                               " correct as possible."
                                               " Don't forget to have a good game!!", wrap=275,
                                          fg="green", justify=CENTER, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        self.question_instructions = Label(self.start_frame, font="Arial 10 bold",
                                                text="How many questions would you like? ",
                                                wrap=275, justify=CENTER, padx=10, pady=10)
        self.question_instructions.grid(row=2)

        # Question Heading, entry box & Button (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=10)
        self.entry_error_frame.grid(row=3)

        self.start_amount_entry = Entry(self.entry_error_frame, 
                                        font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=4)

        self.number_error_label = Label(self.start_frame, fg="red",
                                        text="", font="Arial 10 bold",
                                        justify=LEFT)
        self.number_error_label.grid(row=4)

        # button frame (row 3)
        self.start_frame = Frame(self.start_frame)
        self.start_frame.grid(row=5)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange start button
        self.start_button = Button(self.start_frame, text="Start Game",
                                   font=button_font, bg="#FF9933", command=self.check_question_amount)
        self.start_button.grid(row=5, column=0, pady=5)
        
    def check_question_amount(self): 
        question_amount = self.start_amount_entry.get()

        # Set error background colours (and assume that there are no)
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change backgrounds to white for testing purpose
        self.start_amount_entry.config(bg="white")
        self.number_error_label.config(text="")

        try:
            question_amount = int(question_amount)

            if question_amount < 10:
                has_errors = "yes"
                error_feedback = "Sorry, the minimum amount of questions you can play with is 10"
            elif question_amount > 45:
                has_errors = "yes"
                error_feedback = "Sorry, the maximum amount of questions you can play with is 45"

        except ValueError:
                has_errors = "yes"
                error_feedback = "Enter a number please (no decimals / text)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.number_error_label.config(text=error_feedback)
        else:
            # Set question balance to amount entered by the user
            error_feedback = "Let's get started!!"
            self.number_amount.set(question_amount)

    def to_play(self):

        # Retrieve number amount
        question_amount = self.number_amount.get()

        Game(self. question_amount)

        # hide start up window
        # root.withdraw()

class Game:
    def __init__(self, partner, number_amount):
        print(number_amount)

        # GUI Setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Golf Quiz Game")
    something = Start(root)
    root.mainloop()