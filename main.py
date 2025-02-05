from tkinter import *
from tkinter import ttk
from random import shuffle
from tkinter import messagebox

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
COUNT = 5
right = 0
wrong = 0
characters = 0

WORDS = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "know", "take", "people",
    "into", "year", "your", "good", "some", "could", "them", "see", "other", "than",
    "then", "now", "look", "only", "come", "its", "over", "think", "also", "back",
    "after", "use", "two", "how", "our", "work", "first", "well", "way", "even",
    "new", "want", "because", "any", "these", "give", "day", "most", "us", "are",
    "was", "is", "am", "such", "here", "take", "long", "may", "before", "too",
    "never", "through", "much", "should", "mean", "only", "another", "people", "being",
    "those", "tell", "very", "feel", "little", "own", "leave", "put", "between", "both",
    "end", "follow", "came", "own", "while", "around", "number", "ever", "live", "under",
    "run", "small", "home", "watch", "child", "world", "during", "now", "man", "too",
    "place", "big", "hand", "next", "night", "point", "show", "part", "against", "sure",
    "turn", "day", "hear", "story", "take", "never", "high", "help", "out", "end",
    "again", "right", "ever", "keep", "minute", "mind", "change", "try", "tell", "least",
    "stand", "eye", "more", "reason", "almost", "few", "girl", "find", "last", "ever",
    "hand", "while", "door", "much", "nothing", "face", "something", "head", "without",
    "door", "live"
]
def count_down(sec):
    global right, wrong, characters
    timer.config(text=f"{sec}")
    if sec > 0:
        window.after(1000,count_down,sec-1)
    else:
        wpm = round(characters / 5)
        text_canvas.itemconfig(text, text=f"Right Words:{right}, Wrong Words:{wrong}, characters :{characters}")
        timer.config(text=f"WPM :{wpm}")
        right = 0
        wrong = 0
        characters = 0
        start_button.config(state=NORMAL)
        start_button.focus()
        text_field.delete(0,"end")
        text_field.config(state=DISABLED)


def start():
    start_button.config(state=DISABLED)
    count_down(COUNT)

def on_click_enter(event,word):
    global right, wrong, characters
    if text_field.get() == word:
        characters = characters + len(word) + 1 # added 1 as a space
        right += 1
        text_field.delete(0,"end")
        list_of_words()
    else:
        print("Wrong")
        wrong += 1
        text_field.delete(0, "end")
        list_of_words()

def list_of_words():
    text_field.config(state=NORMAL)
    text_field.focus()
    shuffle(WORDS)
    text_canvas.itemconfig(text, text=WORDS[0])
    text_field.bind("<Return>", lambda event: on_click_enter(event, WORDS[0]))



window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20,bg=YELLOW)
window.geometry("800x500")
window.resizable(False,False)

canvas = Canvas(width=400, height=190, highlightthickness=0, bg=YELLOW)
keyboard = PhotoImage(file="assets/kb.png")
canvas.create_image(200,95,image=keyboard)
canvas.grid(row = 1,column = 1, padx=20, pady=20)


text_canvas = Canvas(width=650, height=30)
text = text_canvas.create_text(325,15,text="Words Appear Here",font=FONT_NAME)
text_canvas.grid(row= 3, column=0, columnspan = 2)

style = ttk.Style()
style.configure('TLabel',background=YELLOW, font=(FONT_NAME,20,"bold"))

title = ttk.Label(text="Welcome to Typing Speed Test")
title.grid(row=0, column=1)

separator = ttk.Separator(orient='horizontal')
separator.grid(row=2, column=1, ipadx=380, pady=20)

timer = ttk.Label(text="1 Min")
timer.grid(row=4, column=1, pady = 10)

text_field = ttk.Entry(width=25)
text_field.config(state=DISABLED)
text_field.grid(row = 5, column = 1)

start_button = ttk.Button(text="Start", command=lambda:[start(), list_of_words()])
start_button.grid(row=6, column=1, pady = 10)


window.mainloop()