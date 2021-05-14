import csv
import re

class Play:
    def __init__(self, parent):

    # *** generate question dictonary ***
    # open file
    questions = open('Copy of golf_quiz')

    # Read data into a list
    csv_questions = csv.reader(questions)

    # Create a dictoinary to hold data
    question_dictonary = {}

    # Add the data from the list into the dictonary
    # (first item in row is key, next is defenition.)

    for row in question_dictonary:


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()