from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(upper_text, text="French", fill="black")
    canvas.itemconfig(lower_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(upper_text, text="English", fill="white")
    canvas.itemconfig(lower_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


def remove_card():
    global to_learn
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data\words_to_learn.csv", index=False)
    return to_learn

#________________UI configuration____________________________________________________
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

upper_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
lower_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda: [new_card(), remove_card()])
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)
new_card()

window.mainloop()
