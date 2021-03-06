import csv
from os import startfile
import random
# from tkinter import Button, Frame, Label, Toplevel
from tkinter import *

from tkinter.constants import DISABLED, LEFT


class Game:
    def __init__(self, parent, question_amount):

        # GUI Setup
        self.game_box = Toplevel()

        # If users press cross at top, quiz quits
        self.game_box.protocol("WN_DELETE_WINDOW", self.to_quit)

        # Golf Quiz Heading (row 0)
        self.start_frame_label = Label(self.start_frame, text="Golf Quiz Game",
                                        font="Arial 19 bold",padx=10,
                                        pady=10)
        self.start_frame_label.grid(row=0)

        # Instructions Label (row 1)
        self.golf_instructions = Label(self.start_frame, font="Arial 10 italic",
                                        text="Press Next when you have answered the question.",
                                        wrap=275, justify=LEFT, padx=10, pady=10)
        self.golf_instructions.grid(row=1)

        
        # *** generate question dictonary ***
        # open file
        questions = open('Copy of golf_quiz')

        # Read data into a list
        csv_questions = csv.reader(questions)

        # Create a dictoinary to hold data
        question_dictonary = {}

        data = 'Copy of golf_quiz'

        question_ans = random.choice(data)
        question = question_ans[0]
        answer = question_ans[1]

        print(question)
        print(answer)
        
class Help:
    def __init(self,partner, partial):

        # disable help button
            partner.help_button.config(state=DISABLED)

            # Sets up child window (ie: help box)
            self.help_box = Toplevel()

            # If users press cross at top, closes help and 'releases' help button
            self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

            # Set up GUI Frame
            self.help_frame = Frame(self.help_box, width=300)
            self.help_frame.grid()

            # Set up Help heading (row 0)
            self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                    font="arial 14 bold")
            self.how_heading.grid(row=0)

            help_text="This game is a quiz on general knowledge of Golf "\
            "ranging from dates, people and places. "\
            "Maximum of 50 questions per round. "\
            "Once finished you can export answers & questions to a separate file. " 
            "Even if you don't know take a guess, " 
            "enjoy the quiz and try get 100%!"

            # Help text (label, row 1)
            self.help_text = Label(self.help_frame, text=help_text,
                                justify=LEFT, wrap=400, padx=10, pady=10)
            self.help_text.grid(row=1)

            # Dismiss Button (row 2)
            self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                    width=10, bg="#660000", fg="white",
                                    font="arial 16 bold")
     

class GameStats:
    def __init__(self, partner, quiz_history, partial):
    
        print(quiz_history)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                            partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                        font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

    def to_quit(self):
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Golf Quiz Game")
    something = Start(root)
    root.mainloop()