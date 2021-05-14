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

        # Initial Instructions (row 1)
        self.quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text=" Welcome to the Golf Quiz Game. "
                                               " Each question will be randomly "
                                               " generated. Try answer as many "
                                               " correct as possible."
                                               " Don't forget to have a good game!!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Number Question Heading (row 2)
        self.start_frame_label = Label(self.start_frame, text="How many Questions would you like to answer?",
                                       font="Arial 19 bold")
        self.start_frame_label.grid(row=2)

        # Entry box & Button (row 3)
        self.start_amount_entry = Entry(self.start_frame, width=200)
        self.start_amount_entry.grid(row=3)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 14 bold", width=10)
        self.start_amount_entry.grid(row=0, column=1)
        
        self.number_error_label = Label(self.start_frame, fg="blue",
                                        text="", font="Arial 10 bold",
                                        justify=LEFT)
        self.number_error_label.grid(row=3)

        # button frame (row 4)
        self.start_frame = Frame(self.start_frame)
        self.start_frame.grid(row=4)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange start button
        self.start_button = Button(self.start_frame, text="Start",
                                   font=button_font, bg="#FF9933")
        self.start_button.grid(row=0, column=0, pady=10)
        # Blue select button
        self.select_button = Button(self.select_frame, text="Select",
                                    font=button_font, bg="#3399FF")
        self.select_button.grid(row=0, column=0, pady=10)

    def number_amount(self): 
        number_balance = self.number_amount_entry.get()

        # Set error background colours (and assume that there are no)
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        try:
            number_balance = int(number_balance)

            if number_balance < 10:
                has_errors = "yes"
                error_feedback = "Sorry, the minimum amount of questions you can play with is 10"
            elif number_balance > 50:
                has_errors = "yes"
                error_feedback = "Sorry, the maximum amount of questions you can play with is 50"

        except ValueError:
                has_errors = "yes"
                error_feedback = "Enter a number please (no decimals / text)"

    def to_play(self, amount_entry):

        # Retrieve number amount
        number_balance = self.number_amount.get()

        Game(self. amount_entry)

        # hide start up window
        root.withdraw()

class Game:
    def __init__(self, partner, amount_entry):
        print(amount_entry)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Golf Quiz Game")
    something = Start(root)
    root.mainloop()