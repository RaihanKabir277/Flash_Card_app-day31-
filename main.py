# print("Projects starts here .......")

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])



window = Tk()
window.title("Fleshy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,140, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
known_btn.grid(row=1, column=1)

window.mainloop()
