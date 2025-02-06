from tkinter import *
from tkinter import ttk
from random import shuffle
from tkinter import messagebox

class TypingTest:
    def __init__(self, window):
        self.wpm = None
        self.YELLOW = "#f7f5dd"
        self.FONT_NAME = "Courier"
        self.COUNT = 60
        self.right = 0
        self.wrong = 0
        self.characters = 0
        self.running = False        # to know the difference B/W start and restart
        self.countdown_id = None    # represents the actual counter
        self.WORDS = ['the', 'and', 'that', 'have', 'for', 'not', 'with', 'you', 'this', 'but',
                      'his', 'from', 'they', 'say', 'her', 'she', 'will', 'one', 'all', 'would',
                      'there', 'their', 'what', 'out', 'about', 'who', 'get', 'which', 'when',
                      'make', 'can', 'like', 'time', 'just', 'know', 'take', 'people', 'into',
                      'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than',
                      'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also',
                      'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well',
                      'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day',
                      'most', 'are', 'was', 'such', 'here', 'take', 'long', 'may', 'before',
                      'too', 'never', 'through', 'much', 'should', 'mean', 'only', 'another',
                      'people', 'being', 'those', 'tell', 'very', 'feel', 'little', 'own',
                      'leave', 'put', 'between', 'both', 'end', 'follow', 'came', 'own', 'while',
                      'around', 'number', 'ever', 'live', 'under', 'run', 'small', 'home', 'watch',
                      'child', 'world', 'during', 'now', 'man', 'too', 'place', 'big', 'hand',
                      'next', 'night', 'point', 'show', 'part', 'against', 'sure', 'turn', 'day',
                      'hear', 'story', 'take', 'never', 'high', 'help', 'out', 'end', 'again',
                      'right', 'ever', 'keep', 'minute', 'mind', 'change', 'try', 'tell', 'least',
                      'stand', 'eye', 'more', 'reason', 'almost', 'few', 'girl', 'find', 'last',
                      'ever', 'hand', 'while', 'door', 'much', 'nothing', 'face', 'something',
                      'head', 'without', 'door', 'live']
        # UI
        self.window = window
        self.window.title("Typing Speed Test")
        self.window.config(padx=20, pady=20, bg=self.YELLOW)
        self.window.geometry("800x500")
        self.window.resizable(False, False)

        # entire window is a canvas here
        self.canvas = Canvas(width=400, height=190, highlightthickness=0, bg=self.YELLOW)
        self.keyboard = PhotoImage(file="assets/kb.png")
        self.canvas.create_image(200, 95, image=self.keyboard)
        self.canvas.grid(row=1, column=1, padx=20, pady=20)

        # canvas just for text appearing
        self.text_canvas = Canvas(width=650, height=30)
        self.text = self.text_canvas.create_text(325, 15, text="Words Appear Here", font=(self.FONT_NAME, 20, "normal"))
        self.text_canvas.grid(row=3, column=0, columnspan=2)

        # applies to all the labels
        self.style = ttk.Style()
        self.style.configure('TLabel', background=self.YELLOW, font=(self.FONT_NAME, 16, "bold"))

        self.title = ttk.Label(text="Welcome to Typing Speed Test")
        self.title.grid(row=0, column=1)

        # horizontal line
        self.separator = ttk.Separator(orient='horizontal')
        self.separator.grid(row=2, column=1, ipadx=380, pady=20)

        self.timer = ttk.Label(text="1 Min")
        self.timer.grid(row=4, column=1, pady=10)

        # input field
        self.text_field = ttk.Entry(width=25)
        self.text_field.config(state=DISABLED)
        self.text_field.grid(row=5, column=1)

        # buttons -----------------------------------------------------------------------------------------
        self.start_button = ttk.Button(text="Start", command=lambda: [self.start(), self.list_of_words()])
        self.start_button.grid(row=6, column=1, pady=10)

        self.restart_button = ttk.Button(text="Restart", command=self.restart)
        self.restart_button.grid(row=7, column=1)
        self.restart_button.config(state=DISABLED)

        self.guide = ttk.Button(text="Instructions", command= self.instructions)
        self.guide.grid(row=0, column=1,sticky=E)
        # ------------------------------------------------------------------------------------------------

    # function for countdown
    def count_down(self,sec):
        self.timer.config(text=f"{sec}")
        if sec > 0 and self.running:
            self.countdown_id = self.window.after(1000, self.count_down, sec - 1)
        else:
            self.running = False
            self.wpm = round(self.characters / 5)
            self.text_canvas.itemconfig(self.text, text=f"Right Words:{self.right}, Wrong Words:{self.wrong}, characters :{self.characters}",
                                        font=(self.FONT_NAME, 16, "normal"))
            self.timer.config(text=f"WPM :{self.wpm}")
            self.right = 0  # sets everything back to zero
            self.wrong = 0
            self.characters = 0
            self.start_button.config(state=NORMAL)
            self.start_button.focus()
            self.text_field.delete(0, "end")
            self.text_field.config(state=DISABLED)
            self.restart_button.config(state=DISABLED)

    # handles start button functionalities
    def start(self):
        if not self.running:
            self.running = True

            self.start_button.config(state=DISABLED)
            self.restart_button.config(state=NORMAL)

            self.count_down(self.COUNT)

    # handles restart button functionalities
    def restart(self):

        self.restart_button.config(state=DISABLED)
        self.text_field.delete(0,"end")
        self.text_field.config(state=DISABLED)

        if self.countdown_id:
            self.window.after_cancel(self.countdown_id)  # Stop the running timer

        self.text_canvas.itemconfig(self.text, text="Wait till countdown completes")
        self.timer.config(text="3")  # Start countdown
        self.window.after(1000, lambda: self.timer.config(text="2"))
        self.window.after(2000, lambda: self.timer.config(text="1"))
        self.window.after(3000, lambda: self.timer.config(text="Go!"))

        # After 4 seconds, reset and start timer
        self.window.after(4000, self.reset_and_start) # Reset timer

    # after 4 seconds, we need to call a function in order to restart timer
    def reset_and_start(self):
        self.restart_button.config(state=NORMAL)
        self.text_field.config(state=NORMAL)
        self.running = True
        self.list_of_words()
        self.count_down(self.COUNT)

    # handles user input
    def on_click_enter(self,event, word):
        if self.text_field.get() == word:
            self.characters = self.characters + len(word) + 1  # added 1 as a space
            self.right += 1
            self.text_field.delete(0, "end")
            self.list_of_words()
        else:
            print("Wrong")
            self.wrong += 1
            self.text_field.delete(0, "end")
            self.list_of_words()

    # displays word
    def list_of_words(self):
        self.text_field.config(state=NORMAL)
        self.text_field.focus()
        shuffle(self.WORDS)
        self.text_canvas.itemconfig(self.text, text=self.WORDS[0], font=(self.FONT_NAME, 20, "normal"))
        self.text_field.bind("<Return>", lambda event: self.on_click_enter(event, self.WORDS[0]))

    # handles instructions button functionalities
    def instructions(self):
        messagebox.showinfo(title="Instructions",message="--> Press 'Start' to begin the test.\n"
                                                         "--> Press 'Restart' to restart the test.\n"
                                                         "--> It will be a 60 seconds test and calculated WPM "
                                                         "will be displayed along with number of right words, "
                                                         "wrong words and characters typed.\n"
                                                         "--> Do note that wrong words are not considered for "
                                                         "calculating WPM.\n"
                                                         "NOTE : THE RESULTS ARE NOT ACCURATE SINCE THE WORDS "
                                                         "APPEAR ONE-BY-ONE WHICH RESULTS IN LOWER WPM.")



root = Tk()
app = TypingTest(root)
root.mainloop()