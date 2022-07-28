from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
word = {}
words_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    words = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")

# ------------------------------WORD GENERATION---------------------------------------------------------#
words_data = pandas.read_csv("/Users/HP/Downloads/flash-card-project-start/data/french_words.csv")


def generate_word():
    global words_dict, word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words_dict)
    word_fr = word["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word_fr, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    word_en = word["English"]
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word_en, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    words_dict.remove(word)
    print(len(words_dict))
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# --------------------------------STARTING THE UI ------------------------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="/Users/HP/Downloads/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="/Users/HP/Downloads/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# right button
right_img = PhotoImage(file="/Users/HP/Downloads/flash-card-project-start/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

# wrong button
wrong_img = PhotoImage(file="/Users/HP/Downloads/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=1, row=1)

generate_word()

window.mainloop()
