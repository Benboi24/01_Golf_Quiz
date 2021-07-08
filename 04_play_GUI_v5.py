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
        # Keeps track of how many questions have been answered
        self.question_amount = IntVar()
        self.question_amount.set(0)

        # Set limit of questions, depending on user entry in start GUI
        self.question_limit_amount = IntVar()
        self.question_limit_amount.set(10)

        self.num_right = IntVar()
        self.num_right.set(0)

        # List for holding statistics
        self.questions_asked = []

        # # game stats should be [right, total asked]
        # self.game_stats_list = [0, 0]

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
                                   font=button_font, bg="#009900",
                                   command=self.help)
        self.help_button.grid(row=0, column=0, padx=6)

        # Blue Stats Button
        self.stats_button = Button(self.hsd_frame, text="Stats",
                                   font=button_font, bg="#FF0000",
                                   command=lambda: self.stats(self.questions_asked))
        self.stats_button.grid(row=0, column=1, padx=6)
        
        # Purple Dismiss Button
        self.dismiss_button = Button(self.hsd_frame, text="Dismiss",
                                    font=button_font, bg="#B266FF", 
                                    command=self.close_quiz)
        self.dismiss_button.grid(row=0, column=2, padx=6)

        # button frame (row 3)
        self.start_frame = Frame(self.play_frame)
        self.start_frame.grid(row=5)  

        # Disable next question button at start
        self.check_button.config(state=DISABLED)
        
    def next_question(self):
        # Open file
        with open('golf_quiz_v5.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        # Update number of questions asked?
        num_asked_so_far = self.question_amount.get()
        num_asked_so_far += 1
        self.question_amount.set(num_asked_so_far)

        # Allows user to get help before and during the game
        self.help_button.config(state=NORMAL)

        progress_label = "Question {} of {}".format(num_asked_so_far, 10)
        self.number_error_label.configure(text= progress_label, fg="black")
        
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

        self.check_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)


    def check(self):

        # retrieve question number for question_list
        question_num = self.question_amount.get()

        var_num_right = self.num_right.get()

        print("you pushed check")

        self.next_button.config(state=NORMAL)

        right_ans = self.right_ans.get()
        print(right_ans)

        answer_entry = self.answer_entry.get()
        print(answer_entry)

        # Printing out wether the answer is right or incorrect
        if answer_entry == right_ans:
            print("Well done, the answer is", right_ans)
            error = "Well done, the answer is {}".format(right_ans)
            result = "correct"
            var_num_right += 1
            self.num_right.set(var_num_right)

        else:
            print("sorry, the answer is", right_ans)
            error = "sorry, the right answer is, {}".format(right_ans)
            result = "incorrect"

            self.number_error_label.config(text=error)
            self.number_error_label.config(text=error)

        question_summary = "Question {}: {}".format(question_num, result)
        self.questions_asked.append(question_summary)

            
    def close_quiz(self):
        root.destroy()

    def stats(self, question_summary):

        amount_asked = self.question_amount.get()
        amount_right = self.num_right.get()

        game_stats = [amount_right, amount_asked]

        GameStats(self, question_summary, game_stats)
 

    def help(self):
        get_help = Help(self)

class Help:
    def __init__(self,partner):

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
                                width=10, bg="#B266FF", fg="white",
                                font="arial 16 bold",
                                comman=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=15)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

class GameStats:
    def __init__(self, partner, quiz_history, game_stats):

        print("quiz history", quiz_history)

        print("game stats", game_stats)

        right_ans = game_stats[0]
        wrong_ans = game_stats[1] - game_stats[0]
        number_asked = game_stats[1]

        percent_right = right_ans / number_asked * 100

        correct_text = "Questions Correct: {}".format(right_ans)


        # wrong_ans = [1]
        # right_ans = [2]
        # game_stats = [3]

        # Add round results to statistics
        # round_summary = "{} {} {}".format(wrong_ans[1], right_ans[2],
        #                         game_stats[3])
        # self.round_stats_list.append(round_summary)
        # self.stats_button.config(state=NORMAL)
        # print(self.round_stats_list)

        # disable help button
        partner.help_button.config(state=DISABLED)

        heading = "Arial 13 bold"
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
        self.stats_heading_label = Label(self.stats_frame, text="Quiz Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Quiz Statistics. "
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)    

        # Questions Correct (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        self.stats_correct_label = Label(self.details_frame,
                                        text="Questions Correct:", font=heading,
                                        anchor="e")
        self.stats_correct_label.grid(row=0, column=1, padx=0)

        self.stats_correct_value_label = Label(self.details_frame, font=content,
                                              text="{}".format(right_ans),
                                              anchor="w")
        self.stats_correct_value_label.grid(row=1, column=1, padx=0)

        # Questions Incorrect (row 2.1)
        self.stats_incorrect_label = Label(self.details_frame,
                                          text="Questions Incorrect:", font=heading,
                                          anchor="e")
        self.stats_incorrect_label.grid(row=2, column=1, padx=0)

        self.stats_incorrect_value_label = Label(self.details_frame, font=content,
                                                text="{}".format(wrong_ans),
                                                anchor="w")
        self.stats_incorrect_value_label.grid(row=3, column=1, padx=0)

        # Percentage Correct (row 2.2)
        self.percent_correct_label = Label(self.details_frame,
                                          text="Percentage Overall:", font=heading,
                                          anchor="e")
        self.percent_correct_label.grid(row=4, column=1, padx=0)

        self.percent_correct_value_label = Label(self.details_frame,
                                                 text="%{}".format(percent_right),
                                                 anchor="w")
        self.percent_correct_value_label.grid(row=5, column=1, padx=0)

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, quiz_history, game_stats):
        Export(self, quiz_history, game_stats)
        
class Export:
    def __init__(self, partner, quiz_history, game_stats):

        self.filename_entry = None
        self.history_frame = None
        background = "#99FF99" # Green

        # disable stats button
        partner.export_button.config(state=DISABLED)

        # Sets up another window (iw: export box)
        self.export_box = Toplevel()

        # Users presses cross at the top right side closing window
        self.export_box.protocol("WM_DELETE_WINDOW",
                                partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_frame,
                                  text="Export / Instructions",
                                  font="arial 15 bold", bg=background)

        # Stats text (label, row 1)
        self.history_text = Label(self.history_frame, text="Please enter a filename "
                                                            "in the entry box below "
                                                            "then press save it"
                                                            "will then save to a "
                                                            "text file",
                                                            justify=LEFT, width=30,
                                                            bg=background, wrap=275)
        self.history_text.grid(row=1)

        # Filename Entry Box (row 2)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 15 bold", justify=CENTER)
        self.filename_entry.grid(row=2, pady=10)

        # Save / Cancel Frame(row 3)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (first row of the frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, quiz_history, game_stats)))
        self.save_button.grid(row=0, column=1)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    
    def save_history(self, partner, quiz_history, game_stats):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z-0-9_]"
        has_errors = "no"
        problem = ""

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == "":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_errors = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_errors = "yes"

        if has_errors == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file name to hold data
            f = open(filename, "w+")

            f.write("Golf Quiz Game\n\n")

        # close file
        f.close()

        # close dialouge
        self.close_export(partner)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


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