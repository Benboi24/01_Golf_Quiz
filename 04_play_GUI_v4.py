from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # Buttons styling here...
        button_font = "Arial 12 bold"

        # GUI to get user to start game
        self.play_frame = Frame(padx=10, pady=10)
        self.play_frame.grid()

        # Set intial amount of games to zero
        self.number_amount = IntVar()
        self.number_amount.set(0)

        # Golf Quiz Heading (row 0)
        self.start_frame_label = Label(self.play_frame, text="Golf Quiz Game",
                                       font="Arial 19 bold")
        self.start_frame_label.grid(row=0)

        # Initial Instructions, Question instructions (row 1 & 2)
        self.quiz_instructions = Label(self.play_frame, font="Arial 10 italic",
                                          text=" Press next when you have answered the question. ",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Statement Heading, entry box & Buttons (row 2)
        self.entry_error_frame = Frame(self.play_frame, width=10)
        self.entry_error_frame.grid(row=3)

        self.answer_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.answer_entry.grid(row=0)

        # Yellow Select Button
        self.select_button = Button(self.entry_error_frame, text="Select",
                                   font=button_font, bg="#FFFF33")
        self.select_button.grid(row=0, column=1, pady=10, padx=5)

        # Will have total questions each time you answer one
        self.number_error_label = Label(self.play_frame, fg="red",
                                        text="errors go here", font="Arial 10 bold",
                                        justify=LEFT)
        self.number_error_label.grid(row=2)

        # Next Frame & Button (row 4)
        self.next_frame = Frame(self.play_frame, width=15)
        self.next_frame.grid(row=4)

        self.next_button = Button(self.next_frame, text="Next",
                                 font=button_font, bg="#FF0080")
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

        # Help, Status & Dismiss Buttons 
        self.hsd_frame = Frame(self.play_frame)
        self.hsd_frame.grid(row=5)

        # Green Help Button
        self.help_button = Button(self.hsd_frame, text="Help",
                                   font=button_font, bg="#009900")
        self.help_button.grid(row=0, column=0, padx=5)

        # Blue Stats Button
        self.stats_button = Button(self.hsd_frame, text="Stats",
                                   font=button_font, bg="#FF0000")
        self.stats_button.grid(row=0, column=1, padx=5)
        # Purple Dismiss Button
        self.dismiss_button = Button(self.hsd_frame, text="Dismiss",
                                    font=button_font, bg="#B266FF")
        self.dismiss_button.grid(row=0, column=2, padx=5)

        # button frame (row 3)
        self.start_frame = Frame(self.play_frame)
        self.start_frame.grid(row=5)     

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