from tkinter import *
from tkinter import ttk

from tkinter import messagebox

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
COUNT = 5


def count_down(sec):
    timer.config(text=f"{sec}")
    if sec > 0:
        window.after(1000,count_down,sec-1)
    else:
        start.config(state=NORMAL)
        timer.config(text=f"{sec}")


def start():
    start.config(state=DISABLED)
    count_down(COUNT)


window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20,bg=YELLOW)
window.geometry("800x600")
window.resizable(False,False)

canvas = Canvas(width=400, height=190, highlightthickness=0, bg=YELLOW)
keyboard = PhotoImage(file="assets/kb.png")
canvas.create_image(200,95,image=keyboard)
canvas.grid(row = 1,column = 1, padx=20, pady=20)


text_canvas = Canvas(width=650, height=30)
text_canvas.create_text(50,15,text="from",font=FONT_NAME)
text_canvas.grid(row= 3, column=0, columnspan = 2)

style = ttk.Style()
style.configure('TLabel',background=YELLOW, font=(FONT_NAME,16,"bold"))

title = ttk.Label(text="Welcome to Typing Speed Test")
title.grid(row=0, column=1)

timer = ttk.Label(text="60")
timer.grid(row=4, column=1)

separator = ttk.Separator(orient='horizontal')
separator.grid(row=2, column=1, ipadx=380, pady=20)

user_input = ttk.Entry(width=25)
user_input.grid(row = 5, column = 1)

start = ttk.Button(text="Start", command=start)
start.grid(row=6,column=1)

window.mainloop()