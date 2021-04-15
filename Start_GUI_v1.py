from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get user to start game
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Golf Quiz Heading (row 0)
        self.start_frame_label = Label(self.start_frame, text="Golf Quiz",
                                       font="Arial 19 bold")
        self.start_frame_label.grid(row=0)

        # Initial Instructions (row 1)
        self.quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text=" Welcome to the Golf Quiz. "
                                               "There are 50 questions that"
                                               " will randomly generate. Try"
                                               " answer as many as possible."
                                               " Don't forget to have a good game!!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # button frame (row 2)
        self.start_frame = Frame(self.start_frame)
        self.start_frame.grid(row=3)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange start button
        self.start_button = Button(self.start_frame, text="Start",
                                   font=button_font, bg="#FF9933")
        self.start_button.grid(row=0, column=0, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Golf Quiz")
    something = Start(root)
    root.mainloop()