# print("Projects starts here .......")

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_image2)


# ------------ UI design ----------
window = Tk()
window.title("Fleshy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# --------set the time ---------
window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file="images/card_front.png")
card_image2 = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400,140, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
