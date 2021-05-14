from tkinter import *
from functools import partial   # To prevent unwanted windows

import random

class Play:
    def __init__(self, parent):

        # GUI to get user to start game
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Golf Quiz Heading (row 0)
        self.start_frame_label = Label(self.start_frame, text="Golf Quiz Game",
                                        font="Arial 19 bold")
        self.start_frame_label.grid(row=0)

    def get_tof_statements():
        statements = []
        statements.append(["The chances of making two holes-in-one in a round of golf are one in 67 million","T"])
        statements.append(["125,000 golf balls a year are hit into the water at the famous 17th hole of the Stadium Course at Sawgrass","T"])
        statements.append(["Golf was banned three times for years after it was invented because the Scottish government","T"])
        statements.append(["The avereage golfer has a one in 1,000 chance of getting a hole in one","F"])
        statements.append([" At one time golf balls were made from wood","T"])
        statements.append(["Golf has been played on the moon?","T"])


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()