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

        # button frame (row 3)
        self.start_frame = Frame(self.start_frame)
        self.start_frame.grid(row=5)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange start button
        self.start_button = Button(self.start_frame, text="Start Game",
                                   font=button_font, bg="#FF9933")
        self.start_button.grid(row=5, column=0, pady=5)
        

    def to_play(self):

        Game(self)

        # hide start up window
        # root.withdraw()

class Game:
    def __init__(self, partner):

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