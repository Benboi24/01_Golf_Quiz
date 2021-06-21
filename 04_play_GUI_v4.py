from os import error
from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv


class Quiz:
    def __init__(self, parent):

        # Buttons styling here...
        button_font = "Arial 13 bold"

        # GUI to get user to start game
        self.play_frame = Frame(padx=10, pady=10)
        self.play_frame.grid()

        # Set intial amount of games to zero
        # retireve the initial amount they selected in play GUI
        self.question_amount = IntVar()
        self.question_amount.set(0)

        self.right_ans = StringVar()

        # Golf Quiz Heading (row 0)
        self.start_frame_label = Label(self.play_frame, text="Golf Quiz Game",
                                       font="Arial 19 bold")
        self.start_frame_label.grid(row=0)

        # Initial Instructions, Question instructions (row 1 & 2)
        self.quiz_instructions = Label(self.play_frame, font="Arial 10 italic",
                                          text=" Press next question when you have answered. ",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Question Goes Here
        self.quiz_question_label = Label(self.play_frame, fg="Blue",
                                         text="Question Goes Here", font="Arial 14 bold",
                                         wrap=275, justify=LEFT)
        self.quiz_question_label.grid(row=2)
                        
        # Statement Heading, entry box & Buttons (row 3)
        self.entry_error_frame = Frame(self.play_frame, width=10)
        self.entry_error_frame.grid(row=3)

        self.answer_entry = Entry(self.entry_error_frame, font="Arial 14 bold", width=10)
        self.answer_entry.grid(row=0)

        # Yellow Select Button
        self.check_button = Button(self.entry_error_frame, text="Check",
                                   font=button_font, bg="#FFFF33", command=self.check)
        self.check_button.grid(row=0, column=1, pady=10, padx=5)

        # Will have total questions each time you answer one
        self.number_error_label = Label(self.play_frame, fg="red",
                                        text="errors go here", font="Arial 10 bold",
                                        justify=LEFT)
        self.number_error_label.grid(row=4)

        # Next Frame & Button (row 5)
        self.next_frame = Frame(self.play_frame, width=20)
        self.next_frame.grid(row=5)
        
        self.next_button = Button(self.next_frame, text="Next Question", width = 19,
                                 font=button_font, bg="#FF0080", command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

        # Help, Status, Dismiss & Next Buttons 
        self.hsd_frame = Frame(self.play_frame)
        self.hsd_frame.grid(row=6)

        # Green Help Button
        self.help_button = Button(self.hsd_frame, text="Help",
                                   font=button_font, bg="#009900",)
        self.help_button.grid(row=0, column=0, padx=6)

        # Blue Stats Button
        self.stats_button = Button(self.hsd_frame, text="Stats",
                                   font=button_font, bg="#FF0000")
        self.stats_button.grid(row=0, column=1, padx=6)
        # Purple Dismiss Button
        self.dismiss_button = Button(self.hsd_frame, text="Dismiss",
                                    font=button_font, bg="#B266FF")
        self.dismiss_button.grid(row=0, column=2, padx=6)

        # button frame (row 3)
        self.start_frame = Frame(self.play_frame)
        self.start_frame.grid(row=5)  

        # Disable next question button at start
        # self.next_button.config(state=DISABLED)
        
    def next_question(self):
        # Open file
        with open('golf_v3.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        
        # print(data)

        # Randomly selects a question from csv
        question_ans = random.choice(data)
        print(question_ans)
        question = question_ans[0]
        answer = question_ans[1]

        self.right_ans.set(answer)
        
        # Prints the question
        print(question)
        print(answer)

        self.quiz_question_label.config(text=question)


    def check(self):

        print("you pushed check")

        right_ans = self.right_ans.get()
        print(right_ans)

        answer_entry = self.answer_entry.get()
        print(answer_entry)

        # Printing out wether the answer is right or incorrect
        if answer_entry == right_ans:
            print("You are correct!!")
        else:
            print("sorry, the answer is", right_ans)

            self.number_error_label.config(text=error)

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
        self.dismiss_btn.grid(row=2)
        

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
    something = Quiz(root)
    root.mainloop()