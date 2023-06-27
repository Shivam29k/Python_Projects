from tkinter import *
from tkinter import messagebox
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------ BUTTONS WORK ----------------------------------
try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/spanish_words.csv")
to_learn = word_data.to_dict(orient="records")

def next_card():
    global current_card, fliptimer
    window.after_cancel(fliptimer)
    canvas.itemconfig(card, image=front_card)
    current_card = choice(to_learn)
    canvas.itemconfig(word_txt, text= current_card['Spanish'], fill="black")
    canvas.itemconfig(language_txt, text= "Spanish", fill="black")
    fliptimer = window.after(3000, flip_card)

    

def flip_card():
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(word_txt, text= current_card["English"], fill="white")
    canvas.itemconfig(language_txt, text= "English", fill="white")

def right_click():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def wrong_click():
    next_card()


# --------------------------------------save progress------------------------------



# ------------------------------------ UI DESIGN -----------------------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)

fliptimer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_card)
language_txt = canvas.create_text(400, 150, text="Spanish", fill="black", font=("ariel", 30, "italic"))
word_txt = canvas.create_text(400, 263, text="Word", fill="black", font=("ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=wrong_click)
wrong.grid(column=0, row=1)
right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=right_click)
right.grid(column=1, row=1)
next_card()





mainloop()