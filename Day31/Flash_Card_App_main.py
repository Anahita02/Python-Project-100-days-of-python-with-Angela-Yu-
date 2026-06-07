from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn ={}

# Next Card
try:
    df = pd.read_csv(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else: 
    to_learn = df.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\data/words_to_learn.csv", index=False)
    next_card()

# Window
window =Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\images\card_front.png")
card_back = PhotoImage(file=r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
cross_button_image = PhotoImage(file=r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\images\wrong.png")
cross_button = Button(image=cross_button_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_button_image = PhotoImage(file=r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day31\images\right.png")
check_button = Button(image=check_button_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()